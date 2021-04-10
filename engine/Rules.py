# -*- coding: utf-8 -*-

# NOTE: uncomment to debug
print("{}.{}".format(__package__,__name__))

# Standard libraries import.
import sys

# Third libraries import.
from lib.nihongo_hatsuon.hiragana import *
from lib.nihongo_hatsuon.katakana import *

# Projet modules import.


######################

class Rules():
    """
    Check if rules are respected.
    Contains the game's rules.

    Public attributes.

    """

    EOL = "\n"
    TAB = "\t"
    DIALOGS = {'reminder' : """Dans ce jeu, un 1er joueur écrit un mot en japonais.
Un 2ème, écrit un autre mot, dont le début est la fin du mot du 1er joueur.
Et ainsi de suite, le mot du joueur courant étant la fin du mot du joueur précédent.
Ex : ことば --> ばいく --> くだもの --> ...
Les mots seront seulement en hiragana.

Si le mot du joueur se termine par ん, c'est perdu. Ex : かんたん.

Dans cette version, les mots interdis sont :
    - les mots d'une seule more. Ex : い(胃) - stomach / か(蚊) - mosquito) ;
    - les acronymes. Ex : ヴィップ - VIP ;
    - les mots écrits en katakana. Ex : アルバイト - travail temps partiel /　イノシシ - sanglier ;
    - les "mots" commençant par ん. Ex : んです. On ne sait jamais ^^ ;
    - les mots contenant "ー" ou "・". Ex : ルール - règle / ちきん・なげっと or チキン・ナゲット - chicken nugget.
""",
               'with_ai_like' : ["Je suis bon Seigneur, je vous laisse commencer {}.",
                                 "Si vous êtes trop effrayé, entrez 0 ou cliquez",
                                 "'Je préfère fuire !!!' (en mode graphique)",
                                 "maintenat ou quand vous le souhaitez!"],
               'only_humans' : ["Si l'un d'entre vous est trop froussard, entrez 0 ou cliquez",
                                "'Je préfère fuire !!!' (en mode graphique) lors de votre tour.",
                                "",
                                "Bien, le hasard à décidé que le premier d'entre vous sera {}"],
                'yes' : "Oui",
                'no' : "Non",
                'empty_string' : " Votre réponse est vide !",
                'hiragana_only' : "Hiragana seulement ? ",
                'n_finish' : "Le mot fini par ん",
                'n_begin' : "Le mot commence par ん",
                'only_one_mora' : "Seulement une more !! Désolé, mais trop peu pour accepter !!",
                'end_begin_not_match' : "La fin du mot précédant et début de ce mot sont différents",
                'DB_found' : " trouvée dans goi.sqlite ? ",
                'already_played' : " déjà joué ? ",
                'not_yet' : "Pas encore.",
                'try_remember' : "Essayez de vous souvenir de ce mot.",
                }

    # Private attributes.
    #__dejavu = already played words.
    #__previous = just the end of one of the players previous answer.
    # __sqlmanage = sqlmanage instance adresses.

    # Public methods.

    def __init__(self, sqlmanage):
        """
        __init__ : initiate class
        @parameters : sqlmanage = sqlmanage instance address.
        @return : none.
        """
        self.__sqlmanage = sqlmanage
        self.__previous = ""
        self.__dejavu = []

    def check_answer(self, answer, first_answer):
        """
        Check for rule :
        @parameters : answer = the player answer.
                      first_answer = True if it's a first answer (1st game or after a player has lost). False if next player turn.
        @return : tuple (True, explain) if answer is accepted, everelse (False, explain).
            explain => just to explain this result.
            I also should raise an exception if not good, but i prefer use return statement
            in function.
        """
        if first_answer:
            self.__previous = "" # It's a new game.

        # Check if no answer.
        if answer == "":
            return (False, self.DIALOGS['empty_string'])

        explain = ""        # Explain what wrong or not.

        # Check if the answer if full in hiragana.
        explain += "{}{}{}".format(self.EOL, self.TAB, self.DIALOGS['hiragana_only'])
        if not self.__only_hiragana(answer):
            explain += "{}{}".format(self.DIALOGS['no'], self.EOL)
            return (False, explain)
        explain += "{}{}".format(self.DIALOGS['yes'], self.EOL)

        # Resolve the little hirigana entry problem.
        answer = self.__explode_and_correct_hiragana(answer)

        # Check if the end of the answer is "ん" or"ン". Yes, normally hiragana. But ...
        if answer[len(answer) - 1] in ["ん", "ン"]:
            explain += "{}{}{}".format(self.TAB, self.DIALOGS['n_finish'], self.EOL)
            return (False, explain)

        # Check if the begining of the answer is "ん" or"ン".
        if answer[0] in ["ん", "ン"]:
            explain += "{}{}{}".format(self.TAB, self.DIALOGS['n_begin'], self.EOL)
            return (False, explain)

        # Check if the lenght of the answer is not only one mora.
        if len(answer) == 1:
            explain += "{}".format(self.DIALOGS['only_one_mora'])
            return (False, explain)

        # Check if the begining of the answer is the then same as the end of the previous one.
        # Should be check after the 1st turn.
        if self.__previous != "" and answer[0] != self.__previous:
            explain += "{}{}{}".format(self.TAB, self.DIALOGS['end_begin_not_match'], self.EOL)
            return (False, explain)

        # Check if the word is inside the sqlite DB dictionnary.
        explain += "{}{}{}".format(self.TAB, "".join(answer), self.DIALOGS['DB_found'])
        if not self.__sqlmanage.ask_if_exist_kana("".join(answer)):
            explain += "{}{}".format(self.DIALOGS['no'], self.EOL)
            return (False, explain)
        explain += "{}{}".format(self.DIALOGS['yes'], self.EOL)

        # Check if the playing word wasn't already played before.
        explain += "{}{}{}".format(self.TAB, "".join(answer), self.DIALOGS['already_played'])
        if True in [a == answer for a in self.__dejavu]:
            explain += "{}{}".format(self.DIALOGS['yes'], self.EOL)
            return (False, explain)
        explain +=  "{}{}{}{}{}{}".format(self.DIALOGS['not_yet'], self.EOL, self.TAB, self.TAB, self.DIALOGS['try_remember'], self.EOL)

        self.__previous = answer[-1]    # Don't need a "" answer.

        explain += "OK."

        self.__dejavu.append(answer)        # Remember this answer, don't be used again.

        return (True,  explain)

    def before_to_play(self, nb_players, nickname):
        """
        Return the how to depending the number of players
        @parameters : nb_players = number of players.
                      now_player = the player who will begin.
        @return : the how to.
        """
        if nb_players == 1:
            btp = self.EOL.join(self.DIALOGS['with_ai_like']).format(nickname)
            btp += 2 * self.EOL
        else:
            btp = self.EOL.join(self.DIALOGS['only_humans']).format(nickname)
            btp += 2 * self.EOL

        return btp

    # Private methods.

    def __only_hiragana(self, answer):
        """
        Check if the answer is in Hiragana only.
        @parameters : answer = the player answer.
        @return : True = ok, False = not only Hiragana.
        """
        check_hiragana = [h in hiragana for h in answer]
        # True if a False is found, so it's inverted to be False.
        return not False in check_hiragana

    def __explode_and_correct_hiragana(self, answer):
        """
        Explode the answer in list, and resolve the problem of the little hiragana.
        It should be only one character, but it's entering as 2 one.
        @parameters : answer = the answer to check.
        @return = list of the hiragana with join of the little hiragana.
        """
        exploded_str = [c for c in answer]

        i = len(exploded_str) - 1
        while i > 0:
            if exploded_str[i] in ['ゃ', 'ゅ', 'ょ', 'ぁ', 'ぃ','ぅ', 'ぇ', 'ぉ']:
                exploded_str[i - 1] += exploded_str[i]
                exploded_str.pop(i)
                i -= 1
            i -= 1

        return exploded_str

######################

if __name__ == "__main__":
    help(Rules)
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely shiri-tory.py if eXecution right(s) is/are ON.")
    sys.exit(1)

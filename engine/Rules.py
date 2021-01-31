# -*- coding: utf-8 -*-

# NOTE: uncomment to debug
print("{}.{}".format(__package__,__name__))

# Standard libraries import.
import sys

# Third libraries import.
from lib.nihongo_hatsuon.hiragana import *

# Projet modules import.
from . import SQLManage


######################

class Rules():
    """
    Check if rules are respected.
    Contains the game's rules.

    Public attributes.

    """

    EOL = "\n"
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
                                "Bien, le hasard à décidé que le premier d'entre vous sera {}"],}

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

    def check_answer(self, answer):
        """
        Check for rule :
        @parameters : answer = the player answer.
        @return : tuple (True, explain) if answer is accepted, everelse (False, explain).
            explain => just to explain this result.
            I also should raise an exception if not good, but i prefer use return statement
            in function.
        """
        explain = ""        # Explain what wrong or not.

        # Check if the answer if full in hiragana.
        explain += "\n\tOnly Hiragana ? "
        if not self.__only_hiragana(answer):
            explain += "No\n"
            return (False, explain)
        explain += "Yes\n"

        # Resolve the little hirigana entry problem.
        answer = self.__explode_and_correct_hiragana(answer)

        # Check if the end of the answer is "ん" or"ン". Yes, normally hiragana. But ...
        if answer[len(answer) - 1] in ["ん", "ン"]:
            explain += "\tThe answer finishes with ん\n"
            return (False, explain)

        # Check if the begining of the answer is "ん" or"ン".
        if answer[0] in ["ん", "ン"]:
            explain += "\tThe answer begins with ん\n"
            return (False, explain)

        #Check if "ー" is in the word.
        explain += "\tPresence of ー ? "
        if not False in [c == "ー" for c in answer]:
            explain = "Yes\n"
            return (False, explain)
        explain += "No\n"

        # Check if "・" is in the word.
        explain += "\tPresence of ・ ? "
        if not False in [c == "・" for c in answer]:
            explain += "Yes\n"
            return (False, explain)
        explain += "No\n"

        # Check if the lenght of the answer is not only one mora.
        if len(answer) == 1:
            explain += "Only one mora !! Sorry, to easy to be accepted !!"
            return (False, explain)

        # Check if the begining of the answer is the then same as the end of the previous one.
        # Should be check after the 1st turn.
        if self.playing and answer[0] != self.__previous:
            explain += "\tThe end of previous answer and the beginning of these are different.\n"
            return (False, explain)

        # Check if the word is inside the sqlite DB dictionnary.
        explain += "\t{} found in goi.sqlite ? ".format("".join(answer))
        if not self.__sqlmanage.ask_if_exist_kana("".join(answer)):
            explain += "No\n"
            return (False, explain)
        explain += "Yes\n"

        # Check if the playing word wasn't already played before.
        explain += "\t{} already played ? ".format("".join(answer))
        if True in [a == answer for a in self.__dejavu]:
            explain += "Yes\n"
            return (False, explain)
        explain += "Not yet.\n\t\tTry to rememeber this word.\n"

        self.__previous = answer[-1]    # Don't need a "" answer.

        explain += "OK."

        self.__dejavu.append(answer)        # Remember this answer, don't be used again.

        return (True,  explain)

    def before_to_play(self, nb_players, nickname):
        """
        Return the how to depending the number of players
        @parameters : nb_players = number of players.
                      now_player = the player who will begin.
                      playersI = players' instance.
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
        check_hiragana = [h in hirahana for h in answer]
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

# -*- coding: utf-8 -*-

# Standard library import.
import sys

# Project library import.
import sqlmanage


class One_Game():
    """
    Representing one game class.

    # Public attributes.
        playing = the turn is playing.
        sqlmgt = instance of SQLManage.
        p_answer = answer of a player.
    """

    # Private attributes.
    __hirahana = [
        'あ', 'い', 'う', 'え', 'お',
        'か', 'き', 'く', 'け', 'こ',
        'が', 'ぎ', 'ぐ', 'げ', 'ご',
        'さ', 'し', 'す', 'せ', 'そ',
        'ざ', 'じ', 'ず', 'ぜ', 'ぞ',
        'しゃ', 'しゅ', 'しょ',
        'じゃ', 'じゅ', 'じょ',
        'た', 'ち', 'つ', 'て', 'と',
        'だ', 'ぢ', 'づ', 'で', 'ど',
        'な', 'に', 'ぬ', 'ね', 'の',
        'は', 'ひ', 'ふ', 'へ', 'ほ',
        'ば', 'び', 'ぶ', 'べ', 'ぼ',
        'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ',
        'ひゃ', 'ひゅ', 'ひょ',
        'びゃ', 'びゅ', 'びょ',
        'ぴゃ', 'ぴゅ', 'ぴょ',
        'ま', 'み', 'む', 'め', 'も',
        'や', 'ゆ', 'よ',
        'ゃ', 'ゅ', 'ょ',
        'ぁ', 'ぃ','ぅ', 'ぇ', 'ぉ',
        'ら', 'り', 'る', 'れ', 'ろ',
        'わ', 'を', 'ん',
        'きゃ', 'きゅ', 'きょ',
        'ぎゃ', 'ぎゅ', 'ぎょ',
        'ちゃ', 'ちゅ', 'ちょ',
        'にゃ', 'にゅ', 'にょ',
        'みゃ', 'みゅ', 'みょ',
        'りゃ', 'りゅ', 'りょ',
        'っ']
    __dejavu = []   # Already played words.
    #__previous = just the end of one of the players previous answer.



    # Public methods.
    def __init__(self):
        """
        __init__ : initiate class
        @parameters : ...
        @return : none.
        """
        self.__previous = ""

        self.p_answer = ""
        self.playing = False
        self.sqlmgt = sqlmanage.SQLManage()

    def check_answer(self):
        """
        Check the player answer (self.p_answer) following rules in README.
        Some rules are checked by program, because it should be in database yet.
        Thanks to Python 3.2 str class to understand UTF-8.
        @parameters : none.
        @return : tuple (True, explain) if answer is accepted, everelse (False, explain).
            explain => just to explain this result.
            It will be used in Game.py.
            I also should raise an exception if not good, but i should deep refund my console_mode.py
            code. Remember, it just to be kill time in train ! Maybe, in another life.
        """
        answer = self.p_answer      # YES, i'm a big useless man !!!

        # Check if no answer.
        if answer == "":
            return (False, " Your answer is empty !")

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

        # Check if the playing word wasn't already played before.
        explain += "\t{} already played ? ".format("".join(answer))
        if True in [a == answer for a in self.__dejavu]:
            explain += "Yes\n"
            return (False, explain)
        explain += "Not yet. Try to rememeber this word.\n"

        # Check if the word is inside the sqlite DB dictionnary.
        explain += "\t{} found in goi.sqlite ? ".format("".join(answer))
        if not self.sqlmgt.ask_if_exist_kana("".join(answer)):
            explain += "No\n"
            return (False, explain)
        explain += "Yes\n"

        self.__previous = answer[-1]    # Don't need a "" answer.

        explain += "OK."
        self.__dejavu.append(answer)
        return (True, explain)


    # Private methods.
    def __only_hiragana(self, answer):
        """
        Check if the answer is in Hiragana only.
        @parameters : answer = the player answer.
        @return : True = ok, False = not only Hiragana.
        """
        check_hiragana = [h in self.__hirahana for h in answer]
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
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely if eXecution right(s) is/are ON.")
    sys.exit(1)

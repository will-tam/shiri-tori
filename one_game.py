# -*- coding: utf-8 -*-

# Project library import.
import sqlmanage


class One_Game():
    """
    Representing one game class.

    # Public attributes.
        playing = the turn is playing.
        sqlmgt = instance of SQLManage.
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
        'ら', 'り', 'る', 'れ', 'ろ',
        'わ', 'を', 'ん',
        'きゃ', 'きゅ', 'きょ',
        'ぎゃ', 'ぎゅ', 'ぎょ',
        'ちゃ', 'ちゅ', 'ちょ',
        'にゃ', 'にゅ', 'にょ',
        'みゃ', 'みゅ', 'みょ',
        'りゃ', 'りゅ', 'りょ',]
    #__previous = just the end of one of the players previous answer.


    # Public methods.
    def __init__(self):
        """
        __init__ : initiate class
        @parameters : ...
        @return : none.
        """
        self.__previous = ""
        self.playing = False
        self.sqlmgt = sqlmanage.SQLManage()

    def check_answer(self, answer):
        """
        Check the player answer following rules in README.
        Some rules are checked by program, because it should be in database yet.
        Thanks to Python 3.2 str class to understand UTF-8.
        @parameters : answer = the player answer.
        @return : True = answer is accepted, everelse False
        """
        print("Check it ...", answer, "...")

        # Check if no answer.
        if answer == "":
            return False

        # Check if the answer if full in hiragana.
        if not self.__only_hiragana(answer):
            return False

        # Check if the end of the answer is "ん" or"ン". Yes, normally hiragana. But ...
        if answer[-1] in ["ん", "ン"]:
            return False

        # Check if the begining of the answer is "ん" or"ン".
        if answer[0] in ["ん", "ン"]:
            return False

        #Check if "ー" is in the word.
        if not False in [c == "ー" for c in answer]:
            return False

        # Check if "・" is in the word.
        if not False in [c == "・" for c in answer]:
            return False

        # Check if the lenght of the answer is not only one mora.
        if len(answer) == 1:
            return False

        # Check if the begining of the answer is the then same as the end of the previous one.
        if self.playing and answer[0] != self.__previous:
            return False

        # Check if the word is inside the sqlite DB dictionnary.
        if not self.sqlmgt.ask_if_exist(answer):
            return False

        self.__previous = answer[-1]    # Don't need a "" answer.

        return True


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

######################

if __name__ == "__main__":
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely if eXecution right(s) is/are ON.")
    sys.exit(1)

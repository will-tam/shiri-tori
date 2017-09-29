# -*- coding: utf-8 -*-

class One_Turn():
    """
    Representing one turn class.
    """


    # Public attributes.


    # Private methods.


    # Public methods.
    def __init__(self):
        """
        __init__ : initiate class
        @parameters : ...
        @return : none.
        """
        pass

    def ask_word(self, nickname):
        """
        Ask the player to give a word.
        @parameters : nickname = the nickname of the player.
        @return : the palyer's word.
        """
        print("{}, please your word".format(nickname), end="")
        return input(">")

    def only_hiragana(self, answer):
        """
        Check if the answer is in Hiragana only.
        @parameters : answer = the player answer.
        @return : True = ok, False = not only Hiragana.
        """
        pass

    def check_answer(self, answer):
        """
        Check the player answer.
        @parameters : answer = the player answer.
        @return : True = answer is accepted, everelse False
        """
        if answer[-1] in ["ん", "ン"]:
            return False

        # TODO : La partie qui vérifie un mot dans un dico.

        return True


    # Private methods.


if __name__ == "__main__":
    help(One_Turn)

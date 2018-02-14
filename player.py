# -*- coding: utf-8 -*-

class Player():
    """
    Representing only ONE player class.
    <Players> class parent class.

    Public attributes :
        nickname = player nickname.
        win_rounds = how many rounds a player wins.
        loose_rounds = how many rounds a player losts.
    """


    # Private attributes.


    # Public methods.
    def __init__(self, nickname):
        """
        __init__ : initiate class
        @parameters : nickname = a player nickname.
        @return : none.
        """
        # Management of the unknown players.
        self.nickname = nickname
        self.win_rounds = 0
        self.loose_rounds = 0

    def __repr__(self):
        """
        Called when we want to print the class.
        @parameters : none.
        @return : the representation class string.
        """
        to_show = [self.nickname, self.win_rounds, self.loose_rounds];
        return str(to_show)

    def tuple_it(self):
        """
        Format Player class attributes within tuple.
        @parameters : none.
        @return : the tuple it-self.
        """
        return (self.nickname, self.win_rounds, self.loose_rounds)

    def add_one_point_win(self):
        """
        Add 1 point to win points.
        @parameters : none.
        @return : none.
        """
        self.win_rounds += 1

    def add_one_point_lost(self):
        """
        Add 1 point to loose points.
        @parameters : none.
        @return : none.
        """
        self.loose_rounds += 1


    # Private methods.


######################

def find_me_a_nickname(player_num):
    """
    Add unknown to an empty player's nickname.
    @parameters : player_num = number of player who find a name.
    @return : unknown with a digit if several.
    """
    ze_best_nn = "Unknown You" if player_num == 0 else "Unknown Player {}".format(player_num)
    return ze_best_nn

######################

if __name__ == "__main__":
    print("Don't launch me directely, please !")
    print("Run python3 shiri-tory.py or directely if eXecution right(s) is/are ON.")
    sys.exit(1)

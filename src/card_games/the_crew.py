import logging

from tabulate import tabulate

from src.card_games import decks, utils, generators
from src.card_games.models import Player, BaseMission, Fold

"""
Currently this file is the entry point to play a game of The Crew.
Just call python src/card_games/the_crew.py to play a game on your terminal.
"""


logger = logging.getLogger("the_crew")


class TheCrew(object):
    """A game of The Crew is defined by a deck of cards and muliple players.
    Game follow the following rules:
    - The deck is shuffled and distributed between the players.
    - TODO...
    """

    def __init__(self, players=None):
        """Constructor of the class Bataille"""
        if players is None:
            players = utils.get_anonymous_players(3)

        self.deck = decks.get_the_crew_deck()
        self.mission_generator = generators.MissionGenerator()

        self.players = players
        self.nb_players = len(self.players)

        self.captain = None
        self.communications = []
        self.current_level = None
        self.missions = []
        self.nb_missions = 0
        self.level = 0

        self.current_fold = None

    def discover_missions(self, level: int = 1):
        self.current_level = level
        self.missions = self.mission_generator.generate(level=level)
        self.nb_missions = len(self.missions)

    def distribute_deck(self, shuffle=False):
        """Distribute all deck cards. When playing with 3 players
        Distribution is odd. First player has +1 card.
        """
        if shuffle:
            self.deck.shuffle()

        while self.deck.size() > 0:
            for _player in self.players:
                if self.deck.is_empty():
                    continue

                card = self.deck.pop()
                # blong: Find a better synthax to find a given card.
                # here we want to know if the card is the 4 black => captain.
                if card.value == 4 and card.color == "black":
                    self.captain = _player
                _player.add(card)

    def display_current_state(self):
        print("*****************************")
        print(f"The Crew: Current State #Level {self.current_level}")
        self._display_players()
        self._display_captain()
        self._display_missions()
        print("*****************************")

    def _display_players(self, with_cards: bool = False):
        print(f"****** {self.nb_players} Players:")
        for player in self.players:
            player.display_current_state(with_cards=with_cards)

    def _display_player(self, player: Player, with_cards:bool = False):
        player.display_current_state(with_cards=with_cards)

    def _display_captain(self):
        print(f"****** Captain: {self.captain}")

    def _display_missions(self):
        print("\n*********************************")
        if self.missions:
            missions_data = []
            for count, mission in enumerate(self.missions):
                missions_data.append([f"[{count}]", mission.__str__(), mission.player])
                # mission.display_current_state(index=count)
            print(tabulate(missions_data, headers=['Missions', 'Title', 'Owner']))
        else:
            print("****** No Missions - Enjoy the sea <3")

    def select_missions(self):
        # We Start from captain and increment index (modulo nb_players)
        # for each player.
        player_index = self.players.index(self.captain)
        for i in range(self.nb_missions):
            index = ( player_index + i ) % self.nb_players
            self.ask_to_select_mission(self.players[index])

    def ask_to_select_mission(self, player: Player, retry=0):
        if not retry:
            print("\n*********************************")
            print(f"****** Asking Player: {player.__str__()} to select a mission...")
            player.display_current_state(with_cards=True)
            self._display_missions()

        _input = input("\nOy ! Take a mission...\n Use number inside [.] to give your choice ?!\n")

        try:
            mission = self.select_mission(player, int(_input))
            print(f"\n******* {mission.__str__()} Selected")
        except (ValueError, IndexError) as e:
            print(e)
            self.ask_to_select_mission(player, retry + 1)

        print("*********************************\n")

    def select_mission(self, player: Player, index: int):
        # blong: Currently we don't store mission inside player.
        _mission = self.missions[index]
        if _mission.player:
            raise IndexError("Mission already taken")

        _mission.player = player
        return _mission

    def init_new_turn(self, start_player: Player):
        self.current_fold = Fold(expected_cards=self.nb_players)

    def ask_to_play_card(self, player: Player, retry=0):
        if not retry:
            player.display_current_state(with_cards=True)

        _input = input("Oy ! Play a card...\n Use number inside [.] to give your choice.")

        try:
            played_card = player.pop(int(_input))
            self.current_fold.add(played_card)
        except (ValueError):
            self.ask_to_play_card(player, retry + 1)


if __name__ == "__main__":
    level = 5
    players = utils.get_anonymous_players(3)
    the_crew = TheCrew(players=players)

    logger.warning(" --------------------------  The Crew version v0.0.0-alpha  -------------------------- ")
    logger.warning(" ************ ------------------------------------------------------------------------ ")
    logger.warning(" ************ ------------------------------------------------------------------------ ")
    logger.warning(" --- ** ------------------------------------------------------------------------------ ")
    logger.warning(" --- ** ---- ** ------ **** ------- ***** -  **** ------ **** -- ** --------- ** ----- ")
    logger.warning(" --- ** ---- ** ---- ***  ** ---- ***   --- **  *** -- ***  ** - **  -------  ** ----- ")
    logger.warning(" --- ** ---- ***** - ***** ------ **   ---- ** ** ---- ***** ---- **   ***   ** ------ ")
    logger.warning(" --- ** ---  ** ** - **   ------- ***   --- **   ** -- **   ------ ** ** ** ** ------- ")
    logger.warning(" --- ** ---  ** ** -- ****** ------ ***** - **    ** -- ****** ---- ***   *** -------- ")
    logger.warning(" ------------------------------------------------------------------------------------- ")

    print(f"****** Current Level {level}")

    the_crew.distribute_deck(shuffle=True)
    for _player in the_crew.players:
        _player.do_order_cards()

    the_crew._display_players()
    the_crew._display_captain()

    the_crew.discover_missions(level=level)

    the_crew.select_missions()

    the_crew.display_current_state()

    the_crew.init_new_turn(start_player=the_crew.captain)


    # input = input("Display Current State? (y,n)")
    # if input in ["y", "yes"]:
    #     the_crew.display_current_state()

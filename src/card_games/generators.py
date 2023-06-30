from src.card_games.decks import get_the_crew_mission_deck


class MissionGenerator:
    """Dummy Mission Generator.
    - When instantiated, it owns all possible missions inside `_missions`.
    - Use `generate(level=2)` method to recover missions.

    Currently, we only have Single Card (TheCrew I) missions.
    """

    def __init__(self, shuffled: bool = True):
        self._missions = get_the_crew_mission_deck(shuffled=shuffled)

    def generate(self, level=1):
        """Return missions based on requested level.
        :param level: Currently, The number of mission returned.
        :return: [Mission]."""

        missions = []
        for i in range(level):
            missions.append(self._missions.pop())

        return missions

import pytest

from src.card_games.generators import MissionGenerator


def test_mission_generator_is_instantiable():
    generator = MissionGenerator()
    assert isinstance(generator, MissionGenerator)


@pytest.fixture
def mission_generator():
    return MissionGenerator()


@pytest.mark.parametrize(
    "level,expected_count",
    [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
    ],
)
def test_mission_generator(level, expected_count, mission_generator):
    missions = mission_generator.generate(level=level)
    assert len(missions) == expected_count

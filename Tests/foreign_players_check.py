import json
import sys

from InputData.parse_team_json import check_max_four_foreign_player

file_path = sys.argv[1]  # gets the filepath from console
file = open(file_path)
data = json.load(file)


def test_max_foreign_players():
    check_foreign_players_count = check_max_four_foreign_player(data)
    assert check_foreign_players_count <= 4, 'You can not have more than 4 foreign player in the team..!'
    print('The team combination is valid with not more than four foreign players in the team..!')

file.close()

if __name__ == '__main__':
    test_max_foreign_players()

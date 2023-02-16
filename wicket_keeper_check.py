import json
import sys

from parse_team_json import check_min_one_wicket_keeper

file_path = sys.argv[1]  # gets the filepath from console
file = open(file_path)
data = json.load(file)


def test_wicket_keeper():  # checks for wicket keeper logic
    check_wk_count = check_min_one_wicket_keeper(data)
    assert check_wk_count > 0, "Need At leas one wicket keeper in the team..!"


file.close()

if __name__ == '__main__':
    test_wicket_keeper()

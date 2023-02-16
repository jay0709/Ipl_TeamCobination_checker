import json
import sys

from InputData.parse_team_json import check_min_one_wicket_keeper

file_path = sys.argv[1]  # gets the filepath from console
file = open(file_path)
data = json.load(file)


def test_min_wicket_keeper():  # checks for wicket keeper logic
    check_wk_count = check_min_one_wicket_keeper(data)
    assert check_wk_count > 0, "Need At leas one wicket keeper in the team..!"
    print('The team combination is valid with at least One wicket keeper..!')


file.close()

if __name__ == '__main__':
    test_min_wicket_keeper()

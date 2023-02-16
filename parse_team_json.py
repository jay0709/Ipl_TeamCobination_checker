import json


def check_min_one_wicket_keeper(json_data):
    wk_count = 0
    for item in json_data['player']:
        if item['role'] == 'Wicket-keeper':
            wk_count = wk_count + 1
    return wk_count


def check_max_four_foreign_player(json_data):
    fp_count = 0
    for item in json_data['player']:
        if item['county'] != 'India':
            fp_count = fp_count + 1
    return fp_count

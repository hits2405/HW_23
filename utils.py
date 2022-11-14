from typing import Generator

from functions import filter_data, map_data, unique_data, sort_data, limit_data, regexp_data


FILE = 'data/apache_logs.txt'

params_dict: dict = {
    'filter': filter_data,
    'map': map_data,
    'unique': unique_data,
    'sort': sort_data,
    'limit': limit_data,
    'regex': regexp_data
}


def read_file(filename: str) -> Generator:
    with open(filename) as file:
        for line in file:
            yield line


def query_params(cmd1, value1, cmd2, value2, data):
    pre_data = read_file(FILE)
    if cmd2:
        a: dict = params_dict[cmd1](params=value1, data=pre_data)
        res: dict = params_dict[cmd2](params=value2, data=a)
        return res
    else:
        a: dict = params_dict[cmd1](params=value1, data=pre_data)
        return a



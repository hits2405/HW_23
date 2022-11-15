from typing import Generator, Iterable, Dict, List

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


def query_params(cmd1: int, value1: str, cmd2: int, value2: str, data: Iterable[str]) -> Dict[str, List[str]]:
    pre_data = read_file(FILE)
    if cmd2:
        a_1: dict = params_dict[cmd1](params=value1, data=pre_data)
        res: dict = params_dict[cmd2](params=value2, data=a_1)
        return res
    else:
        a_2: dict = params_dict[cmd1](params=value1, data=pre_data)
        return a_2

import json 

import requests

import filepaths

def read_stats_metadata() -> dict:
    with open(filepaths.NSO_STATS_METADATA) as json_file:
        stats_metadata = json.load(json_file)
    return stats_metadata

def download_csv(url: str) -> str:
    r = requests.get(url)
    tmp_filepath = '/tmp/temp.csv'
    open(tmp_filepath, 'wb').write(r.content)
    return tmp_filepath
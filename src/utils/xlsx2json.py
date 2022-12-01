import pandas as pd
import json

async def convert2json(file):
    df = pd.read_excel(file, engine='openpyxl')
    str_object = df.to_json(force_ascii=False, orient='records')
    json_dict = json.loads(str_object)
    dest = f'{file.split(".")[0]}.json'
    with open(dest, 'w') as file:
        json.dump(json_dict, file, ensure_ascii=False)
    return dest

async def convert2jsonRecs(file):
    df = pd.read_excel(file, engine='openpyxl')
    str_object = df.to_json(force_ascii=False, orient='columns')
    json_dict = json.loads(str_object)
    dest = f'{file.split(".")[0]}.json'
    with open(dest, 'w') as file:
        json.dump(json_dict, file, ensure_ascii=False)
    return dest
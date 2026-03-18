import gzip
import re
from lxml import html
import json
def load(file):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
        return content

def gzip_html(file):
    with gzip.open(file,"rt",encoding="utf-8") as f:
        data=f.read()
        return data

def html_write(file):
    with open("lands.html","w") as f:
        f.write(file)
def get_json(text):
    tree = html.fromstring(text)

    raw = tree.xpath('string(//script[@id="app-root-state"])')
    if isinstance(raw, list):
        raw = raw[0] if raw else ""

    clean = (raw
             .replace('&q;', '"')
             .replace('&s;', "'")
             .replace('&a;', '&')
             .replace('&g;', '>')
             .replace('&l;', '<')
             )

    data=json.loads(clean)
    json_data = parse_nested_json(data)

    with open('land.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4)

    return json_data


def parse_nested_json(obj):
    if isinstance(obj, dict):
        new_obj = {}
        for key, value in obj.items():

            if isinstance(value, str):
                value_strip = value.strip()
                if (value_strip.startswith("{") and value_strip.endswith("}")) or (
                        value_strip.startswith("[") and value_strip.endswith("]")):
                    value = json.loads(value_strip)

            new_obj[key] = parse_nested_json(value)
        return new_obj

    else:
        return obj

def xpath_file(Xpath_file):
    with open(Xpath_file, "r") as f:
        XPATHS = json.load(f)
        return XPATHS
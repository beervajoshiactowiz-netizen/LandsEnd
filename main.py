from parser import parser
from models import Products
from db_config import create_table,insert_into_db
from lxml import html
import time
from utils import gzip_html,get_json


file="401068.html.gz"
table_name="Products"

def main():
    create_table(table_name)
    html_content = gzip_html(file)
    json_file = get_json(html_content)
    result=parser(json_file)
    validated=[]
    for prod in result:
        try:
            validated.append(Products(**prod))
        except Exception as e:
            print("Validation Error: ",e)
    if validated:
        insert_into_db(table_name,validated)

if __name__=="__main__":
    st=time.time()
    main()
    et=time.time()
    print(et-st)
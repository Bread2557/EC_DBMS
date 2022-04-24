import dbms
import pandas as pd
import os


def deconstruct_query(query):
    query.replace(",", " ")

    keywords = ["select", "from", "where"]
    keywords_contents = dict.fromkeys(keywords)
    for key in keywords_contents:
        keywords_contents[key] = []

    parts_of_query = query.split(" ")
    temp_keyword = None
    for string in parts_of_query:
        if string.strip().lower() in keywords:
            temp_keyword = string
            continue
        keywords_contents[temp_keyword.lower().strip()] += [string]

    return keywords_contents

    # keys_states = ["SELECT/UPDATE", "columns", "FROM", "tables", "WHERE", "clause"] --Automat zur Validierung der Abfrage für später
    # automaton = dict.fromkeys(keys_states)


def user_input_query():
    print("Enter query line by line, finish with '#END' \n")

    query = ""

    while True:
        temp = input("")
        if temp == "#END":
            break
        query += str(temp + " ")

    return query


def execute_query(dict_instructions):
    table_name = dict_instructions["from"]
    data = dbms.read_data(os.path.join(os.path.dirname(__file__), str(table_name[0] + ".csv")))

    data = data.loc[dict_instructions["select"]]

    print(data)


def start():
    query = user_input_query()
    keywords_contents = deconstruct_query(query)
    execute_query(keywords_contents)


start()

#!/usr/bin/python3
"""
Script that adds all arguments to a Python
list, and saves them to a file
    Description:
        We have a file (if not, we create it)
        This file is named add_item.json in our system

        We want to achieve three things:
            Load this file:
                --we check if this file exist using the
                os.path module
                --if it is successful, we call the load function
                --then we collec all its content with our list varible
                -- Done
            Collect more data inbetween:
                -- more data could be stored in our list
                -- we use the sys.argv module to do that
                -- if our argv len is > 1, we append the
                    command line argument into our list
            Save
                -- we call our save function to save
                    all our python list object in to the filname

"""
from os import path
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    save_file = "add_item.json"
    python_list = []

    if path.exists(save_file) and path.isfile(save_file):
        python_list = load_from_json_file(save_file)

    if len(argv) > 1:
        for argz in argv[1:]:
            python_list.append(argz)

    save_to_json_file(python_list, save_file)

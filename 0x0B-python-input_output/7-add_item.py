#!/usr/bin/python3
import sys
from typing import List
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def add_items(args: List[str]):
    # Load the list from the JSON file
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    # Add the new items to the list
    items.extend(args)

    # Save the list to the JSON file
    save_to_json_file(items, "add_item.json")

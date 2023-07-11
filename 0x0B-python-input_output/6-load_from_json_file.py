#!/usr/bin/python3
"""Definition of a JSON file-reading function."""
import json

def load_from_json_file(filename):
    """This method creates a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)

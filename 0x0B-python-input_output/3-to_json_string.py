#!/usr/bin/python3
"""Definition of a string-to-JSON function."""
import json

def to_json_string(my_obj):
    """This method returns the JSON representation of
	a string object."""
    return json.dumps(my_obj)

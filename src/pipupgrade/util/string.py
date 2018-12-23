# imports - standard imports
import re

_REGEX_ANSI_ESCAPE = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")

def strip_ansi(string):
    string = _REGEX_ANSI_ESCAPE.sub("", string)
    return string

def pluralize(string, count = 1):
    # A very shitty pluralizer
    if not string.endswith("s"):
        if count > 1:
            string += "s"
    
    return string
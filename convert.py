from typing import Optional

""""
This function takes a string value, and will attempt to change it to a float. However, it
can only do this if the string is a number containing a '.' (so essentially it just has to
 be a regular float. And, if it does not work, then it will be because the value is actually 
 not a float. If this is the case, then the "except" will cause it to return "None."
"""""""""

def str_to_float(string: str) -> Optional[float]:
    try:
        if "." in string:
            return float(string)
    except TypeError:
        return None
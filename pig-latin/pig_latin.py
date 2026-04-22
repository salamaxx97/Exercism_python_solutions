"""pig latin """
import re

def translate(text):
    """pig latin translation"""
    if " " in text :
        return " ".join([translate(word) for word in text.split()])
    
    #Rule 1
    if re.match("^([aioue]|xr|yt)",text) :
        return text+"ay"
    
    #Rule 3
    if re.match("^[^aeoiu]*qu",text):
        letter=text[0]
        while letter != "u" :
            letter=text[0]
            text=text[1:]+letter
        return text+"ay"
    #Rule 4
    if re.match("^[^aeoiu]+y",text):
        letter=text[0]
        while letter != "y" :
            text=text[1:]+letter
            letter=text[0]
        return text+"ay"
    
    #Rule 2
    if re.match("^[^aeiou]+",text):
        letter=text[0]
        while letter not in "aeoui" :
            text=text[1:]+letter
            letter=text[0]
        return text+"ay"
    return text
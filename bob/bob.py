""" what will bob says """

def response(hey_bob):
    """ what will he says """
    if len(hey_bob) == 0 or hey_bob.isspace() :
        return   "Fine. Be that way!"
        # This is how he responds to silence. The convention used for silence is nothing, or various combinations of whitespace characters.
    hey_bob=hey_bob.strip()
    if hey_bob[-1]=="?" and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
         #This is what he says if you yell a question at him.
    if   hey_bob[-1]=="?" :
        return "Sure." 
        #This is his response if you ask him a question, such as "How are you?" The convention used for questions is that it ends with a question mark.
    if hey_bob.isupper() :    
        return "Whoa, chill out!"
        #This is his answer if you YELL AT HIM. The convention used for yelling is ALL CAPITAL LETTERS.
    
    return "Whatever." #This is what he answers to anything else.
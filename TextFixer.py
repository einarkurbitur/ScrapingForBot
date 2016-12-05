import re
from htmlentitydefs import name2codepoint as n2c

def entity(text):
    if text[:2] == "&#":
        try:
            if text[:3] == "&#x":
                return unichr(int(text[3:-1], 16))
            else:
                return unichr(int(text[2:-1]))
        except ValueError:
            pass
    else:
        guess = text[1:-1]
        numero = n2c[guess]
        try:
            text = unichr(numero)
        except KeyError:
            pass
    return text


def filter_tweet(text):
    text = re.sub(r'\b(RT|MT) .+','',text) #take out anything after RT or MT
    text = re.sub(r'(\#|@|(h\/t)|(http))\S+','',text) #Take out URLs, hashtags, hts, etc.
    text = re.sub(r'\n','', text) #take out new lines.
    text = re.sub(r'\"|\(|\)', '', text) #take out quotes.
    htmlsents = re.findall(r'&\w+;', text)
    if len(htmlsents) > 0 :
        for item in htmlsents:
            text = re.sub(item, entity(item), text)
    text = re.sub(r'\xe9', 'e', text) #take out accented e
    return text


def filter_lines(lines):
    """ Filters multiple lines.
    Should be given a list os strings:
    E.g.
        [
          'tweet one.',
          'tweet two,',
          'tweet three'
        ]
    """
    outlines = []
    for line in lines:
        outlines.append(filter_tweet(line))
    outtext = "/n".join(outlines)
    return outtext

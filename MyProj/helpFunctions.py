import re
from unidecode import unidecode

def separateString(str, clear=True):
    if clear:
        # str = re.sub("[\.]", " ", str)
        # str = re.sub("[$+&'-]", "", str)
        str = re.sub("[$+&'-\.]", "", str)
    REGEX = r"\b\S+\b"
    finder = re.compile(REGEX)

    matches = re.findall(finder, str)
    return matches


def toLatin(str):
    return unidecode(str)



test = "(St.Augst bridge), South-West Torreluca! B&B O'Dell Cabin Wastlgasse MM-505?"
testLatin = "Ура товарищи! | դարու հայ զօրավար | җирдә ваграк елгалар | 節の明確化のために"
# re.sub("[-()!?,\[\](){}]|\s*[\.&!?]?\s+|\.$", " ", "[{(St.Augst bridge), South-West]} . a - a Torreluca! B&B O'Dell! & Cabin& Wastlgasse MM-505?.".lower()).split()

if __name__ == "__main__":
    print(separateString(test))
    print(separateString(testLatin))
    print(separateString(toLatin(testLatin)))
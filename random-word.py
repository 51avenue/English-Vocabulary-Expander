import random
import requests
from bs4 import BeautifulSoup
words = ["sarcasm",
         "disseminate",
         "savage",
         "consequence",
         "intact",
         "be spoken for",
         "interact",
         "conventional",
         "represent",
         "radical",
         "rational",
         "servant",
         "mud",
         "silly",
         "fur",
         "majesty",
         "glimpse",
         "stumble onto",
         "cruel",
         "akin",
         "disturbing",
         "snotty",
         "ranch",
         "pinch",
         "phony",
         "soggy",
         "janitor",
         "adore",
         "gobble",
         "modest",
         "senator",
         "leverage",
         "elaborate",
         "fragile",
         "mock",
         "chap",
         "regard",
         "fault",
         "soppy",
         "sugarcoat",
         "embrace",
         "conscience",
         "stiff",
         "reign",
         "delicacy",
         "bashful",
         "exclamation",
         "asset",
         "double-cross",
         "deceive",
         "secretary",
         "anthem",
         "raspy",
         "cripple",
         "cherished",
         "attorney",
         "stern",
         "sham",
         "brainy",
         "gasp",
         "arise",
         "harsh",
         "particle",
         "infatuated",
         "veto",
         "intensity",
         "profound",
         "forger",
         "weary",
         "mumble",
         "predecessor",
         "representative",
         "high horse",
         "obsession",
         "fascinated",
         "hubris",
         "persistent",
         "rogue",
         "fugitive",
         "karma",
         "live in the present",
         "mirage",
         "happenstance",
         "it was just luck",
         "perimeter",
         "sponge up everything you see",
         "belly",
         "rumor",
         "in a nutshell",
         "slick",
         "sequel",
         "sunken",
         "contradiction",
         "inconsistency",
         "adjacent",
         "pedestrian",
         "sterilize",
         "circulate",
         "make amends",
         "bear witness",
         "quarrel",
         "eyelids",
         "grope",
         "erratic",
         "reconcile",
         "distress",
         "bail",
         "alderman",
         "deliberation",
         "humble",
         "personnel",
         "liable",
         "commotion",
         "onlooker",
         "filthy",
         "sewer",
         "quandary",
         "musingly",
         "chuckle",
         "deftly",
         "obscurantism",
         "mess around",
         "funnies",
         "straddle",
         "lap",
         "mend",
         "limber",
         "biggity",
         "roam",
         "wander",
         "elaborate",
         "greenhorn",
         "dusk",
         "po",
         "poverty",
         "somber",
         "cordial",
         "inscrutable",
         "latter",
         "tucked his tail",
         "palace",
         "decorum",
         "kinfolk",
         "blood kin",
         "fracture",
         "make the rounds",
         "prudent",
         "bleak",
         "plight",
         "composure",
         "patronize",
         "endorse",
         "advocate",
         "amicable"]
words.sort()
#
theword = random.choice(words)
html = requests.get("http://www.merriam-webster.com/dictionary/%s" % theword)
soup = BeautifulSoup(html.text, "lxml")
desc1 = soup.find("ul", "definition-list no-count")
desc2 = soup.find("ol", "definition-list")
print ("___________________________________")
total = len(words)
print ("\n")
print ("Welcome to The English Vocabulary Expander!\n"
       "\n"
       "You can view the word list by entering w.\n"
       "Press enter to continue.")
print ("\n")
print ("%d words(idioms) available" % total)
print("\n")
print ("___________________________________")
while 0 == 0:
    if input() == "w":
        print("\n")
        print("\n".join(words))
        print("\n")
        print("___________________________________")
    else:
        print("\n")
        print(theword)
        print("\n")
        input()
        try:
            print (desc1.get_text())
        except:
            try:
                for node in desc2:
                    print (" ".join(node.findAll(text=True)))
            except:
                print ("think yourself")
        print("\n")
        print("___________________________________")
        theword = random.choice(words)
        html = requests.get("http://www.merriam-webster.com/dictionary/%s" % theword)
        soup = BeautifulSoup(html.text, "lxml")
        desc1 = soup.find("ul", "definition-list no-count")
        desc2 = soup.find("ol", "definition-list")

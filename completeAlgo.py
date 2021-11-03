import webbrowser, requests
from bs4 import BeautifulSoup
from nltk.corpus import wordnet


#===================================synonems func=======================================
def syno(lis):

    synony = []

    for x in lis:
        for syn in wordnet.synsets(x):
            for l in syn.lemmas():
                synony.append(l.name())

    synony = dict.fromkeys(synony)
    return synony
#================================End synonms func========================================


#================================ Wiki func==============================================

def wikfunc(lis):
 a = []
 for wor in lis:
   google_search = requests.get("https://en.wiktionary.org/wiki/" + wor)
   soup = BeautifulSoup(google_search.text, 'html.parser')
   #print(soup.prettify())
   der = soup.find_all('div', { "class" : "derivedterms term-list ul-column-count"})
   exm = soup.find_all('b')
   for x in exm:
           a.append(x.getText().lower())
        #print(x.getText())
   for xd in der:
           a.append(xd.getText().lower())
 word_wik = []
 aa = list(dict.fromkeys(a))
 for x in aa:
     if "1" not in x and "2" not in x and "3" not in x and "4" not in x and "5" not in x and "6" not in x and "7" not in x and "8" not in x and "9" not in x and "0" not in x and "(" not in x and ":" not in x:
       word_wik.append(x)

 test_list = list(filter(None, word_wik))
 return test_list

#===========================================End Wik func=====================================================

#===========================================google func =====================================================


def words(s, wor):
    k = s.split()
    word = wor
    j = 0
    ar = []
    for x in k:

        if j == 3:
            # print(x)
            ar.append(x)
            j = 0

        if j == 2:
            if x == "the" or x == "be":
                # print(x)
                j = 3
            else:
                # print(x)
                ar.append(x)
                j = 0

        if j == 1:
            if x == "and" or x == "&":
                # print(x)
                j = 2

        if x == word:
            # print(x)
            j = 1

    return list(dict.fromkeys(ar))


def get_result(lisu):
    aar = []
    ar_word = []
    for word in lisu:
        google_search = requests.get("https://www.google.com/search?q=" + word + " and")
        soup = BeautifulSoup(google_search.text, 'html.parser')

        # print (soup.prettify())

        search_result = soup.select('h3')
        # print (search_result)

        for x in search_result:
            # print (x.getText().lower())
            ar_word = ar_word + words(x.getText().lower(), word)

    ar_word = list(dict.fromkeys(ar_word))
    return ar_word


#============================================== End Google Func ====================================================

#==============================================Main ================================================================



# F_1 my_list = ["shake", "flow", "burn", "drown", "fly", "collide"]

# F_2 my_list = ["see", "hear", "smell", "feel", "touch", "sense", "taste"]

# F_3 my_list = ["injure", "cancel", "destroy", "blow", "die"]

# F_4 my_list = ["high", "low", "strong","intense"]

# F_5 my_list = ["i", "we"]

# F_6 my_list = ["office", "area", "building","home"]

# F_9 my_list = ["make", "wake", "play","watch", "speak", "sleep", "clean"]

# F_10 my_list = ["now", "today", "just","month", "year"]

# F_12 my_list = ["careful", "watch", "avoid","alert", "danger", "warn"]
# F_13
my_list = ["earthquack", "wildfire", "bomb","blast", "hurricane", "flood"]

sn = list(dict.fromkeys((syno(my_list))))

#for x in sn:
# print(x)


sn2 = list(dict.fromkeys((wikfunc(sn))))

#sn3 = list(dict.fromkeys((get_result(sn2))))

# sn4 = list(dict.fromkeys(sn + sn2 + sn3))

sn4 = list(dict.fromkeys(sn + sn2))



filename = "F_13.csv"
f = open(filename , "w", encoding="utf-8")
header = "F_13\n"

f.write(header)


for s in sn4:

    f.write(s + "\n")
    print(s)
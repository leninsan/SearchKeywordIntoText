text = "Un texto argumentativo busca transmitir un punto de vista sobre un tema en particular con la intención de persuadir al receptor. Por ejemplo: una carta de opinión. Estos tipos de texto suelen predominar en los debates públicos, las negociaciones y los parlamentos nacionales."

keywords = []
permission2 = ""

count = []


def insertWord():
    keyword = input("Insert the word to search:\n")
    keywords.append(keyword)
    count.append(0)

insertWord()

while (True):
    
    permission2 = input("y/n if you want add more words:\n")
    if permission2 == "y":   
        insertWord()
    elif permission2 == "n":
        print("the system is search the words given:\n")
        break
    else:
        print("insert a letter available\n")


def counter(): 
    
    for word in text.split():
        count2 = 0
        for keyword in keywords:
            if keyword == word:
                count[count2] += 1
            count2 += 1
    return count2;


counter()

for i in range(len(keywords)):
    print(f"the word '{keywords[i]}' is into the text {count[i]} time")
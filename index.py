import requests
import random



def getWords():

    url = 'https://random-words-api.kushcreates.com/api'
    param = {'category':'wordle', 'length':5, 'words':1000}

    try:
        resp = requests.get(url,params=param)
    except:
        print("There was an error in connecting to the random words API")

    words = []
    data = (resp.json())
    for item in data:
        words.append(item["word"])
    
    index = random.randint(0,979)
    
    return words[index:index+20]

def getMeaning(words):

    data = ''
    finalWord = None
    for word in words:

        url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
        resp = requests.get(url)
        data = resp.json()
        if isinstance(data,list):
            finalWord = word
            break
    
    return(finalWord,data[0]['meanings'][0]['definitions'][0]['definition'])


def test(found,word,guess):

   
    for i,g in enumerate(guess.lower()):
        for j,w in enumerate(word.lower()):
            if g == w and i == j:
                found[i] = '🟩'
            elif g==w:
                found[i] = '🟨'
        
    return("".join(found))

found = ['*','*','*','*','*']
words = getWords()
word, meaning = getMeaning(words)
won = False

print(f"**********{word}***********\n")
print("You need to guess a 5 letter word\n")
print(f"The word means: {meaning}")

for i in range(6):

    if won:
        break
    guess = "abc"
    while len(guess)  != 5:
        guess = input("Enter your guess (5 characters): ")
    if '*' in found:
        test(found, word, guess)
        print(''.join(found))
        
    if guess == word:
        print("You found the word!")
        won = True
        

if not won:
    print("You lose")

import random

# Select a word randomly from a list of words
file = open('wordlist.txt', 'r')
lines=file.readlines()
word = random.choice(lines)

# Variables definition
lives = 7
choices = []
result = []
i = 0


#The result list shall be by default composed of hyphens
for i in range(len(word)):
    result.insert(i,'_')


#While the number of lives is not equal to 0
while lives != 0:

    #Variable to count a successful move from the user
    a = 0

    #A loop to check user's input
    while True:
        
        letter = input('Guess a letter : ')
        

        if letter.isalpha() == False :
            print ('You must type a letter.')
        elif len(letter) > 1 :
            print("Sorry, you must type only one letter.")
        else :
            break

  
    #Store user's choice in a variable
    choices += letter

    #Transform the word into a list
    word = list(word)

    for i in range(len(word)):
        if word[i] == letter :
            result[i] = letter
            a +=1
   
    if a == 0:
        print ('Your letter, ', letter,', is not in the word')


    i += 1

    lives = lives - 1
   
   #Convert choices variable to string and upper cases
    finalchoices = ' '.join(choices)
    ultimatechoices = finalchoices.upper()


    #Tell the user how many lives they have left
    print('You have', lives ,'remaining lives and you have used these letters : ', ultimatechoices)
    #Tell the user what the current word is 
    finalresult = ' '.join(result)
    ultimateresult = finalresult.upper()
    print('Current word : ',ultimateresult)

finalword = ' '.join(word)
ultimateword = finalword.upper()
print('The correct word was', ultimateword)

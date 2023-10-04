import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    return random.choice(wordlist)


wordlist = load_words()
secret_word=choose_word(wordlist)

def is_word_guessed(secret_word,letters_guessed):
    if letters_guessed in secret_word:
        return True
    else:
        return False
    
    
def get_guessed_word(secret_word,letters_guessed):
    c="" 
    s=""
    for letter in secret_word:
        if letter in letters_guessed:
            s+="_ "
            c+=letter
        else:
            c+="_ "
            s+=letter
    return (s,c)


def get_available_letters(letters_guessed):
    c=""
    s="abcdefghijklmnopqrstuvwxyz"
    for letter in s:
        if letter not in letters_guessed:
            c+=letter
    return c


def hangman(secret_word):
    total_score=0
    unique=""
    for j in secret_word:
        if j not in unique:
            unique+=j
    total_score=len(unique)
    warnings=3
    letter_list=[]
    word=secret_word
    guess=6
    letter_guessed=''
    correct_word=""
    print("Welcome to the game Hangman !")
    print("I am thinking of a word that is "+str(len(secret_word))+" letters long.")
    for i in secret_word:
        correct_word+="_ "
    while guess>0:
        test=get_available_letters(letter_list)
        print("You have "+str(warnings)+" warnings left.")
        print("You have "+str(guess)+" guesses left.")
        print("Available letters: "+test)
        letter_guessed=input("Please guess a letter: ")
        if warnings>0 and letter_guessed not in "abcdefghijklmnopqrstuvwxyz":
            warnings-=1
            print("Oops! That is not a valid letter. You have "+str(warnings)+" warnings left: "+correct_word)
            print("________________________________________________")
            continue
        if (warnings==0 and letter_guessed not in "abcdefghijklmnopqrstuvwxyz"):
            guess-=1
            print("Oops! That is not a valid letter. You have "+str(guess)+" guesses left: "+correct_word)
            print("________________________________________________")
            continue
        if letter_guessed not in test and warnings>0:
            warnings-=1
            print("You have already guessed that letter. You have "+str(warnings)+" warnings left: "+correct_word)
            print("________________________________________________")
            continue
        if letter_guessed not in test and warnings==0:
            guess-=1
            print("You have already guessed that letter. You have "+str(guess)+" guesses left: "+correct_word)
            print("________________________________________________")
            continue
        letter_list.append(letter_guessed)
        (word,correct_word)=get_guessed_word(secret_word, letter_list)
        if is_word_guessed(secret_word,letter_guessed):
            print("Good guess: "+ correct_word)
        elif letter_guessed in "aeiou":
            print("Oops! That letter is not in my word: "+ correct_word)
            guess-=2
        else:
            print("Oops! That letter is not in my word: "+ correct_word)
            guess-=1
        if '_' not in correct_word:
            print("Congratulations...! You have guessed the word correctly..")
            print("Your total score for this game is: "+str(total_score*guess))
            print("________________________________________________")
            break
        if guess<=0:
            print("Sorry! You've run out of guesses...")
            print("The correct word was: "+secret_word)
        print("________________________________________________")


def match_with_gaps(my_word, other_word):
    word=""
    for letter in my_word:
        if letter not in " ":
            word+=letter
    for position in range(len(word)):
        if word[position] not in "_":
            if(word[position] != other_word[position]):
                return ""
    return other_word


def show_possible_matches(my_word,test):
    wordlist=load_words()
    possible_matches=[]
    actual_list=[]
    printable_list=[]
    word=""
    for letter in my_word:
        if letter not in " ":
            word+=letter
    for test_word in wordlist:
        if(len(word)==len(test_word)):
            actual_list.append(test_word)
    for test_word in actual_list:
        possible_matches.append(match_with_gaps(my_word,test_word ))
    for test_word in possible_matches:
        if test_word not in "":
            printable_list.append(test_word)
    if len(printable_list)>0:
        return printable_list
    else:
        return "No matches found.."


def hangman_with_hints(secret_word):
    total_score=0
    unique=""
    for j in secret_word:
        if j not in unique:
            unique+=j
    total_score=len(unique)
    warnings=3
    get_help=3
    letter_list=[]
    word=secret_word
    guess=6
    letter_guessed=''
    correct_word=""
    print("Welcome to the game Hangman !")
    print("I am thinking of a word that is "+str(len(secret_word))+" letters long.")
    for i in secret_word:
        correct_word+="_ "
    while guess>0:
        test=get_available_letters(letter_list)
        print("You have "+str(warnings)+" warnings left.")
        print("You have "+str(guess)+" guesses left.")
        print("You have "+str(get_help)+" hints left.")
        print("Available letters: "+test)
        letter_guessed=input("Please guess a letter: ")
        if get_help>0 and letter_guessed in "*":
            get_help-=1
            print(show_possible_matches(correct_word,test))
            continue
        if get_help<1 and letter_guessed in "*":
            print("You have no hints left: "+correct_word)
            continue
        if warnings>0 and letter_guessed not in "abcdefghijklmnopqrstuvwxyz":
            warnings-=1
            print("Oops! That is not a valid letter. You have "+str(warnings)+" warnings left: "+correct_word)
            print("________________________________________________")
            continue
        if (warnings==0 and letter_guessed not in "abcdefghijklmnopqrstuvwxyz"):
            guess-=1
            print("Oops! That is not a valid letter. You have "+str(guess)+" guesses left: "+correct_word)
            print("________________________________________________")
            continue
        if letter_guessed not in test and warnings>0:
            warnings-=1
            print("You have already guessed that letter. You have "+str(warnings)+" warnings left: "+correct_word)
            print("________________________________________________")
            continue
        if letter_guessed not in test and warnings==0:
            guess-=1
            print("You have already guessed that letter. You have "+str(guess)+" guesses left: "+correct_word)
            print("________________________________________________")
            continue
        letter_list.append(letter_guessed)
        (word,correct_word)=get_guessed_word(secret_word, letter_list)
        if is_word_guessed(secret_word,letter_guessed):
            print("Good guess: "+ correct_word)
        elif letter_guessed in "aeiou":
            print("Oops! That letter is not in my word: "+ correct_word)
            guess-=2
        else:
            print("Oops! That letter is not in my word: "+ correct_word)
            guess-=1
        if '_' not in correct_word:
            print("Congratulations...! You have guessed the word correctly..")
            print("Your total score for this game is: "+str(total_score*guess))
            print("________________________________________________")
            break
        if guess<=0:
            print("Sorry! You've run out of guesses...")
            print("The correct word was: "+secret_word)
        print("________________________________________________")

choice=input("Do you want hints in your game ? Press Y for Yes and N for no: ")
if choice in "Yy":
    print("Then press * for hints .. ")
    hangman_with_hints(secret_word)
elif choice in "Nn":
    hangman(secret_word)
else:
    print("Wrong choice...!")

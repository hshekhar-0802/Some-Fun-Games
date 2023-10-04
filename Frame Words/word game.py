import string
import random
import math

WORDLIST_FILENAME="words.txt"
vowels=list("aeiou")
consonants=list("bcdfghjklmnpqrstvwxyz")
SCRABBLE_LETTER_VALUES = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist
wordlist=load_words()

def get_word_score(hand_size, word):
    first_component=0
    second_component=0
    for letter in word:
        if letter in SCRABBLE_LETTER_VALUES:
            first_component+=SCRABBLE_LETTER_VALUES[letter]
    diff=3*(hand_size-len(word))
    pro=7*len(word)
    second_component=pro-diff
    if second_component>1:
        return first_component*second_component
    else:
        return first_component


def get_frequency_dict(word):
    frequency_dict={}
    for letter in word:
        counter=0
        for lett in word:
            if lett==letter:
                counter+=1
        if letter not in frequency_dict:
            frequency_dict[letter]=counter
    return frequency_dict


def display_hand(frequency_dict):
    hand=""
    for key in frequency_dict.keys():
        for i in range(frequency_dict[key]):
            hand=hand+key+" "
    return hand

def display_hand_without_space(frequency_dict):
    hand=""
    for key in frequency_dict.keys():
        for i in range(frequency_dict[key]):
            hand=hand+key
    return hand

def deal_hand(hand_size):
    hand_vowel=hand_size//3
    hand_consonant=hand_size-hand_vowel
    word=""
    for i in range(hand_vowel-1):
        choice=random.choice(vowels)
        word+=choice
    word+="*"
    for i in range(hand_consonant):
        choice=random.choice(consonants)
        word+=choice
    return word


def update_hand(hand,word):
    new_hand=get_frequency_dict(hand)
    for letter in word:
        if letter in new_hand and new_hand[letter]>0:
            new_hand[letter]-=1
        if letter in new_hand and new_hand[letter]<1:
            del(new_hand[letter])
    return new_hand


def is_valid_word(word):
    if "*" in word:
        for char in "aeiou":
            word_test=word.replace("*",char)
            if word_test in wordlist:
                return True
        return False
    if word in wordlist:
        return True
    else:
        return False


def substitute_hand(hand):
    new_hand=get_frequency_dict(hand)
    choice=input("Would you like to substitute a letter ? Press Y for yes and N for no: ")
    if choice in "Yy":
        letter=input("Which letter would you like to replace ?")
        if letter in hand:
             times=new_hand[letter]
             new_letter=random.choice(alphabets)
             del(new_hand[letter])
             if new_letter in new_hand.keys():
                 new_hand[new_letter]+=times
             else:
                 new_hand[new_letter]=times
             return display_hand_without_space(new_hand)
        else:
             print("That letter is not in the hand.")
             return hand
    elif choice in "Nn":
        return hand
    else:
        print("Wrong choice..!")
        return hand


def play_hand(hand):
    total_score=0
    flag=0
    new_hand=hand
    substitute=0
    while len(new_hand)>0:
        print("Current Hand: "+display_hand(get_frequency_dict(new_hand)))
        if substitute==0:
            new_hand=substitute_hand(new_hand)
            hand=new_hand
            substitute+=1
            print("Current Hand: "+display_hand(get_frequency_dict(new_hand)))
        word_input=input("Enter word, or '!!' to indicate that you are finished: ")
        word_dict=get_frequency_dict(word_input)
        hand_dict=get_frequency_dict(new_hand)
        if word_input=="!!":
            print("Total score: "+str(total_score))
            break
        for key in word_dict.keys():
            if key not in hand_dict.keys():
                print("Your word is outside the scope of the hand. Please choose different word.")
                flag=1
                break
            if word_dict[key]>hand_dict[key]:
                print("Your word is outside the scope of the hand. Please choose different word.")
                flag=1
                break
        if flag==1:
            new_hand=display_hand_without_space(update_hand(new_hand,word_input))
            continue
        if word_input != "!!":
            if is_valid_word(word_input):
                print("'"+word_input+"' earned "+str(get_word_score(len(new_hand),word_input)))
                total_score+=get_word_score(len(new_hand), word_input)
                print("Total score: "+str(total_score))
            else:
                print("That is not a valid word. Please choose a different word.")
            new_hand=display_hand_without_space(update_hand(new_hand,word_input))
        if len(new_hand)==0:
            print("Ran out of letters")
            print("Total score: "+str(total_score))
            break
    print("--------------------------------------------------------------------------------")
    return hand,total_score

hand_size=random.randint(7,10)
word=deal_hand(hand_size)
(word,total_1)=play_hand(word)
choice=input("Do you want to replay the hand ? Press Y for yes and N for no : ")
if choice in "Yy":
    (word,total_2)=play_hand(word)
    print("Total score over all the hands: "+str(total_1+total_2))

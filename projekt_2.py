"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Ivo Srot
email: srot.ivo@gmail.com
discord: theivos_63282
"""

from random import randint
import os

# VYTVOR NAHODNE CISLO
def vytvor_nahodne_cislo():

    # VYTVARI PRVNI NAHODNE CISLO, KTERE NESMI BYT 0
    first_num = str(randint(1,9))
    
    # LIST PRO JIZ POUZITA CISLA
    pre_nums = []

    # VYTVARI POSLEDNI 3 CISLA, VYHAZUJE JIZ POUZITA, ABY VSECHNA BYLA UNIKATNI
    while len(pre_nums) != 3:
        a = randint(0,9)
        if str(a) in pre_nums or str(a) == first_num:
            continue
        else:
            pre_nums.append(str(a))
    
    # SESKUPUJE VSECHNA 4 CISLA DO JEDNOHO
    nums = "".join(pre_nums)
    number = first_num + nums

    # VRACI CISLO S UNIKATNIMI HODNOTAMI
    return number

# VSTUP UZIVATELE PRI HADANI SPRAVNEHO CISLA
def user_guess_input():
    while True:
        
        # POMOCNE LISTY PRO ROZHODOVANI SMYCEK 
        ok_nums = []
        notunique = []
        notdigit = []

        # UZIVATELSKY VSTUP
        print(oddelovac)
        guess = input("")
        
        # SMYCKA KONTROLUJICI JESTLI VSTUP OBSAHUJE POUZE CISLA
        for i in guess:
            if not i.isdigit():
                notdigit.append(i)


        # SMYCKA KONTROLUJICI JESTLI VSTUP OBSAHUJE UNIKATNI HODNOTY
        for i in guess:
            if i not in ok_nums:
                ok_nums.append(i)
            else:
                notunique.append(i)

        # VYPNUTI UZIVATELEM
        if guess.lower() == "q":
            print("Ok. Bye!")
            exit()

        # AKCE PRO TO, KDYZ VSTUP OBSAHUJE JINE ZNAKY NEZ CISLA
        elif len(notdigit) > 0:
            print("Number can be only numbers.\nTry again!")
        
        # AKCE PRO TO, KDYZ VSTUP ZACINA NULOU
        elif guess.startswith("0"):
            print("Number cannot start with 0.\nTry again!")
        
        # AKCE PRO TO, KDYZ VSTUP MA VICE CI MENE JAK 4 ZNAKY
        elif len(guess) != 4:
            print("Number has to have 4 digits.\nTry again!")
        
        # AKCE PRO TO, KDYZ VSTUP OBSAHUJE DUPLICITY
        elif len(notunique) > 0:
            print("All numbers has to be unique.\nTry again!")
        
        # AKCE POKUD JSOU VSECHNY PODMINKY V PORADKU
        else:
            break
    # VRACI ZKONTROLOVANY UZIVATELSKY VSTUP
    return guess

# HLAVNI HRA
def bulls_and_cows(a):
    
    # VYCHOZI HODNOTA POCTU HADANI
    guesses = 0


    while True:

        # ZVYSENI POCTU HADANI O JEDEN
        guesses +=1

        # PREVOD CISLA NA LIST PRO POUZITI INDEXOVANI
        list_number = list(a)
        
        # POCET BULLS AND COWS PRED KAZDYM TIPEM
        bulls = 0
        cows = 0

        # VYCHOZI HODNOTA INDEXU K POROVNAVANI
        index = -1

        # VYZADANI SI VSTUPU OD UZIVATELE
        guess = user_guess_input()

        # SMYCKA POCITAJICI BULLS AND COWS VE VSTUPU
        for i in guess:
            
            # NAVYSENI INDEXU O JEDNA ABY ODPOVIDAL POZICI ZKOUMANEHO CISLA VE VSTUPU
            index +=1
            
            # PODMINKY PRO POCITANI BULLS AND COWS VE VSTUPNI HODNOTE
            if i in a and i == list_number[index]:
                bulls += 1
            elif i in a:
                cows += 1

        # VITEZNA PODMINKA
        if bulls == 4:
            print("Correct, you've guessed the right number")
            print("in " + str(guesses) + " guesses!")
            print(oddelovac)
            print("That's amazing!")
            break
        
        # UPRAVA MNOZNEHO CISLA COW/COWS resp BULL/BULLS PRI VYPISOVANI VYSLEDKU
        textbulls = "bulls"
        textcows = "cows"

        if bulls == 1:
            textbulls = "bull"
        if cows == 1:
            textcows = "cow"

        # POCET BULLS AND COWS PO KAZDEM KOLE HADANI    
        print(str(bulls) + " " + textbulls + ", " + str(cows) + " " + textcows)

os.system('cls')

# VYTVOR NAHODNE CISLO
number = vytvor_nahodne_cislo()

# ODDELOVACI CARA
oddelovac = "-"*60

# UVODNI HLASKA
print("Hi there!")
print(oddelovac)
print("""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
print(oddelovac)
print("Guess the 4-digit number (or 'q' for quit):")

# SPUSTENI HRY
bulls_and_cows(number)


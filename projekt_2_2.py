"""
projekt_2_2.py: druhý druhý projekt do Engeto Online Python Akademie

author: Ivo Srot
email: srot.ivo@gmail.com
discord: theivos_63282
"""

import os

# ZACATEK HRY - DEFINUJE KDO BUDE ZACINAT
def game():
    os.system("cls")
    print("""
Welcome to Tic Tac Toe
============================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
============================================
Let's start the game
-------------------------------------------- 
""")
    input("Press any key to continue...")
    os.system("cls")
    player_1_turn()


# KONTROLA PO KAZDEM KOLE, MAME-LI JIZ VITEZE         
def game_check(a):

    # POCITA KOLIK SYMBOLU JIZ BYLO NAKRESLENO, ABYCHOM VEDELI KDY JSOU POLE ZAPLNENA
    rounds.append("round")

    # PODMINKY PRO VITEZSTVI S VITEZNOU HLASKOU
    if top_line_values[0] == a and top_line_values[1] == a and top_line_values[2] == a:
        show_table()
        print("Player",a,"wins!")
        exit()
    elif middle_line_values[0] == a and middle_line_values[1] == a and middle_line_values[2] == a:
        show_table()
        print("Player",a,"wins!")
        exit()
    elif bottom_line_values[0] == a and bottom_line_values[1] == a and bottom_line_values[2] == a:
        show_table()
        print("Player",a,"wins!")
        exit()
    elif top_line_values[0] == a and middle_line_values[0] == a and bottom_line_values[0] == a:
        show_table()
        print("Player",a,"wins!")
        exit()
    elif top_line_values[1] == a and middle_line_values[1] == a and bottom_line_values[1] == a:
        show_table()
        print("Player",a,"wins!")
        exit()
    elif top_line_values[2] == a and middle_line_values[2] == a and bottom_line_values[2] == a:
        show_table()
        print("Player",a,"wins!")
        exit()
    elif top_line_values[0] == a and middle_line_values[1] == a and bottom_line_values[2] == a:
        show_table()
        print("Player",a,"wins!")
        exit()
    elif top_line_values[2] == a and middle_line_values[1] == a and bottom_line_values[0] == a:
        show_table()
        print("Player",a,"wins!")
        exit()

    # PODMINKA PRO REMIZU - V PRIPADE, ZE JE NA POLI JIZ 9 ZNAKU A NIKDO SE MEZITIM NESTAL VITEZEM
    elif len(rounds) == 9:
        show_table()
        print("It's a DRAW!")
        exit()


# FUNKCE KTERA ZOBRAZUJE AKTUALNI DENI NA POLI
def show_table():

    # SMAZNI PREDCHOZI OBRAZOVKY PRO LEPSI PREHLED
    os.system("cls")

    # AKTUALNI HODNOTY NA JEDNOTLIVYCH POLICH
    top_line = "|",top_line_values[0],"|",top_line_values[1],"|",top_line_values[2],"|"
    middle_line = "|",middle_line_values[0],"|",middle_line_values[1],"|",middle_line_values[2],"|"
    bottom_line = "|",bottom_line_values[0],"|",bottom_line_values[1],"|",bottom_line_values[2],"|"

    # PROPOJENI POLI
    top_line = " ".join(top_line)
    middle_line = " ".join(middle_line)
    bottom_line = " ".join(bottom_line)

    # KONECNE VYKRESLENI AKTUALNI SITUACE NA POLI
    print("+---+---+---+")
    print(top_line)
    print("+---+---+---+")
    print(middle_line)
    print("+---+---+---+")
    print(bottom_line)
    print("+---+---+---+")


# UZIVATELSKY VSTUP PRO HRACE X
def player_1_input():

    # KONTROLA SPRAVNYCH HODNOT
    while True:
        choose = input("Choose a position (1-9):\n")
        if choose.isdigit() and choose != "0" and len(choose) == 1:
            break
        else:
            show_table()
            print("Wrong input.\nTry again!")
            print("")
            print("Player X:")
            
    return choose


# UZIVATELSKY VSTUP PRO HRACE O
def player_2_input():

    # KONTROLA SPRAVNYCH HODNOT
    while True:
        choose = input("Choose a position (1-9):\n")
        if choose.isdigit() and choose != "0" and len(choose) == 1:
            break
        else:
            show_table()
            print("Wrong input.\nTry again!")
            print("")
            print("Player O:")
            
    return choose


# AKCE V TAHU HRACE X
def player_1_turn():

    show_table()

    player_1_choose()


# AKCE V TAHU HRACE O
def player_2_turn():

    show_table()

    player_2_choose()

# KAM HRAC X UMISTI SVUJ SYMBOL
def player_1_choose():
    
    print("Player X:")
    choose = player_1_input()
   
    if choose == "1" and top_line_values[0] == " ":
        top_line_values[0] = "X"
    elif choose == "2" and top_line_values[1] == " ":
        top_line_values[1] = "X"
    elif choose == "3" and top_line_values[2] == " ":
        top_line_values[2] = "X"
    elif choose == "4" and middle_line_values[0] == " ":
        middle_line_values[0] = "X"
    elif choose == "5" and middle_line_values[1] == " ":
        middle_line_values[1] = "X"
    elif choose == "6" and middle_line_values[2] == " ":
        middle_line_values[2] = "X"
    elif choose == "7" and bottom_line_values[0] == " ":
        bottom_line_values[0] = "X"
    elif choose == "8" and bottom_line_values[1] == " ":
        bottom_line_values[1] = "X"
    elif choose == "9"and bottom_line_values[2] == " ":
        bottom_line_values[2] = "X"
    
    # OPAKOVANI AKCE V PRIPADE, ZE ZVOLENE POLE JE JIZ OBSAZENE
    else:
        show_table()
        print("The position is occupied already!\nTry again!")
        print("")
        player_1_choose()

    # KONTROLA MOZNE VYHRY
    game_check("X")

    # PREDANI HRY DRUHEMU HRACI
    player_2_turn()


# KAM HRAC O UMISTI SVUJ SYMBOL
def player_2_choose():

    print("Player O:")
    choose = player_2_input()
   
    if choose == "1" and top_line_values[0] == " ":
        top_line_values[0] = "O"
    elif choose == "2" and top_line_values[1] == " ":
        top_line_values[1] = "O"
    elif choose == "3" and top_line_values[2] == " ":
        top_line_values[2] = "O"
    elif choose == "4" and middle_line_values[0] == " ":
        middle_line_values[0] = "O"
    elif choose == "5" and middle_line_values[1] == " ":
        middle_line_values[1] = "O"
    elif choose == "6" and middle_line_values[2] == " ":
        middle_line_values[2] = "O"
    elif choose == "7" and bottom_line_values[0] == " ":
        bottom_line_values[0] = "O"
    elif choose == "8" and bottom_line_values[1] == " ":
        bottom_line_values[1] = "O"
    elif choose == "9"and bottom_line_values[2] == " ":
        bottom_line_values[2] = "O"
    
    # OPAKOVANI AKCE V PRIPADE, ZE POLE JE JIZ OBSAZENE
    else:
        show_table()
        print("The position is occupied already!\nTry again!")
        print("")
        player_2_choose()

    # KONTROLA MOZNE VYHRY
    game_check("O")

    # PREDANI HRY DRUHEMU HRACI
    player_1_turn()

# ZAKLADNI POCITADLO KOL/UMISTENYCH SYMBOLU
rounds = []

# VYCHOZI HODNOTY V POLICH
top_line_values = [" "," "," "]
middle_line_values = [" "," "," "]
bottom_line_values = [" "," "," "]


# ZAHAJENI HRY
game()
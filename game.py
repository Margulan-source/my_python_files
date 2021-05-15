import random

words = ["охраник", "кошка", "функция"]
ind = random.randint(0, 3)

def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    bboard = ["__"] * len(word)
    win = False
    print("Добро пожаловать на игру")

    while wrong < len(stages)-1:
        print("\n")
        msg = "Введите букву: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            bboard[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(bboard)))
        e = wrong + 1
        print("\n".join(stages[0:e]))

        if "__" not in bboard:
            print("Вы выиграли! Было загадано слово: ")
            print(" ".join(bboard))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("Вы проиграли! Было загадано слово: {}.".format(word))

hangman(words[ind])
    

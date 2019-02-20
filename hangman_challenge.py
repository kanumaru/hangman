import random
english_list = ["accept","append","argument","boolean","category","children",
                "compile","confirm","consumer","container","decimal","enable",
                "exception","force","function","infinity","info","notice"]
def hangman(word):
    wrong = 0
    stages = ["",
              "__________          ",
              "|                   ",
              "|         |         ",
              "|         O         ",
              "|        /|\        ",
              "|        / \        ",
              "|                   ",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ")
    while wrong < len(stages)-1:
        print("\n")
        char = input("一文字を予想してね")
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        print("\n".join(stages[:wrong+1]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("絵が完成してしまいました！あなたの負け！正解は" + word)
hangman(english_list[random.randint(0,17)])

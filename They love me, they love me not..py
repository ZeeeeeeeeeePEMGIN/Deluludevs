import time

lovemeter = 0
code = "0828"


def main_menu():
    print("They love me... They love me not.")
    time.sleep(1)
    print("===========================")
    print("A. Start\nB. Locker\nC. Credits and honorable mentions")
    print("===========================")
    time.sleep(1)
    choice = str(input("Where shall I take you? "))

    if choice == "A" or choice == "a":
        main()
    elif choice == "B" or choice == "b":
        next_move = None
        while next_move != "yes" or next_move != "Yes":
            codeguess = input("Enter the 4 number code. ")
            if codeguess == code:
                locker()
            else:
                print("Incorrect. Return to menu?")
                time.sleep(1)
                next_move = input("Yes\tor\tNo\n")
                if next_move == "Yes" or next_move == "yes":
                    main_menu()
    elif choice == "Take me to where they promised.":
        secretwed()
    elif choice == "C" or choice == "c":
        creds()
        time.sleep(2)
        main_menu()
    else:
        print("That path does not exist.")
        main_menu()


def scenario1():
    global lovemeter
    print(
        "As you pass by their classroom on the way to your own, your eyes wandered to their figure, sitting down on their seat as usual. They notice you, and you lock eyes...\nA. Wave enthusiastically and give them a soft smile. \nB. Stare at them for a full 5 seconds and wave awkwardly.\nC. Turn away immediately and walk off.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 2
    else:
        lovemeter = lovemeter - 1


def scenario2():
    global lovemeter
    print(
        "\nIt's finally break, and you decide not to leave your classroom. You pull out your phone and your eyes catches the green dot on their profile. They're active! Your heart skips a beat. \nA. Archive them so your heart can rest.\nB. Send them a like emoji without further explanation.\nC. Greet them with a simple 'good morning'.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter - 1
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 2
    else:
        lovemeter = lovemeter + 4


def scenario3():
    global lovemeter
    print(
        "Lunch has finally arrived and you go down to the canteen, wanting to buy your food. You spot them---surprisingly---alone at a table and without food.\nA. You walk up to them, and ask them 'Do you want to eat lunch together?'\nB. You awkwardly walk up to them, but your brain freezes and you end up not saying ANYTHING and walk off, regretting your life decisions.\nC. You quietly leave their favorite food on their table.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter - 1
    else:
        lovemeter = lovemeter + 2


def scenario4():
    global lovemeter
    global charname
    global username
    print(
        f"It's finally dismissal and you get to go home! But before you could exit through the gate, a tap on your shoulder. It was {charname}! \"Hey, {username}, wanna maybe... walk together? I've been a bit lonely lately.\"\nA. You nod awkwardly, a sheepish smile on your face.\nB. You accept without hesitation, a bright smile on your face as you walk alongside them.\nC. Stare at them for a full minute before accepting.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    else:
        lovemeter = lovemeter - 1


def scenario5():
    global lovemeter
    global charname
    print(
        f"Walking beside {charname}, you can't help the fast beating of your heart against your chest. But... the silence was getting a bit awkward.\nA. You decide to begin a conversation, but while they speak, you act rather indifferent.\nB. You begin a conversation, asking about their day and telling jokes, ultimately painting a bright smile on their face.\nC. You begin a conversation, though while telling a joke, you stumble over your words and elicit a soft laugh from {charname}.")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter - 3
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 6
    else:
        lovemeter = lovemeter + 4


def scenario6():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter - 1
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 2
    else:
        lovemeter = lovemeter + 4


def scenario7():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    else:
        lovemeter = lovemeter - 1


def scenario8():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter - 1
    else:
        lovemeter = lovemeter + 2


def scenario9():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter - 1
    else:
        lovemeter = lovemeter + 2


def scenario10():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 6
    else:
        lovemeter = lovemeter - 3


def scenario11():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    else:
        lovemeter = lovemeter - 1


def scenario12():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    else:
        lovemeter = lovemeter - 1


def scenario13():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter - 1
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 2
    else:
        lovemeter = lovemeter + 4


def scenario14():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter - 1
    else:
        lovemeter = lovemeter + 2


def scenario15():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 6
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter - 3
    else:
        lovemeter = lovemeter + 4


def scenario16():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter - 1
    else:
        lovemeter = lovemeter + 2


def scenario17():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter - 1
    else:
        lovemeter = lovemeter + 4


def scenario18():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    else:
        lovemeter = lovemeter - 1


def scenario19():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 2
    else:
        lovemeter = lovemeter - 1


def scenario20():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter - 3
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    else:
        lovemeter = lovemeter + 6


def scenario21():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter - 1
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    else:
        lovemeter = lovemeter + 2


def scenario22():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter - 1
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    else:
        lovemeter = lovemeter + 2


def scenario23():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    else:
        lovemeter = lovemeter - 1


def scenario24():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter - 1
    else:
        lovemeter = lovemeter + 4


def scenario25():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 6
    else:
        lovemeter = lovemeter - 3


def scenario26():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter - 1
    else:
        lovemeter = lovemeter + 2


def scenario27():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter - 1
    else:
        lovemeter = lovemeter + 4


def scenario28():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 2
    else:
        lovemeter = lovemeter - 1


def scenario29():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    else:
        lovemeter = lovemeter - 1


def scenario30():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 6
    else:
        lovemeter = lovemeter - 3


def scenario31():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 2
    else:
        lovemeter = lovemeter - 1


def scenario32():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter - 1
    else:
        lovemeter = lovemeter + 4


def scenario33():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 2
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    else:
        lovemeter = lovemeter - 1


def scenario34():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter - 1
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 4
    else:
        lovemeter = lovemeter + 2


def scenario35():
    global lovemeter
    print("#scenario\n#choiceA\n#choiceB\n#choiceC")
    time.sleep(1)
    choice = str(input("What do you do? "))

    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter - 3
    else:
        lovemeter = lovemeter + 6


def final():
    global lovemeter
    print("End scene")

    choice = input("What do you get them? ")
    if choice == "A" or choice == "a":
        lovemeter = lovemeter + 4
    elif choice == "B" or choice == "b":
        lovemeter = lovemeter + 2
    else:
        lovemeter = lovemeter + 6

    if lovemeter < 5:
        print("harsh rejection")
        end1 = "Heartbroken"
        time.sleep(4)
        print(f"{end1} end.")
        print("===========================")

    elif lovemeter <= 25:
        print("blunt rejection")
        end2 = "At least I tried"
        time.sleep(4)
        print(f"{end2} end.")
        print("===========================")

    elif lovemeter <= 50:
        print("polite rejection")
        end3 = "Friends"
        time.sleep(4)
        print(f"{end3} end.")
        print("===========================")

    elif lovemeter <= 75:
        print("promise of a future")
        end4 = "Hopeful"
        time.sleep(4)
        print(f"{end4} end.")
        print("===========================")

    elif lovemeter <= 100:
        print("reciprocation")
        end5 = "Happy"
        time.sleep(4)
        print(f"{end5} end.")
        print("===========================")
    else:
        yansecret()


def yansecret():
    print("secret scene\nchoiceA\nchoiceB")
    time.sleep(4)
    choice = str(input("What is your choice? . . . "))

    if choice == "A" or choice == "a":
        print("Obsession scene")
        end6 = "Happy...?"
        time.sleep(4)
        print(f"{end6} end.")
        print("===========================")

    else:
        print("breakup scene")
        end7 = "Won't work out anymore"
        time.sleep(4)
        print(f"{end7} end.")
        print("===========================")


def secretwed():
    print("wedscene KWBDFBWDFBEWJFDFBDSUBDS")
    time.sleep(5)
    main_menu()


def locker():
    choice = input("Go through their locker?\nYes\tor\tNo\n")
    if choice == "yes" or choice == "Yes":
        print("You found: Phone!")
        print("You found their phone. Weirdly enough, you knew their password.")
        second_choice = input("Go through it?\nYes\tor\tNo\n")
        if second_choice == "yes" or second_choice == "Yes":
            print(
                "You look through a couple selfies, their recent searches, then you entered a notes app.\nWait-- Creator's note??? You open it and see:\n\n===========================\nCreator's note\n\nTell EVEREST to take you to where they promised.\n(hint: EVEREST is the one who asks you what you want to do next.\n===========================")
            print("Um...")
            time.sleep(1)
            print(
                "\"Strange,\" you thought. You then heard the bell. \"I should go now...\"\nShutting the locker, you made your way to class.\n")
            time.sleep(2)
        else:
            print(
                "\"I've already gone through their locker... their phone is a bit of a stretch,\" you told yourself. You put their phone back down and shut the locker.\n")
            time.sleep(2)
    else:
        print("\"This is an invasion of their privacy,\" you thought to yourself. You decide to leave.\n")
        time.sleep(2)
    main_menu()


def creds():
    print("===========================")
    print(
        "They love me... They love me not.\nMade by --- The deluludevs\nDeveloper --- Zeryl Gonadan, Krisha Villa, Lordwyn Demoni\nMain coder --- Zeryl Gonadan\nSecondary coder --- Lordwyn Demoni, Krisha Villa\nStorywriter --- Lordwyn Demoni, Zeryl Gonadan, Krisha Villa\n'SHOUTOUT TO MY (Zeryl) ONE AND ONLY INSPIRATION!!!!!'")
    print("===========================")
    time.sleep(2)


def main():
    global charname
    global username
    time.sleep(1)
    username = input("What shall we call you? ")
    charname = input("What shall 'their' name be? ")
    if charname == "Zeryl" or charname == "zeryl":
        print("Unless ur a certain camia, she wants nothing to do with u /lh")
    elif charname == "Krisha" or charname == "krisha":
        print("Unless ur a fictional character, u better GET OUUUUU--")
    elif charname == "Lordwyn" or charname == "lordwyn":
        print("You must be one shady guy...")
    input(
        "MINOR WARNING!!!\nThis character has their own fixed persona---If you attempt this with your special someone, it's not guaranteed they'll like you back (ehe)")

    print(
        f"\nAugust 21, 20xx. One more week until you finally confess.\n\nIt's been a whole year ever since you first laid your eyes on them...\nYou had enough of watching from afar.. This week.. It's going to be different..!\nYou...\nWill make the first move...")
    time.sleep(4)

    print("===========================")
    print("☆｡⁠⁠✧.* ~ Day 1 ~ *⁠.⁠✧｡⁠☆ ")
    time.sleep(1)
    scenario1()
    time.sleep(1)
    scenario2()
    time.sleep(1)
    scenario3()
    time.sleep(1)
    scenario4()
    time.sleep(1)
    scenario5()
    time.sleep(1)
    print("DAY END.")
    print("===========================")

    print("===========================")
    print("☆｡⁠⁠✧.* ~ Day 2 ~ *⁠.⁠✧｡⁠☆ ")
    time.sleep(1)
    scenario6()
    time.sleep(1)
    scenario7()
    time.sleep(1)
    scenario8()
    time.sleep(1)
    scenario9()
    time.sleep(1)
    scenario10()
    time.sleep(1)
    print("DAY END.")
    print("===========================")

    print("===========================")
    print("☆｡⁠⁠✧.* ~ Day 3 ~ *⁠.⁠✧｡⁠☆ ")
    time.sleep(1)
    scenario11()
    time.sleep(1)
    scenario12()
    time.sleep(1)
    scenario13()
    time.sleep(1)
    scenario14()
    time.sleep(1)
    scenario15()
    time.sleep(1)
    print("DAY END.")
    print("===========================")

    print("===========================")
    print("☆｡⁠⁠✧.* ~Day 4 ~ *⁠.⁠✧｡⁠☆ ")
    time.sleep(1)
    scenario16()
    time.sleep(1)
    scenario17()
    time.sleep(1)
    scenario18()
    time.sleep(1)
    scenario19()
    time.sleep(1)
    scenario20()
    time.sleep(1)
    print("DAY END.")
    print("===========================")

    print("===========================")
    print("☆｡⁠⁠✧.* ~ Day 5 ~ *⁠.⁠✧｡⁠☆")
    time.sleep(1)
    scenario21()
    time.sleep(1)
    scenario22()
    time.sleep(1)
    scenario23()
    time.sleep(1)
    scenario24()
    time.sleep(1)
    scenario25()
    time.sleep(1)
    print("DAY END.")
    print("===========================")

    print("===========================")
    print("☆｡⁠⁠✧.* ~ Day 6 ~ *⁠.⁠✧｡⁠☆")
    time.sleep(1)
    scenario26()
    time.sleep(1)
    scenario27()
    time.sleep(1)
    time.sleep(1)
    scenario28()
    time.sleep(1)
    scenario29()
    time.sleep(1)
    scenario30()
    time.sleep(1)
    print("DAY END.")
    print("===========================")

    print("===========================")
    print("☆｡⁠⁠✧.* ~ Day 7 ~ *⁠.⁠✧｡⁠☆")
    time.sleep(1)
    scenario31()
    time.sleep(1)
    scenario32()
    time.sleep(1)
    scenario33()
    time.sleep(1)
    scenario34()
    time.sleep(1)
    scenario35()
    time.sleep(1)
    print("DAY END.")
    print("===========================")

    print("===========================")
    print("Day of confession.")
    time.sleep(1)
    final()
    time.sleep(4)
    creds()
    print("===========================")
    ans = str(input("\t\tRetry?\t\t\nYes\tor\tNo\n  "))
    print("===========================")

    if ans == "Yes":
        main()
    else:
        main_menu()


main_menu()
#deluludevs so real
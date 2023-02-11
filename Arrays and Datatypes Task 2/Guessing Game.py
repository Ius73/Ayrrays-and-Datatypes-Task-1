import json
import random
from copy import deepcopy


def read_name():  # this function prints all players name
    with open("records.json", "r") as records:  # open the file as records
        data = json.load(records)  # turn the file in a dictionary/json format named data
        for item in data:  # for each item in data
            print(item["name"])  # print the item at the "name" key


def read_record(record, size):  # this function reads 10 items form record
    while True:
        n = 0  # reset n, n counts the items printed
        for i in record:  # for each item in data
            print(i["name"], end=":\t")  # print the item at the "name" key, ending with tab
            print(i["score"],"€")  # print the item at the "score" key
            n = n + 1  # add 1 to n
            if n == 10 or n == size:  # if n is 10 or n is equal to the size
                break  # stop the for loop
        if n == 10 or n == size:  # if n is 10 or n is equal to the size
            break  # stop the while loop


def update_record(player, score):  # this function updated the json file
    entry = {"name": f"{player}", "score": score}  # format the entry in json/dictionary format
    with open("records.json", "r") as record:  # open the file as records
        data = json.load(record)  # turn the file in a dictionary/json format named data
    size = len(data)  # get the size of data
    index = 0  # reset index
    ver = True  # ver verifies if the player is new
    while index < size:  # loop until the last element, this is a linear searching algorithm
        if data[index]["name"] == player:  # if the name at the index is the player name
            data[index]["score"] = score  # change the score related to the name (in the same index)
            ver = False  # set ver to false, the player not new
            break  # stop
        index += 1  # go to the next index
    if ver is True:  # if the player is new
        data.append(entry)  # add the new player and score to the dictionary
    with open("records.json", "w") as record:  # open the file as records
        json.dump(data, record, indent=4)  # write the data to the json file


def league():  # this function sorts the players in ascending order
    with open("records.json", "r") as record:  # format the entry in json/dictionary format
        data = json.load(record)  # turn the file in a dictionary/json format named data
    sorted_record = deepcopy(data)  # make a copy of the file to use it later
    size = len(data)  # get the size of the file
    if size == 0:  # if there are no players
        print("there are no players")
        menu()  # go to menu
    else:  # if there are players
        print("These are the top players")
    while True:  # this is a bubble sorting algorithm
        v = 0  # this v verifies if an element is sorted
        n = 0  # this n is the current index
        i = n + 1  # this i is the element next to the index
        while i < size:  # this loop repeats until the next index is the last
            if sorted_record[n]["score"] < sorted_record[i]["score"]:  # if the first element is less than the next
                # start the swap process:
                temp_s = sorted_record[n]["score"]
                # store the score of the current element to a temporary score variable
                temp_n = sorted_record[n]["name"]
                # store the name of the current element to a temporary name variable
                sorted_record[n]["score"] = sorted_record[i]["score"]
                # assign the score of the current element to the firs element
                sorted_record[n]["name"] = sorted_record[i]["name"]
                # assign the name of the next element to the first element
                sorted_record[i]["score"] = temp_s
                # assign the temporary score to the next element
                sorted_record[i]["name"] = temp_n
                # assign the temporary name to the next element
            else:  # if the first element is more or equal to  than the next
                v = v + 1  # add 1 to the sorted element counter
            n = n + 1  # pass to the next pair
            i = n + 1  # pass to the next pair
        if v >= size - 1:  # if every element is sorted
            break  # stop
    read_record(sorted_record, size)  # print the sorted dictionary/json file


def new_game(player):  # this function start the game
    print("Answerer 10 questions to win 1,000,000€ ")
    print("You have 3 attempts per question")
    description = transfer_1()  # description pool, the list with all the descriptions that can be selected
    name = transfer_2()  # name pool, the list with all name that can be selected associated with the description
    n = 0  # this n counts the answered questions
    ver = False  # ver verifies if the player won
    score = 1000  # this is the initial score
    while n < 10:  # loop until the question are 10
        ver = False  # reset ver
        size = len(description)  # get the size of the list of description that is the same size as the name list
        rand = random.randint(0, size - 1)  # rand generates a random number between 0 and the last element
        selected_1 = description[rand]  # select the description using rand
        selected_2 = name[rand]  # select the name associated with the description (same index(rand))
        t = 3  # reset t, this variable count the attempts
        while t > 0:  # loop until the attempts are 3
            print(selected_1)  # print the description of the selected item
            user_input = str(input("this is: "))  # get the user_input
            user_input = user_input.lower()  # transform the user_input is lower cases
            if user_input == selected_2:  # if guess is correct
                score = score * 2  # double the score
                print(f"Correct! Your score is {score}€")  # print the score
                ver = True  # set the win condition to true
                break  # stop
            else:  # if the guess is wrong
                print(f"you answer is wrong, you hve {t - 1} attempts left")
            t = t - 1  # subtract 1 to the attempts
        description.remove(selected_1)  # remove the description from the pool
        name.remove(selected_2)  # remove the name from the pool
        if ver is False:  # if the win condition is false
            print(f"the correct answer was {selected_2}")  # print the correct answerer
            print(f"you lost, your score is {score}€")  # print the score
            update_record(player, score)  # update the file with the score and name
            menu()  # go tp menu
        n = n + 1  # add 1 to the answered questions
    if ver is True:  # if the win condition is true
        print(f"Congratulations! You won {score}€")  # print the score
        update_record(player, score)  # update the file with the score and name
        menu()  # go to menu


def transfer_1():  # this function turn json file content int a list
    with open("items.json", "r") as items:  # open the file as records
        data = json.load(items)  # turn the file in a dictionary/json format named data
    item = deepcopy(data)  # make a copy of the file to use it later
    item_r = []  # create a list
    index = 0  # reset index
    while index < 24:  # loop until the end of the file
        item_r.append(item[index]["description"])  # add description to the list
        index += 1  # go tho the next index
    return item_r  # return the list


def transfer_2():  # this function turn json file content int a list
    with open("items.json", "r") as items:  # open the file as records
        data = json.load(items)  # turn the file in a dictionary/json format named data
    item = deepcopy(data)  # make a copy of the file to use it later
    item_n = []  # create a list
    index = 0  # reset index
    while index < 24:  # loop until the end of the file
        item_n.append(item[index]["name"])  # add name to the list
        index += 1  # go tho the next index
    return item_n  # return the list


def load_player():  # this function selects from existing players
    with open("records.json", "r") as record:  # open the file as records
        data = json.load(record)  # turn the file in a dictionary/json format named data
    if len(data) == 0:  # if data is empty
        print("there are no games saved")
        menu()  # go to menu
    else:  # if data is not empty
        read_name()  # read player names
        user_input = str(input("type your name to select your save: "))  # get user input
        v = False  # v means that the player exist
        for i in data:
            if user_input == i["name"]:  # if the name exists
                print("your save is :")
                print(i["name"], end=":\t")  # print name
                print(i["score"],"€")  # print score
                v = True  # the player exists
                break  # stop
            else:  # if the name doesn't exist
                v = False  # the player doesn't exist
        if v:  # if the player exists
            new_game(user_input)  # start the game
        if not v:  # if the player doesn't exist
            while True:  # ask the player if it wants to re-input the name
                print("the is no player with such name")
                user_input = str(input("do you want to try again? y/n: "))  # get user input
                if user_input == "y" or user_input == "Y":  # if the player said yes
                    load_player()  # restart the function
                    break  # stop the loop
                elif user_input == "n" or user_input == "N":  # if the player said no
                    menu()  # go to menu
                    break  # stop the loop
                else:  # it the player makes an error
                    print("error, type y or n")  # repeat the loop


def print_menu():  # this function print the menu
    print("(1)Top Players")
    print("(2)New Game")
    print("(3)Load Game")
    print("(4)Exit")


def menu():  # this function is the menu
    while True:
        print_menu()  # print menu
        user_input = str(input("select an menu item: "))  # get user input
        if user_input == 1 or user_input == "1":  # if user chooses top players
            league()  # print top players
        elif user_input == 2 or user_input == "2":  # if user chooses new game
            player = str(input("insert new player: "))  # get player name
            if (len(player)) < 3:  # if the name is short
                player = player + "  "  # add 2 paces to the name
            print(f"your name is {player}")  # print the player
            new_game(player)  # start the game
        elif user_input == 3 or user_input == "3":  # if user chooses existing player
            load_player()  # load existing player
            break  # stop the loop
        elif user_input == 4 or user_input == "4":  # if user chooses exit
            return 0  # exit the program
        else:  # if player inputs something else
            print("error, select using a number from 1 to 4")  # print error
            menu()  # go to menu


menu()  # go to menu

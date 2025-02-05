import math

word = input("input word: ")
letter = input("input letter: ")

def remove_all_from_string(word, letter):
    while letter in word:
        word = word[:word.find(letter)] + "" + word[word.find(letter) + 1:]
    return word

#################################################################################

word = input("input word: ")
letter = input("input letter: ")

def remove_all_from_string(word, letter):
    while letter in word:
        for i in range(len(letter)):
            word = word[:word.find(letter[i])] + "" + word[word.find(letter[i]) + 1:]
    

    print(len(letter))
    return word

print(remove_all_from_string(word, letter))

#################################################################################

def distance(first_point, second_point): # d = sqrt((x2-x1)^2 + (y2-y1)^2), finds distance between points
    distance = math.sqrt(pow((first_point[0] - second_point[0]), 2) + pow((second_point[1] - first_point[1]), 2))
    return distance

#################################################################################

def max_int_in_list(my_list): # finds the highest integer in a list
    for i in range(len(my_list)):
        try:
            if my_list[i] > my_list[i + 1]:
                print(i, ">")
                greatest_num = my_list[i]
            elif my_list[i] < my_list[i + 1]:
                print(i, "<")
                greatest_num = my_list[i + 1]
            elif my_list[i] == my_list[i + 1]:
                print(i, "=")
                greatest_num = my_list[i]
        except IndexError:
                if my_list[i] > my_list[0]:
                    print(i, ">")
                    greatest_num = my_list[i]
                elif my_list[i] < my_list[0]:
                    print(i, "<")
                    greatest_num = my_list[0]
                elif my_list[i] == my_list[0]:
                    print(i, "=")
                    greatest_num = my_list[i]
    return greatest_num

#################################################################################

def owl_count(text): # finds words in strings
    count = 0
    text = text.lower()
    for word in text.split():
        if "owl" in word: # put word to find in text in the quotes
            count += 1
    return count

#################################################################################

#  list/string/tuple[::2]
#            [start, end, increment]

#################################################################################

def word_ladder():
    word = input("Enter a word: ")

    while True:
        try:
            get_index = int(input("Enter an index (-1 to quit): "))
        except ValueError:
            print("Invalid index")
            get_index = int(input("Enter an index (-1 to quit): "))

        if get_index == -1:
            break
        while True:
            if get_index > len(word) - 1:
                print("Invalid index")
                get_index = int(input("Enter an index (-1 to quit): "))
            elif get_index < -1:
                print("Invalid index")
                get_index = int(input("Enter an index (-1 to quit): "))
            elif get_index < len(word):
                break


        get_letter = input("Enter a letter: ")
        while True:
            if get_letter == get_letter.upper():
                print("Character must be a lowercase letter!")
                get_letter = input("Enter a letter: ")
            elif len(get_letter) > 1:
                print("Must be exactly one character!")
                get_letter = input("Enter a letter: ")
            elif get_letter == get_letter.lower():
                break
            else:
                print("Invalid letter")
        
        word = word[:get_index] + get_letter + word[get_index + 1:]
        print(word)

#################################################################################
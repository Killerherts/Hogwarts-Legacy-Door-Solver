def subtract_numbers_to_word():
    word_list = {
        "Demiguise": 0,
        "Unicorn": 1,
        "Dragon": 2,
        "Hydra": 3,
        "Owl": 4,
        "Quintaped": 5,
        "Salamander": 6,
        "Octapus": 7,
        "Spider": 8,
        "Snakes": 9
    }
    abbreviations = {word[:2]: word for word in word_list}
    print ("Here is all the picture names: " + str(word_list) + "you can also use only the first 2 letters to referance a word")
    while True:
        first_input = input("Enter the first number or word (0-9) or 'q' to quit: ")

        if first_input == 'q':
            break

        if first_input in word_list or first_input in abbreviations or first_input.isdigit():
            first_num = word_list[first_input] if first_input in word_list else word_list[abbreviations[first_input]] if first_input in abbreviations else int(first_input)
        else:
            print("Invalid input. Please enter a valid number or word from the list.")
            continue

        second_input = input("Enter the second number or word (0-9) or 'q' to quit: ")

        if second_input == 'q':
            break

        if second_input in word_list or second_input in abbreviations or second_input.isdigit():
            second_num = word_list[second_input] if second_input in word_list else word_list[abbreviations[second_input]] if second_input in abbreviations else int(second_input)
        else:
            print("Invalid input. Please enter a valid number or word from the list.")
            continue

        third_input = input("Enter the third number or word (0-9) or 'q' to quit: ")

        if third_input == 'q':
            break

        if third_input in word_list or third_input in abbreviations or third_input.isdigit():
            third_num = word_list[third_input] if third_input in word_list else word_list[abbreviations[third_input]] if third_input in abbreviations else int(third_input)
        else:
            print("Invalid input. Please enter a valid number or word from the list.")
            continue

        result = third_num - first_num - second_num
        result_word = [word for word, num in word_list.items() if num == result][0]

        print(f"Result: {result_word}")

if __name__ == '__main__':
    subtract_numbers_to_word()

def subtract_numbers_to_word():
    first_num = int(input("Enter the first number (0-9): "))
    second_num = int(input("Enter the second number (0-9): "))
    third_num = int(input("Enter the third number: "))
    result = third_num - first_num - second_num

    word_list = ["Owl", "Unicorn", "Horned Beast", "Three-headed Serpent", 
                 "Second Owl", "Four-legged Beast", "Salamander", 
                 "Tentacled-Beast", "Spider", "Multi-Headed Serpent Beast"]
    
    if result >= 0 and result <= 9:
        result_word = word_list[result]
        print("The result in words is:", result_word)
    else:
        print("The result is out of range.")

subtract_numbers_to_word()

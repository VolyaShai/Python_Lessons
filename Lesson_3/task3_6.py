def int_func():
    user_list = input("Введите предложение маленькими латинскими буквами: ").split()
    latin_alphabet = "q w e r t y u i o p a s d f g h j k l z x c v b n m "
    for word in user_list:
        if not set(word).difference(latin_alphabet.split()) and word.islower():
            print(word.title())
    else:
        print("Ошибка! Введите предложение маленькими латинскими буквами!!!")


int_func()

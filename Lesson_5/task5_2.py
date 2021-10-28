with open("text_2.txt") as some_strings:
    some_list = some_strings.readlines()
    print(f"В документе {len(some_list)} строк")
    for one_string in some_list:
        print(f"В строке: {one_string} {len(one_string.split())} слов")

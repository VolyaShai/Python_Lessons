translate_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("text_4_1.txt", "w", encoding="utf-8") as list_new:
    with open("text_4.txt", encoding="utf-8") as list_eng:
        for line in list_eng:
            list_new.writelines(line.replace(line.split()[0], translate_dict.get(line.split()[0])))
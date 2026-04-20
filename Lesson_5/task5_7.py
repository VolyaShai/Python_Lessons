import json

with open("text_777.json", "w", encoding="utf-8") as text777:
    with open("text_7.txt", encoding="utf-8") as text:
        dict_profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in text}
        profit = sum([el for el in dict_profit.values() if el > 0]) / \
                 len([el for el in dict_profit.values() if el > 0])
        all_list = [dict_profit, {"average_profit": profit}]
        print(all_list)

    json.dump(all_list, text777, ensure_ascii=False, indent=4)

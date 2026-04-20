dict_lessons = {}
numbers = " 0123456789"
with open("text_6.txt", encoding="utf-8") as lessons:
    for line in lessons:
        name, other = line.split(":")
        line_numb = sum(map(int, "".join([i for i in other if i in numbers]).split()))
        dict_lessons[name] = line_numb
print(dict_lessons)

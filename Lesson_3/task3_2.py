"""Вывод данных о пользователе в столбик для красоты"""
#
# def user_data(**kwargs):
#     for data, us_data in kwargs.items():
#         print(f"{data}: {us_data}")
#
#
# user_data(Firstname="Volya", Lastname="Shaikova", Age="24", City="Orsha",
#           Email="I don't know", Phone="I don't know too")
"""Вывод уже имеющихся данных"""


# def user_data(**kwargs):
#     return kwargs
#
#
# print(user_data(Firstname="Volya", Lastname="Shaikova", Age="24", City="Orsha",
#                 Email="I don't know", Phone="I don't know too"))


def user_data(**kwargs):
    # return kwargs
    # Для возвращения данных просто с ключами
    return ' '.join(kwargs.values())


print(user_data(Firstname=input("Enter your firstname: "), Lastname=input("Enter the your lastname: "),
                Age=input("Enter your age: "), City=input("Enter your city: "),
                Email=input("Enter your email: "), Phone=input("Enter your phone number: ")))

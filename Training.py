answer = input("Вы хотите добавить товар? Да/Нет: ")
yes = "Да"
no = "Нет"
i = 0
product_list = {"Название": "", "Цена": "", "Количество": "", "Ед": ""}
analytics = {"Название": [], "Цена": [], "Количество": [], "Ед": []}
goods = []
while answer == yes:
    i += 1
    prod_copy = product_list.copy()
    for prod in product_list:
    input(f"Введите свойство {prod}: ")
    analytics[prod].append(prod_copy[prod])
    goods.append(i, prod_copy)
    print("Товары:", goods)
    print("Аналитика товаров: ", )
    all_pro_list = {product_list.keys():[product_list.values()]}
    print(all_pro_list)
    answer = input("Вы хотите добавить еще товар? Да/Нет: ")
    if answer == no:
        break

def create_cook_book():
    cook_book = {}
    with open("recipes.txt", "r", encoding="utf-8") as f:
        recipes = f.read().split('\n')
        for line in recipes:
            if "|" not in line and not line.isdigit() and line != '':
                cook_book[line] = []
                current_dish = line
            if "|" in line:
                ingredient_attributes = line.split("|")
                cook_book[current_dish].append({"ingredient_name": f"{ingredient_attributes[0].strip()}",
                                           "quantity": f"{ingredient_attributes[1].strip()}",
                                           "measure": f"{ingredient_attributes[2].strip()}"})
    return cook_book


def get_shop_list_by_dishes(dishes:list, person_count:int):
    cook_book = create_cook_book()
    shop_list = {}
    for dish in dishes:
        if dish not in cook_book:
            print(f"Блюда {dish} нет в книге рецептов.")
            dishes.remove(dish)
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient["ingredient_name"] in list(shop_list.keys()):
                for_another_dishes = shop_list[ingredient["ingredient_name"]]["quantity"]
                need_to_add = int(ingredient["quantity"]) * person_count
                shop_list[ingredient["ingredient_name"]].update({"quantity": for_another_dishes + need_to_add})
            else:
                shop_list[ingredient["ingredient_name"]] = {"measure": f"{ingredient['measure']}",
                                                            "quantity": int(ingredient["quantity"]) * person_count}
    return shop_list


def print_shop_list(shop_list):
    print("Список покупок:")
    for ingredient in shop_list:
        print(f"{ingredient} - {shop_list[ingredient]['quantity']} {shop_list[ingredient]['measure']}")


shop_list = get_shop_list_by_dishes(["Омлет", "Запеканка"], 3)
print_shop_list(shop_list)
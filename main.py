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

        for dish in cook_book:
            print(dish)
            for ingredients in cook_book[dish]:
                print(ingredients)

create_cook_book()
print('~' * 50 )

f_name = f"{'~' * 50}"
print(f_name)


dish_name = input("Введіть назву страви, рецепт якої вам подобається: ").strip()
recept = input("Введіть рецепт страви: ").strip()


f_dish_name = f"{'*' * 10}{dish_name}{'*' * 10}"
print(f_dish_name)


cleaned_recept = recept.lower().strip().title()
print(cleaned_recept + " 👍 ")


meat_count = recept.lower().count("мясо")
print(f"Кількість слів 'мясо' в рецепті: {meat_count}")

print(f_name)

from constants_01 import MSG_INPUT_LAST_NAME, MSG_INPUT_FIRST_NAME

user_first_name = input(MSG_INPUT_FIRST_NAME).title().strip()
# user_first_name = user_first_name.title()
# user_first_name = user_first_name.strip()
user_last_name = input(MSG_INPUT_LAST_NAME).title().strip()


# welcome_text = 'Вiтаю тебе, '
# mark = '!'
# result = welcome_text + user_first_name + ' ' + user_last_name + mark

template = 'Вiтаю тебе, {first_name} {last_name}!'
result = template.format(first_name=user_first_name, last_name=user_last_name)


print(result)

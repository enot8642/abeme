peoples = 4

ticket_price = 500

taxi_cost = 600

extra_taxi_cost_percentage = 20

pizza_cost = 250 * 2

pizza_discount = 15 / 100

air_hockey_cost = 80 * 8

total_cost = (ticket_price + (taxi_cost + taxi_cost * extra_taxi_cost_percentage / 100) + pizza_cost - pizza_cost * pizza_discount + air_hockey_cost)

each_person_cost = total_cost / peoples

print("Кожен з вас повинен сплатити:", each_person_cost, "гривень")

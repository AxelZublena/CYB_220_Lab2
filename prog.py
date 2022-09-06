# This is a program to store new vehicle inventory and assist with monthly payments


# Create variable of your favorite car brand
brand = "mazda"


# Create list of 5 of their models from cheapest to most expensive
cars = ["Mazda3 Sedan", "CX-30", "Mazda3 Hatchback", "CX-5", "CX-50"]


# Append a 6th model to the list
cars.append("MX-5 Miata")


# Create list of 5 standard colors for all models
colors = ["Blue", "Red", "Green", "Yellow", "Gray"]


# Replace your last color with a different color
colors[-1] = "Purple"


# Create variable of the current new year models
new_year_models = ["CX-30", "CX-5", "CX-50", "CX-9", "Mazda3 Sedan", "Mazda3 Hatchback", "MX-5 Miata", "MX-5 Miata RF"]


# Create MSRP constant number (not string) of each of the models
MSRPS = [22500, 26700, 27550, 38750, 21150, 23550, 27650, 35350]


# Create a constant number (not string) for total months in 4yr, 5yr, and 6yr loans
MONTH_IN_A_YEAR = 12
LOAN4 = 4 * MONTH_IN_A_YEAR
LOAN5 = 5 * MONTH_IN_A_YEAR
LOAN6 = 6 * MONTH_IN_A_YEAR


# Create a variable for the guest's name. Be courteous in your upcoming messages :)
guest = "Bob"


# Create message variable (with f-string) welcoming customer to your new car store and an overview of brand and year inventory
message = f"Hello {guest.title()}, welcome to our dealership! At {brand.capitalize()}, we sell {len(cars)} cars"


# Create awesome banner with your brand/name/dealership, however you want to welcome customers
banner = f"{brand.title()} - {len(new_year_models)} new cars are sold:\n{new_year_models}\n\nAt our dealership we sell the following {len(cars)} cars:\n{cars}"


# Print awesome banner and welcome message
print(banner)
print("\n")
print(message)


# Using title methods, print the number vehicles in alphabetical order, with the year and available colors.
cars.sort() 
number_vehicules = len(cars)
for car in cars:
    print(f"{car.title()} - 2022 - Available colors: {colors}")


# Create a variable that calculates a monthly payment (no interest) for 5yr/60months for the first vehicle
monthly_payment = MSRPS[0] / LOAN5 


# and print that in a nice, kind message. Don't be rude/pushy to the customer :)
print(f"\n{cars[0].title()} is ${MSRPS[0]}. Monthly payment for 5 years is ${monthly_payment}.")


# Do the same thing, but give them 4yr and 6yr options for the same vehicle
monthly_payment = MSRPS[0] / LOAN4 
print(f"{cars[0].title()} is ${MSRPS[0]}. Monthly payment for 4 years is ${monthly_payment}.")

# Lastly, give them a 5yr option for each of the other vehicles, just to see if they are interested

for index in range(len(cars)):
    monthly_payment = MSRPS[index] / LOAN5 
    print(f"{cars[index].title()} is ${MSRPS[index]}. Monthly payment for 5 years is ${monthly_payment}.")

from cs50 import get_float

# Prompt user for input
while True:
    change = get_float("Change owed: ")
    if change >= 0:
        break

# Convert dollars to cents
cents = round(change * 100)

coins = 0

# Quarters (25¢)
coins += cents // 25
cents %= 25

# Dimes (10¢)
coins += cents // 10
cents %= 10

# Nickels (5¢)
coins += cents // 5
cents %= 5

# Pennies (1¢)
coins += cents

# Print result
print(coins)

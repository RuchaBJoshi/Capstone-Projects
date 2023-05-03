#created a menu as a list with 5 items.

menu = ['tea', 'cake', 'sandwich', 'coffee', 'hot chocolate']

#created dictionary for stock amount and price for the corresponding item from the menu.

stock = {'tea': 59,
         'cake': 40,
         'sandwich': 125,
         'coffee': 75,
         'hot chocolate': 70}

price = {'tea': 1.75,
         'cake': 3.00,
         'sandwich': 4.50,
         'coffee': 2.25,
         'hot chocolate': 2.90}

# Created a for loop.
# Set up two variables that can be increased in value upon each interation to keep track of number of items and their corresponding values.
# This also helps sum up the cost with each iteration to display the total stock value so far at the end of each iteration.
# Furthermore, allows me to calculate the grand total of stock value in the end after completion of all iterations.

item_number = 0
sum_value = 0

for item in menu:
    item_value = stock[item] * price[item]
    item_number += 1
    sum_value += item_value
    print('\nItem ' + str(item_number) + ' value: ' + str(item_value))
    print('new total = '+ str(sum_value))

print('\nTotal stock value of all the items in the cafe is £' + str(sum_value) + '\n')

#End of code
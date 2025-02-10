"""
This script calculates the total cost of food items at my coffee shop.

The program asks the user for the number of coffees, muffins, fuits, and croissants they bought, then calculates a subtotal, tax, and total amount due.

Price details:
- coffee: $5 each
- Muffin: $4 each
- Fruit: $3 each
- Croissant: $7 each
- Tax: 6%

Output:
The program prints a detailed receipt displaying the number of items, cost per item, tax amount, and total.
"""

print('Shiv's Coffee Shop Receipt')

#Prices of items
price_coffee = 5
price_muffin = 4
price_fruit = 3
price_crois = 7

#Get user input of purchase details
num_coffee = int(input('Number of coffees bought?: '))
num_muffin = int(input('Number of muffins bought?: '))
num_fruit = int(input('Number of fruits bought?: '))
num_crois = int(input('Number of croissants bought?: '))

#Calculates item subamounts and formats amounts to two decimal places for input into print functions
sub_coffee = price_coffee * num_coffee
form_coffee = f'{sub_coffee:.2f}'
sub_muffin = price_muffin * num_muffin
form_muffin = f'{sub_muffin:.2f}'
sub_fruit = price_fruit * num_fruit
form_fruit = f'{sub_fruit:.2f}'
sub_crois = price_crois * num_crois
form_crois = f'{sub_crois:.2f}'

#Calculates subtotal, tax, and total, and rounds values to two decimal places
subtotal = sub_coffee + sub_muffin + sub_fruit + sub_crois
total = subtotal * 1.06
total = round(total,2)
tax = total - subtotal
tax = round(tax,2)

#Displays the receipt and thanks the user
print(f'{num_coffee} Coffee(s) at ${price_coffee} each: ${form_coffee}')
print(f'{num_muffin} Muffin(s) at ${price_muffin} each: ${form_muffin}')
print(f'{num_fruit} Fruit(s) at ${price_fruit} each: ${form_fruit}')
print(f'{num_crois} Croissant(s) at ${price_crois} each: ${form_crois}')
print(f'6% tax: ${tax}')
print('---------')
print(f'Total: ${total}')
print('\nThank you for your purchase.\nWe hope to see you again soon!')

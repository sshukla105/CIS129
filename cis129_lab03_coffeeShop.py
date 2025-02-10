"""
This script calculates the total cost of coffee(s) and muffin(s) at my coffee shop.

the program asks the user for the number of coffees and muffins they bought, then calculates a subtotal, tax, and total amount due.

Price details:
- coffee: $5 each
- Muffin: $4 each
- Tax: 6%

Output:
The program prints a detailed receipt displaying the number of items, cost per item, tax amount, and total.
"""

#Get user input of purchase details
num_coffee = int(input('Number of coffees bought?: '))
num_muffin = int(input('Number of muffins bought?: '))

#Prices of items
price_coffee = 5
price_muffin = 4

#Calculates item subamounts and formats amounts to two decimal places for input into print functions
sub_coffee = price_coffee * num_coffee
form_coffee = f'{sub_coffee:.2f}'
sub_muffin = price_muffin * num_muffin
form_muffin = f'{sub_muffin:.2f}'

#Calculates subtotal, tax, and total, and rounds values to two decimal places
subtotal = sub_coffee + sub_muffin
total = subtotal * 1.06
total = round(total,2)
tax = total - subtotal
tax = round(tax,2)

#Displays the receipt
print('My Coffee and Muffin Shop')
print(f'{num_coffee} Coffee(s) at ${price_coffee} each: ${form_coffee}')
print(f'{num_muffin} Muffin(s) at ${price_muffin} each: ${form_muffin}')
print(f'6% tax: ${tax}')
print('---------')
print(f'Total: ${total}')

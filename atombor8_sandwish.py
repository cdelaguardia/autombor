import pyinputplus

bread_type = ['wheat', 'white', 'black']
bread_price_list = [2, 2.5, 1]
protein_type = ['chicken', 'turkey', 'ham', 'tofu']
protein_price_list = [5, 5.2, 3, 2]
cheese_price = 1
many=0
price=0

print('This program will help you to prepare your favorite sandwish')
print('Choose the bread type for your sandwish')
bread = pyinputplus.inputMenu(bread_type, numbered = True)
price+=bread_price_list[bread_type.index(bread)]

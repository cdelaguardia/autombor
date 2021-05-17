import pyinputplus

bread_type = ['wheat', 'white', 'black']
bread_price_list = [2, 2.5, 1]

protein_type = ['chicken', 'turkey', 'ham', 'tofu']
protein_price_list = [5, 5.2, 3, 2]

cheese_type = ['cheddar', 'Swiss', 'mozzarella']
cheese_price_list = [3, 4, 3.5]
many=0
price=0

print('This program will help you to prepare your favorite sandwish')

print('Choose the bread type for your sandwish')
bread = pyinputplus.inputMenu(bread_type, numbered = True)
price+=bread_price_list[bread_type.index(bread)]

print('\nChoose the protein type for your sandwish')
protein = pyinputplus.inputMenu(protein_type, numbered = True)
price+=protein_price_list[protein_type.index(protein)]

cheese=pyinputplus.inputYesNo('\nDo you waant cheese, yes or no ?\n')
if cheese == 'yes':
    print('\nChoose the cheese type for your sandwish')
    cheese = pyinputplus.inputMenu(cheese_type, numbered = True)
    price+=cheese_price_list[cheese_type.index(cheese)]

print('\nDo you want mayo?')
mayo = pyinputplus.inputYesNo()
if mayo == 'yes':
    price+=1

print('\nDo you want mustard?')
mustard = pyinputplus.inputYesNo()
if mustard == 'yes':
    price+=1

print('\nDo you want letuce?')
letuce = pyinputplus.inputYesNo()
if letuce == 'yes':
    price+=1

print('\nDo you want tomato?')
tomato = pyinputplus.inputYesNo()
if tomato == 'yes':
    price+=1

while True:
    cantidad = input('\nYa que elegiste el tipo de sandwish, cuanto de estos quieres?\n')
    cantidad = int(cantidad)
    if cantidad >0:
        total_cost=price*cantidad
        print(f'\nEl costo toal de todo es {total_cost}.')
        break

    else:
        print('\nNo me has dicho la cantidad de manera adecuada')
        continue

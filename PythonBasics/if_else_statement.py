#Creating a Pizza Order System

print('Welcome to Python Pizza Deliveries')
#ps =pizza sizes
ps = input ("Pizza size. Enter 's' for small, 'm' for medium, or 'l'for large \n").lower()
if (ps != 's' and ps != 'm' and ps != 'l'):
    print('enter valid options')
else:
    if ps == 's':
        price = 15
    elif ps == 'm':
        price = 20
    elif ps == 'l':
        price=25
    #ap = add_pepperoni
    ap= input ("Add pepperoni? enter 'y' for yes or 'n' for no \n").lower()
    if (ap != 'y' and ap != 'n'):
        print('enter valid options')
    else:
        if ps== 's' and ap =='y':
            price+= 2
        elif (ps == 'm' or ps =='l') and  ap == 'y':
            price+=3
        #c = cheese
        c= input("Extra cheese? enter 'y' for yes or 'n' for no \n").lower()
        if (c != 'y' and c != 'n'):
            print('enter valid options')
        else:
            if c == 'y':
                price+= 1

            print (f"Your total bill is ${price}")

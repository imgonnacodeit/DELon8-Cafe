import codetest
#LOAD products list from products.txt
# productsFile = open('products.txt', 'r')
# productsLine = productsFile.readlines()
# products = []
# for p_line in productsLine:
#     p_line = p_line.strip()
#     products.append(p_line)


#LOAD couriers list from couriers.txt
courierFile = open('couriers.txt', 'r')
courierLine = courierFile.readlines()
courier = []
for c_line in courierLine:
    c_line = c_line.strip()
    courier.append(c_line)

#     The above can be replace with a functions to not be repeating 

# An empty list to append the orders
orders = []


selection = 0
    
#Printing the main menu
#Put the below on one line 
print('Welcome to the main menu')
while selection == 0 :
    print('')
    print('MENU')
    print('To EXIT the program select 0')
    print('To enter the PRODUCTS MENU select 1')
    print('To enter the ORDERS MENU select 2')
    print('To enter the COURIERS MENU select 3')
    

    #Get the choice from the main menu

    #Save everything for both files and then exit the APP
    print('')
    choice = (int(input('What is your choice: ')))
    if choice == 0:
        productsFile = open('products.txt', 'w')
        productsFile.write('\n'.join(codetest.productlist))
        productsFile.close()

        courierFile = open('couriers.txt', 'w')
        courierFile.write('\n'.join(courier))
        courierFile.close()


        break

   
    if choice == 1:
        while True:
            print ('')
            print ('')
            print ('PRODUCTS MENU')
            print ('0. Return to the MAIN MENU.')
            print ('1. To PRINT all products')
            print ('2. To CREATE a new product') 
            print ('3. To UPDATE a product')
            print ('4. To DELETE a product')
            print('')
            
            #Taking an input for the products menu
            product_menu_choice = int(input(''))

            #Exit out of the product menu
            if product_menu_choice == 0:
                break


            #Takes everyproduct and prints it to a new line.
            if product_menu_choice == 1:
                codetest.PRODUCT_print()


            #Creating new items in the list. 
            elif product_menu_choice == 2:
                x = codetest.PRODUCT_dic()
                codetest.PRODUCT_add(x)
                


            #This updates the product list 
            elif product_menu_choice == 3:
                codetest.PRODUCT_update()



            #This will delete something from the list using the index number.
            elif product_menu_choice == 4:
                codetest.PRODUCT_delete()

import codetest
 
while True:
    choice = int(input('\nWELCOME TO THE MAIN MENU\n\n\nMENU\nTo EXIT the program select 0\nTo enter the PRODUCTS MENU select 1\nTo enter the ORDERS MENU select 2\nTo enter the COURIERS MENU select 3\n\nPlease enter selection: '))
    if choice == 1:
        x = 'name'
        y = 'price'
        z = codetest.productlist
        while True:
            #Taking an input for the products menu
            product_menu_choice = int(input('\nPRODUCTS MENU\n0. Return to the MAIN MENU.\n1. To PRINT all products\n2. To CREATE a new product\n3. To UPDATE a product\n4. To DELETE a product\n\nPlease enter selection: '))

            #Exit out of the product menu
            if product_menu_choice == 0:
                break

            #Takes everyproduct and prints it to a new line.
            if product_menu_choice == 1:
                codetest.printing(x, y, z)
                
            #Creating new items in the list. 
            elif product_menu_choice == 2:
                create_new = codetest.PRODUCT_making_dic()
                codetest.add(create_new, z)
                
            #This updates the product list 
            elif product_menu_choice == 3:
                codetest.printing(x, y, z)
                choice = int(input('Which number would you like to choose'))
                select = input(f'Would you like to change the {x} or the {y}')
                update = input('What would you like to change it to.')
                codetest.update(choice, select, update, z)
                codetest.printing(x, y, z)

            #This will delete something from the list using the index number.
            elif product_menu_choice == 4:
                codetest.printing(x, y, z)
                codetest.delete(z)
                codetest.printing(x, y, z)

    if choice == 1:
        x = 'name'
        y = 'price'
        z = codetest.productlist
        while True:
            #Taking an input for the products menu
            product_menu_choice = int(input('\nPRODUCTS MENU\n0. Return to the MAIN MENU.\n1. To PRINT all products\n2. To CREATE a new product\n3. To UPDATE a product\n4. To DELETE a product\n\nPlease enter selection: '))

            #Exit out of the product menu
            if product_menu_choice == 0:
                break

            #Takes everyproduct and prints it to a new line.
            if product_menu_choice == 1:
                codetest.printing(x, y, z)
                
            #Creating new items in the list. 
            elif product_menu_choice == 2:
                create_new = codetest.PRODUCT_making_dic()
                codetest.add(create_new, z)
                
            #This updates the product list 
            elif product_menu_choice == 3:
                codetest.printing(x, y, z)
                choice = int(input('Which number would you like to choose'))
                select = input(f'Would you like to change the {x} or the {y}')
                update = input('What would you like to change it to.')
                codetest.update(choice, select, update, z)
                codetest.printing(x, y, z)

            #This will delete something from the list using the index number.
            elif product_menu_choice == 4:
                codetest.printing(x, y, z)
                codetest.delete(z)
                codetest.printing(x, y, z)
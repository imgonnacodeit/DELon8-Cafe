import codetest
 
while True:
    choice = int(input('\nWELCOME TO THE MAIN MENU\n\n\nMENU\nTo EXIT the program select 0\nTo enter the PRODUCTS MENU select 1\nTo enter the ORDERS MENU select 2\nTo enter the COURIERS MENU select 3\n\nPlease enter selection: '))
    if choice == 1:
        e = 'of the item'
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
                create_new = codetest.PRODUCT_making_dic(e)
                codetest.add(create_new, z)
                
            #This updates the product list 
            elif product_menu_choice == 3:
                codetest.printing(x, y, z)
                index_value = int(input('Please enter the number of the product that you would like to update: '))
                a = input('Please enter the new value for the name')
                b = (input('Please enter the new value for the price'))
                codetest.update(index_value, a, b, x, y, z)
                codetest.printing(x, y, z)

            #This will delete something from the list using the index number.
            elif product_menu_choice == 4:
                codetest.printing(x, y, z)
                codetest.delete(z)
                codetest.printing(x, y, z)

       
    elif choice == 2:
        e = 'of the person'
        x = 'name'
        y = 'phone number'
        z = codetest.courierlist
        while True:
            #Taking an input for the couriers menu
            courier_menu_choice = int(input('\nCOURIERS MENU\n0. Return to the MAIN MENU.\n1. To PRINT all couriers\n2. To CREATE a new product\n3. To UPDATE a courier\n4. To DELETE a courier\n\nPlease enter selection: '))

            #Exit out of the courier menu
            if courier_menu_choice == 0:
                break

            #Takes everyproduct and prints it to a new line.
            if courier_menu_choice == 1:
                codetest.printing(x, y, z)
                
            #Creating new items in the list. 
            elif courier_menu_choice == 2:
                create_new = codetest.COURIER_making_dic(e)
                codetest.add(create_new, z)
                
            #This updates the product list 
            elif courier_menu_choice == 3:
                codetest.printing(x, y, z)
                index_value = int(input('Please enter the number of the courier that you would like to update: '))
                a = input('Please enter the new value for the courier name')
                b = (input('Please enter the new value for the courier phone number'))
                codetest.update(index_value, a, b, x, y, z)
                codetest.printing(x, y, z)

            #This will delete something from the list using the index number.
            elif courier_menu_choice == 4:
                codetest.printing(x, y, z)
                codetest.delete(z)
                codetest.printing(x, y, z)

    elif choice == 3:
        z = codetest.orderlist
        status = 'Preparing'
        while True:
            order_menu_choice = int(input('\nORDERS MENU\n0. Return to the MAIN MENU.\n1. To PRINT all orders\n2. To CREATE a new order\n3. To UPDATE an order\n4. To DELETE an order\n\nPlease enter selection: '))

            if order_menu_choice == 0:
                break

            if order_menu_choice == 1:
                codetest.ORDER_print(z)

            if order_menu_choice == 2:
                customer_name = input('Please enter the customer name. ')
                customer_address = input('Please enter the customer address. ')
                customer_phone = int(input('Please enter the phone number of the customer. '))

                print_product = codetest.printing(x = 'name', y = 'price', z = codetest.productlist)
                ordering_products = []
                
                
                myseparator = ', '
                while True:
                    index_product = int(input('Please select your item number that you would like to add to your list. '))
                    if index_product == '':
                        break
                    ordering_products.append(index_product)
                    print(ordering_products)
                
                x = myseparator.join(ordering_products)
                courier_print = codetest.printing(x = 'name', y = 'phone number', z = codetest.courierlist)

                new_order = codetest.ORDER_dic(customer_name, customer_address, customer_phone, status)
                codetest.add(new_order, z)

            if order_menu_choice == 3:
                codetest.ORDER_print(z)
                order_index_value = int(input('Please enter the number for the order that you would like to modify'))

            
            if order_menu_choice == 4:
                codetest.ORDER_print(z)


            if order_menu_choice == 5:
                codetest.delete(z)

            if order_menu_choice == 6:
                pass
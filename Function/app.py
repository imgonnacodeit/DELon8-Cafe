import codetest
import csv

pl = codetest.productlist
cl = codetest.courierlist
ol = codetest.orderlist
x = 'name'
p = 'price'
n = 'phone number'
codetest.opening_products(pl)
codetest.opening_couriers(cl)
codetest.opening_orders(ol)



while True:
    try:
        choice = int(input('\nWELCOME TO THE MAIN MENU\n\n\nMENU\nTo EXIT the program select 0\nTo enter the PRODUCTS MENU select 1\nTo enter the COURIERS MENU select 2\nTo enter the ORDERS MENU select 3\n\nPlease enter selection: '))
    except:
        print('You did not insert the correct input. Exiting program')
        break

   
    if choice == 0:
        break

    elif choice == 1:
        e = 'of the item'
        z = codetest.productlist
        while True:
            #Taking an input for the products menu
            product_menu_choice = int(input('\nPRODUCTS MENU\n0. Return to the MAIN MENU.\n1. To PRINT all products\n2. To CREATE a new product\n3. To UPDATE a product\n4. To DELETE a product\n\nPlease enter selection: '))

            #Exit out of the product menu
            if product_menu_choice == 0:
                codetest.writer_product(pl)
                break

            #Takes everyproduct and prints it to a new line.
            if product_menu_choice == 1:
                codetest.printing(x, p, pl)
                
            #Creating new items in the list. 
            elif product_menu_choice == 2:
                create_new = codetest.PRODUCT_making_dic(e)
                codetest.add(create_new, pl)
                
            #This updates the product list 
            elif product_menu_choice == 3:
                codetest.printing(x, p, pl)
                index_value = int(input('Please enter the number of the product that you would like to update: '))
                a = input('Please enter the new value for the name')
                b = input('Please enter the new value for the price')
                codetest.update(index_value, a, b, x, p, pl)
                codetest.printing(x, p, pl)

            #This will delete something from the list using the index number.
            elif product_menu_choice == 4:
                codetest.printing(x, p, pl)
                codetest.delete(pl)
                codetest.printing(x, p, pl)
  
    elif choice == 2:
        e = 'of the person'
        while True:
            #Taking an input for the couriers menu
            courier_menu_choice = int(input('\nCOURIERS MENU\n0. Return to the MAIN MENU.\n1. To PRINT all couriers\n2. To ADD a new courier\n3. To UPDATE a courier\n4. To DELETE a courier\n\nPlease enter selection: '))

            #Exit out of the courier menu
            if courier_menu_choice == 0:
                codetest.writer_courier(cl)
                break

            #Takes everyproduct and prints it to a new line.
            if courier_menu_choice == 1:
                codetest.printing(x, n, cl)
                
            #Creating new items in the list. 
            elif courier_menu_choice == 2:
                create_new = codetest.COURIER_making_dic(e)
                codetest.add(create_new, cl)
                
            #This updates the product list 
            elif courier_menu_choice == 3:
                codetest.printing(x, n, cl )
                index_value = int(input('Please enter the number of the courier that you would like to update: '))
                a = input('Please enter the new value for the courier name')
                b = (input('Please enter the new value for the courier phone number'))
                codetest.update(index_value, a, b, x, n, cl)
                codetest.printing(x, n, cl)

            #This will delete something from the list using the index number.
            elif courier_menu_choice == 4:
                codetest.printing(x, n, cl)
                codetest.delete(cl)
                codetest.printing(x, n, cl)

    elif choice == 3:
        ol = codetest.orderlist
        status = 'Preparing:'
        while True:
            order_menu_choice = int(input('\nORDERS MENU\n0. Return to the MAIN MENU.\n1. To PRINT all orders\n2. To CREATE a new order\n3. To UPDATE an order STATUS\n4. To UPDATE an order\n5. To DELETE an order\n6. To list orders by STATUS or COURIER\n\nPlease enter selection: '))

            #This will exit to the main menu
            if order_menu_choice == 0:
                codetest.writer_order(ol)
                break
            
            #This prints the orders made
            if order_menu_choice == 1:
                codetest.ORDER_print(ol)


            #This creates an order
            if order_menu_choice == 2:
                customer_name = input('Please enter the customer name. ')
                customer_address = input('Please enter the customer address. ')
                customer_phone = int(input('Please enter the phone number of the customer. '))

                print_product = codetest.printing(x, p, pl)
                ordering_products = []                
                myseparator = ', '
                index_product = input('Please select your item number that you would like to add to your list. ')
                while index_product != '':
                    ordering_products.append(index_product)
                    index_product = input('Please select your item number that you would like to add to your list. ')
                    
                product_selection = myseparator.join(ordering_products)
            
                courier_print = codetest.printing(x, n, cl)
                courier_selection = input('Which courier would you like to have')

                new_order = codetest.ORDER_dic(customer_name, customer_address, customer_phone, courier_selection, status, product_selection )
                
                codetest.add(new_order, ol)

            #This updates the order status
            if order_menu_choice == 3:
                codetest.ORDER_print(ol)
                selection = int(input('Please select which order that you would like to update. '))
                codetest.ORDER_status_print_list(ol)
                codetest.ORDER_status_update(selection, ol)
                codetest.ORDER_print(ol)
            
            #This updates an order
            if order_menu_choice == 4:
                cl = codetest.orderlist
                codetest.ORDER_print(cl)
                index_value = int(input('Please enter the number of the courier that you would like to update: '))
                a = input('Please enter the updated name for the customer name. ')
                b = input('Please enter the updated address. ')
                c = input('Please enter the updated courier selection')
                d = input('Please enter the updated items')
                codetest.ORDER_update(index_value, a, b, c, d, cl)
                codetest.ORDER_print(cl)

            #This deletes an order
            if order_menu_choice == 5:
                codetest.delete(ol)

            #This changes the order into the desired list.
            if order_menu_choice == 6:
                change_order = int(input('Would you like to rearrange by [0]status or [1]courier. '))
                shuffle = codetest.ordering_ORDERS(change_order, ol)
                codetest.ORDER_print(shuffle)
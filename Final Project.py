# Admin - 2001 James
# User - 2006 Simona

# noinspection PyUnresolvedReferences
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

p_df = pd.read_csv("Product.csv")
p_df.set_index("id_no", inplace=True)
u_df = pd.read_csv("Customers.csv")
u_df.set_index("id_no", inplace=True)

print("*" * 46)
print("\t\t\tOnline Shopping System")
print("*" * 46)
print()

tf = "-"
while tf.casefold() != 'e':
    tf = input("Enter the type of user(A for admin, U for user) or press E to exit: ").casefold()
    if tf.casefold() == 'a':
        u_id = int(input("Enter your id: "))
        first_name = input("Enter your first name: ").casefold()
        for index in u_df.index:
            first = u_df.loc[index, 'first_name'].casefold()
            u_type = u_df.loc[index, 'type'].casefold()
            if (index == u_id) & (first == first_name) & (u_type == tf):
                print("Login successful!")
                choice = -1
                while choice != 13:
                    print()
                    print("*****************Admin Menu*****************")
                    print()
                    print("1.  Display Product Menu")
                    print("2.  Display Product Menu From A Specific Category")
                    print("3.  Add Product")
                    print("4.  Remove Product")
                    print("5.  Edit Product")
                    print("6.  Display List Of Users")
                    print("7.  Display List OF Users From A Specific Category")
                    print("8.  Add User")
                    print("9.  Remove User")
                    print("10. Edit User Details")
                    print("11. Plot Line Chart Of Product vs Price")
                    print("12. Plot Bar Graph Of Product vs Price")
                    print("13. Logout")
                    print("********************************************")
                    print()
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        print("Displaying product menu....\n")
                        print(p_df)
                        print()
                        print("********************************************")
                        temp = input("Press 'C' key...")
                    elif choice == 2:
                        for category in p_df.category.unique():
                            print(category)
                        c_choice = input("\nEnter your preferred category: ").casefold()
                        print("Displaying product menu from a specific category....\n")
                        for index2 in p_df.index:
                            if c_choice == p_df.loc[index2, 'category'].casefold():
                                print(p_df.loc[index2, :])
                                print()
                        print()
                        print("********************************************")
                        temp = input("Press 'C' key...")
                    elif choice == 3:
                        total = len(p_df)
                        print("Total No. Of Products: {}". format(total))
                        print("Enter the product details:\n")
                        name = input("Name: ")
                        available = input("Available stock: ")
                        price = input("Price: ")
                        o_price = input("Original Price: ")
                        category = input("Category: ")
                        print("Adding Product.....")
                        row = total + 1001
                        temp = pd.Series(data={'name': name, 'available': available, 'price': price,
                                               'original_price': o_price, 'category': category},
                                         index=['name', 'available', 'price', 'original_price', 'category'],
                                         name=row)
                        p_df = p_df.append(temp)
                        print("Product added!")
                        total = len(p_df)
                        print("Total No. Of Products: {}". format(total))
                        print(p_df)
                        p_df.to_csv("Product.csv")
                        print()
                        print("********************************************")
                        temp = input("Press 'C' key...")
                    elif choice == 4:
                        total = len(p_df)
                        print("Total No. Of Products: {}". format(total))
                        id_no = int(input("Enter ID of product to be removed: "))
                        if id_no in p_df.index:
                            print("Removing product.....")
                            p_df.drop(id_no, axis=0, inplace=True)
                            print("Product removed!")
                            for old_id in p_df.index:
                                if old_id > id_no:
                                    new_id = old_id - 1
                                    p_df.rename(index={old_id: new_id}, inplace=True)
                            total = len(p_df)
                            print("Total No. Of Products: {}". format(total))
                            print(p_df)
                            p_df.to_csv("Product.csv")
                        else:
                            print("Oops! Wrong details.")
                        print()
                        print("********************************************")
                        temp = input("Press 'C' key...")
                    elif choice == 5:
                        col_list = ['Name', 'Available', 'Price', 'Original_Price', 'Category']
                        id_no = int(input("Enter the ID no. of the product to be edited: "))
                        for index2 in p_df.index:
                            if index2 == id_no:
                                print(p_df.loc[index2, :])
                                print("Enter the edited details: ")
                                for col in col_list:
                                    p_df.loc[index2, col.casefold()] = input('{}: '.format(col))
                                    proceed = input("Do you want to continue(Y/N): ").casefold()
                                    if proceed == 'n':
                                        break
                                    elif proceed == 'y':
                                        continue
                                    else:
                                        print("Wrong choice!")
                                        break
                                print("Product details edited!")
                                print(p_df.loc[index2, :])
                                p_df.to_csv("Product.csv")
                                break
                        else:
                            print("Oops! Wrong details.")
                        print()
                        print("********************************************")
                        temp = input("Press 'C' key...")
                    elif choice == 6:
                        print("Displaying customer list....\n")
                        print(u_df)
                        print()
                        print("********************************************")
                        temp = input("Press 'C' key...")
                    elif choice == 7:
                        for category in u_df.type.unique():
                            print(category)
                        c_choice = input("\nEnter your preferred category: ").casefold()
                        print("Displaying customer list from a specific category....\n")
                        for index2 in u_df.index:
                            if c_choice == u_df.loc[index2, 'type'].casefold():
                                print(u_df.loc[index2, :])
                                print()
                        print()
                        print("********************************************")
                        temp = input("Press 'C' key...")
                    elif choice == 8:
                        total = len(u_df)
                        print("Total No. Of Customers: {}". format(total))
                        print("Enter the customer details:\n")
                        u_type = input("Type: ")
                        first = input("First name: ")
                        last = input("Last name: ")
                        company = input("Company name(if any): ")
                        address = input("Address: ")
                        city = input("City: ")
                        district = input("District/County: ")
                        state = input("State(in code): ")
                        country = input("Country: ")
                        zipcode = input("PIN Code: ")
                        phone1 = input("1st Phone No.: ")
                        phone2 = input("2nd Phone No.: ")
                        email = input("Email Address: ")
                        web = input("Website(if any): ")
                        print("Adding customer.....")
                        row = total + 2001
                        temp = pd.Series(data={'type': u_type, 'first_name': first, 'last_name': last,
                                               'company_name': company, 'address': address, 'city': city,
                                               'county': district, 'state': state, 'country': country, 'zip': zipcode,
                                               'phone1': phone1, 'phone2': phone2, 'email': email, 'web': web},
                                         index=['type', 'first_name', 'last_name', 'company_name',
                                                'address', 'city', 'county', 'state', 'country',
                                                'zip', 'phone1', 'phone2', 'email', 'web'],
                                         name=row)
                        u_df = u_df.append(temp)
                        print("Customer details added!")
                        total = len(u_df)
                        print("Total No. Of Customers: {}". format(total))
                        print(u_df)
                        u_df.to_csv("Customers.csv")
                        print()
                        print("********************************************")
                        temp = input("Press 'C' key...")
                    elif choice == 9:
                        total = len(u_df)
                        print("Total No. Of Customers: {}". format(total))
                        id_no = int(input("Enter ID of customer to be removed: "))
                        if id_no in u_df.index:
                            print("Removing customer details.....")
                            u_df.drop(id_no, axis=0, inplace=True)
                            print("Customer removed!")
                            for old_id in u_df.index:
                                if old_id > id_no:
                                    new_id = old_id - 1
                                    u_df.rename(index={old_id: new_id}, inplace=True)
                            total = len(u_df)
                            print("Total No. Of Customers: {}". format(total))
                            print(u_df)
                            u_df.to_csv("Customers.csv")
                        else:
                            print("Oops! Wrong details.")
                        print()
                        print("********************************************")
                        temp = input("Press 'C' key...")
                    elif choice == 10:
                        col_list = ['Type', 'First', 'Last', 'Company', 'Address', 'City', 'County', 'State',
                                    'Country', 'Zipcode', 'Phone1', 'Phone2', 'Email', 'Web']
                        id_no = int(input("Enter the ID no. of the product to be edited: "))
                        for index2 in u_df.index:
                            if index2 == id_no:
                                print(u_df.loc[index2, :])
                                print("Enter the edited details: ")
                                for col in col_list:
                                    u_df.loc[index2, col.casefold()] = input('{}: '.format(col))
                                    proceed = input("Do you want to continue(Y/N): ").casefold()
                                    if proceed == 'n':
                                        break
                                    elif proceed == 'y':
                                        continue
                                    else:
                                        print("Wrong choice!")
                                        break
                                print("Customer details edited!")
                                print(u_df.loc[index2, :])
                                u_df.to_csv("Customers.csv")
                                break
                        else:
                            print("Oops! Wrong details.")
                        print()
                        print("********************************************")
                        temp = input("Press 'C' key...")
                    elif choice == 11:
                        print(p_df)
                        print("Plotting the line chart.....")
                        x = p_df['name']
                        y = p_df['price']
                        plt.title('Price Comparison For Different Products')
                        plt.plot(x, y, marker='X', ls='dashed', linewidth=4, color='r')
                        plt.xlabel("Products")
                        plt.ylabel("Price")
                        plt.xticks(rotation=30)
                        plt.grid(True)
                        plt.show()
                        print()
                        print("********************************************")
                        temp = input("Press 'C' key...")
                    elif choice == 12:
                        print(p_df)
                        print("Plotting the bar graph.....")
                        x = p_df['name']
                        y = p_df['price']
                        plt.title('Price Comparison For Different Products')
                        plt.bar(x, y, color='red')
                        plt.xlabel("Products")
                        plt.ylabel("Price")
                        plt.show()
                        print()
                        print("********************************************")
                        temp = input("Press 'C' key...")
                    elif choice == 13:
                        print("Logging Out! Have a good time.")
                        print()
                        print("********************************************")
                    else:
                        print("Oops! Wrong choice. Try again.")
                break
        else:
            print("Sorry! You entered the wrong credentials.")
    elif tf.casefold() == 'u':
        u_id = int(input("Enter your id: "))
        first_name = input("Enter your first name: ").casefold()
        for index in u_df.index:
            first = u_df.loc[index, 'first_name'].casefold()
            u_type = u_df.loc[index, 'type'].casefold()
            if (index == u_id) & (first == first_name) & (u_type == tf):
                print("Login successful!")
                choice = -1
                while choice != 5:
                    print("******************User Menu******************")
                    print()
                    print("1. Display Product Menu")
                    print("2. Display Product Menu Grouped By Category")
                    print("3. Place Order")
                    print("4. Cancel Order")
                    print("5. Logout")
                    print("*********************************************")
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        print("Displaying product menu....\n")
                        print(p_df)
                        print()
                        print("********************************************")
                        temp = input("Press 'C' key...")
                    elif choice == 2:
                        for category in p_df.category.unique():
                            print(category)
                        c_choice = input("\nEnter your preferred category: ").casefold()
                        print("Displaying product menu from a specific category....\n")
                        for index2 in p_df.index:
                            if c_choice == p_df.loc[index2, 'category'].casefold():
                                print()
                                print(p_df.loc[index2, :])
                        print()
                        print("********************************************")
                        temp = input("Press 'C' key...")
                    elif choice == 3:
                        id_no = int(input("Enter the product id that you want to purchase: "))
                        for index2 in p_df.index:
                            if (index2 == id_no) & (p_df.loc[index2, 'available'] > 0):
                                p_df.loc[index2, 'available'] -= 1
                                if u_df.loc[index, 'latest_order'] != '':
                                    u_df.loc[index, 'last_order2'] = u_df.loc[index, 'last_order1']
                                    u_df.loc[index, 'last_order1'] = u_df.loc[index, 'latest_order']
                                u_df.loc[index, 'latest_order'] = str("#{}#{}".format(u_id, id_no))
                                print("Product purchase added to user details!")
                                print(u_df.loc[index, :])
                                u_df.to_csv("Customers.csv")
                                p_df.to_csv("Product.csv")
                                break
                        else:
                            print("Product id not found or stock empty for the chosen product!")
                        print()
                        print("********************************************")
                        temp = input("Press 'C' key...")
                    elif choice == 4:
                        id_no = int(input("Enter the product id that you want to cancel: "))
                        for index2 in p_df.index:
                            if index2 == id_no:
                                if str(id_no) in str(u_df.loc[index, 'latest_order']):
                                    p_df.loc[index2, 'available'] += 1
                                    u_df.loc[index, 'latest_order'] = ''
                                    print("Order cancelled!")
                                    print(p_df.loc[index, :])
                                    u_df.to_csv("Customers.csv")
                                    p_df.to_csv("Product.csv")
                                    break
                        else:
                            print("Product id not found or order not found in customer details!")
                        print()
                        print("********************************************")
                        temp = input("Press 'C' key...")
                    elif choice == 5:
                        print("Logging Out! Have a good time.")
                        print()
                        print("********************************************")
                    else:
                        print("Oops! Wrong choice. Try again.")
                break
        else:
            print("Sorry! You entered the wrong credentials.")
    elif tf. casefold() == 'e':
        print("\nExiting the program. Thank You!")
    else:
        print("Oops! Wrong key.\n")

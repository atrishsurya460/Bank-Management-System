import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

p_df = pd.read_csv("Product.csv")
u_df = pd.read_csv("Customers.csv")

print("*" * 46)
print("\t\t\tOnline Shopping System")
print("*" * 46)
print()

tf = "-"
choice = -1
while tf.casefold() != 'e':
    tf = str(input("Enter the type of user(A for admin, U for user) or press E to exit: "))
    if tf.casefold() == 'a':
        u_id = int(input("Enter your id: "))
        first_name = str(input("Enter your first name: ")).casefold()
        for index1 in u_df.index:
            i = u_df.loc[index1, 'id_no']
            f = u_df.loc[index1, 'first_name']
            t = u_df.loc[index1, 'type']
            if (i == u_id) & (f.casefold() == first_name) & (t == 'A'):
                print("Login successful!")
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
                        p_df = pd.read_csv("Product.csv", index_col=0)
                        print("Displaying product menu....\n")
                        print(p_df)
                        print()
                        print("********************************************")
                    elif choice == 2:
                        p_df = pd.read_csv("Product.csv")
                        for category in sorted(list(set(p_df['category']))):
                            print(category)
                        c_choice = str(input("\nEnter your preferred category: "))
                        print("Displaying product menu from a specific category....\n")
                        for index6 in p_df.index:
                            if c_choice.casefold() == p_df.loc[index6, 'category'].casefold():
                                print(p_df.loc[index6, 'id_no':'category'])
                        print()
                        print("********************************************")
                    elif choice == 3:
                        p_df = pd.read_csv("Product.csv")
                        total = len(p_df)
                        print("Total No. Of Products: {}". format(total))
                        print("Enter the product details:\n")
                        name = input("Name: ")
                        available = input("Available stock: ")
                        price = input("Price: ")
                        o_price = input("Original Price: ")
                        category = input("Category: ")
                        #id_no = int(p_df.loc[:, 'id_no']).max()
                        print("Adding Product.....")
                        temp = pd.Series(data={'id_no': total + 1001, 'name': name, 'available': available,
                                               'price': price, 'original_price': o_price, 'category': category})
                        p_df = p_df.append(temp, ignore_index=True)
                        print("Product added!")
                        total = len(p_df)
                        print("Total No. Of Products: {}". format(total))
                        print(p_df)
                        #p_df.to_csv("Product.csv")
                        print()
                        print("********************************************")
                    elif choice == 4:
                        p_df = pd.read_csv("Product.csv")
                        total = len(p_df)
                        print("Total No. Of Products: {}". format(total))
                        id_no = int(input("Enter ID of product to be removed: "))
                        if id_no in p_df.id_no:
                            print("Removing product.....")
                            p_df.drop(id_no, axis=0, inplace=True)
                            print("Product removed!")
                            total = len(p_df)
                            print("Total No. Of Products: {}". format(total))
                            print(p_df)
                            #p_df.to_csv("Product.csv")
                        else:
                            print("Oops! Wrong details.")
                    elif choice == 5:
                        p_df = pd.read_csv("Product.csv")
                        id_no = int(input("Enter the ID no. of the product to be edited: "))
                        for index2 in p_df.index:
                            i = p_df.loc[index2, 'id_no']
                            if p_df.loc[index2, 'id_no'] == id_no:
                                print("Enter the edited details: ")
                                p_df.loc[index2, 'name'] = str(input('Name:'))
                                p_df.loc[index2, 'available'] = str(input('Available:'))
                                p_df.loc[index2, 'price'] = str(input('Price:'))
                                p_df.loc[index2, 'original_price'] = str(input('Original Price:'))
                                p_df.loc[index2, 'category'] = str(input('Category:'))
                                print("Product details edited!")
                                print(p_df)
                                #p_df.to_csv("Product.csv")
                                break
                        else:
                            print("Oops! Wrong details.")
                        print()
                        print("********************************************")
                    elif choice == 6:
                        u_df = pd.read_csv("Customers.csv", index_col=0)
                        print("Displaying customer list....\n")
                        print(u_df)
                        print()
                        print("********************************************")
                    elif choice == 7:
                        u_df = pd.read_csv("Customers.csv")
                        for category in sorted(list(set(u_df['type']))):
                            print(category)
                        c_choice = str(input("\nEnter your preferred category: "))
                        print("Displaying customer list from a specific category....\n")
                        for index6 in u_df.index:
                            if c_choice.casefold() == u_df.loc[index6, 'type'].casefold():
                                print(u_df.loc[index6, 'id_no':'latest_order'])
                        print()
                        print("********************************************")
                    elif choice == 8:
                        u_df = pd.read_csv("Customers.csv")
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
                        #id_no = u_df["id_no"].max()
                        print("Adding customer.....")
                        temp = pd.Series(data={'id_no': total + 2001, 'type': u_type, 'first_name': first,
                                               'last_name': last, 'company_name': company, 'address': address,
                                               'city': city, 'county': district, 'state': state, 'country': country,
                                               'zip': zipcode, 'phone1': phone1, 'phone2': phone2, 'email': email,
                                               'web': web})
                        u_df = u_df.append(temp, ignore_index=True)
                        print("Customer details added!")
                        total = len(u_df)
                        print("Total No. Of Customers: {}". format(total))
                        print(u_df)
                        #u_df.to_csv("Customers.csv")
                        print()
                        print("********************************************")
                    elif choice == 9:
                        u_df = pd.read_csv("Customers.csv")
                        total = len(u_df)
                        print("Total No. Of Customers: {}". format(total))
                        id_no = int(input("Enter ID of customer to be removed: "))
                        print("Removing customer details.....")
                        u_df.drop(id_no, axis=0, inplace=True)
                        print("Customer removed!")
                        total = len(u_df)
                        print("Total No. Of Customers: {}". format(total))
                        print(u_df)
                        #u_df.to_csv("Customers.csv")
                        print()
                        print("********************************************")
                    elif choice == 10:
                        u_df = pd.read_csv("Customers.csv")
                        id_no = int(input("Enter the ID no. of the customer details to be edited: "))
                        for index3 in u_df.index:
                            if u_df.loc[index3, 'id_no'] == id_no:
                                product = u_df.loc[id_no]
                                print("Enter the edited details: ")
                                u_df.loc[index3, 'u_type'] = str(input("Type: "))
                                u_df.loc[index3, 'first'] = str(input("First name: "))
                                u_df.loc[index3, 'last'] = str(input("Last name: "))
                                u_df.loc[index3, 'company'] = str(input("Company name(if any): "))
                                u_df.loc[index3, 'address'] = str(input("Address: "))
                                u_df.loc[index3, 'city'] = str(input("City: "))
                                u_df.loc[index3, 'district'] = str(input("District/County: "))
                                u_df.loc[index3, 'state'] = str(input("State: "))
                                u_df.loc[index3, 'country'] = str(input("Country: "))
                                u_df.loc[index3, 'zipcode'] = str(input("PIN Code: "))
                                u_df.loc[index3, 'phone1'] = str(input("1st Phone No.: "))
                                u_df.loc[index3, 'phone2'] = str(input("2nd Phone No.: "))
                                u_df.loc[index3, 'email'] = str(input("Email Address: "))
                                u_df.loc[index3, 'web'] = str(input("Website(if any): "))
                                print("Customer details edited!")
                                #u_df.to_csv("Customers.csv")
                                break
                        else:
                            print("Oops! Wrong details.")
                        print()
                        print("********************************************")
                    elif choice == 11:
                        p_df = pd.read_csv("Product.csv", index_col=0)
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
                    elif choice == 12:
                        p_df = pd.read_csv("Product.csv", index_col=0)
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
        first_name = str(input("Enter your first name: "))
        for index4 in u_df.index:
            i = u_df.loc[index4, 'id_no']
            f = u_df.loc[index4, 'first_name']
            a = u_df.loc[index4, 'type']
            if (i == u_id) & (f.casefold() == first_name.casefold()) & (a == 'U'):
                print("Login successful!")
                while choice != 4:
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
                        p_df = pd.read_csv("Product.csv", index_col=0)
                        print("Displaying product menu....\n")
                        print(p_df)
                        print()
                        print("********************************************")
                    elif choice == 2:
                        p_df = pd.read_csv("Product.csv")
                        for category in sorted(set(p_df['category'])):
                            print(category)
                        print("Displaying product menu from a specific category....\n")
                        c_choice = str(input("\nEnter your preferred category: "))
                        for index6 in p_df.index:
                            if c_choice.casefold() == p_df.loc[index6, 'category'].casefold():
                                print(p_df.loc[index6, 'id_no':'category'])
                        print()
                        print("********************************************")
                    elif choice == 3:
                        p_df = pd.read_csv("Product.csv")
                        u_df = pd.read_csv("Customers.csv")
                        id_no = int(input("Enter the product id that you want to purchase: "))
                        for index5 in p_df.index:
                            if p_df.loc[index5, 'id_no'] == id_no:
                                u_df.loc[index4, 'last_order2'] = u_df.loc[index4, 'last_order1']
                                u_df.loc[index4, 'last_order1'] = u_df.loc[index4, 'latest_order']
                                u_df.loc[index4, 'latest_order'] = str("#{}#{}".format(u_id, id_no))
                                print("Product purchase added to user details!")
                                print(p_df)
                                #u_df.to_csv("Customers.csv")
                                break
                        else:
                            print("Product id not found!")
                        print()
                        print("********************************************")
                    elif choice == 4:
                        p_df = pd.read_csv("Product.csv")
                        u_df = pd.read_csv("Customers.csv")
                        id_no = int(input("Enter the product id that you want to cancel: "))
                        for index5 in p_df.index:
                            if p_df.loc[index5, 'id_no'] == id_no:
                                if str(id_no) in str(u_df.loc[index5, 'latest_order']):
                                    u_df.loc[index4, 'latest_order'] = ''
                                    print("Order cancelled!")
                                    print(p_df)
                                    #u_df.to_csv("C:\\Users\\user\\Downloads\\Customers.csv")
                                    break
                        else:
                            print("Product id not found!")
                        print()
                        print("********************************************")
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

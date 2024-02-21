from superstore import *
from shirt_orders_analysis import *

def print_menu():
    print("1. Print products")
    print("2. Print clients")
    print("3. Add Product to store")
    print("4. Add Client to store")
    print("5. Remove Product from store")
    print("6. Remove Client from store")
    print("7. Print products below price")
    print("8. Print the most expensive product")
    print("9. Print smartphone list")
    print("10. Print laptpo list")
    print("11. Print average phone price")
    print("12. Print largest laptop screen")
    print("13. Print common camera resolution")
    print("14. Print popular product")
    print("15. Print all Shirts")
    print("16. Add new Order to the store")
    print("17. Print all Orders")
    print("18. Exit")

def main():

    store = superstore("products_supply.csv", "clients.csv", "shirts.csv", "orders.csv")
    while True:
        print_menu()
        number = int(input("Insert your choice: "))
        if number == 1:
            store.print_products()
        elif number == 2:
            store.print_clients()
        elif number == 3:
            product_id = input("Insert product ID: ")
            product_type = input("Insert product type: ")
            brand = input("Insert product brand: ")
            model = input("Insert product model: ")
            year = input("Insert product year: ")
            price = input("Insert product price: ")
            if product_type.lower() == "laptop":
                CPU = input("Insert product CPU")
                hard_disk = input("Insert product hard disc")
                screen = input("Insert laptpo screen")
                p = laptop(product_id,brand,model,year,price,CPU, hard_disk,screen)
            if product_type.lower() == "smartphone":
                cell_net = input("Insert product cell net")
                num_cores = input("Insert product num cores")
                cam_res = input("Insert product cam res")
                p = Product(product_id, brand, model, year, price)
            length = len(store.products)
            store += p
            if len(store.products) > length:
                print("The Product added to store")
            else:
                print("The Product ID already exists!")
        elif number == 4:
            client_id = input("Insert client ID: ")
            name = input("Insert client name: ")
            email = input("Insert client email: ")
            address = input("Insert client address: ")
            phone_number = input("Insert client phone number: ")
            gender = input("Insert client gender: ")
            c = Client(client_id, name, email, address, phone_number, gender)
            if store.add_client(c): # == True
                print("The Client added to store")
            else:
                print("The Client ID already exists!")
        elif number == 5:
            product_id = int(input("Insert the product id that you wish to remove: "))
            if store.remove_product(product_id): # == True
                print("The Product removed from store")
            else:
                print("The Product ID NOT exists!")
        elif number == 6:
            client_id = int(input("Insert the client id that you wish to remove: "))
            if store.remove_client(client_id): # == True
                print("The Client removed from store")
            else:
                print("The Client ID NOT exists!")
        elif number == 7:
            price = int(input("Insert max price: "))
            lst_price = store.get_all_by_price_number(price)
            if lst_price: # != []
                for p in lst_price:
                    print(p)
            else:
                print("NO products under this price", price)
        elif number == 8:
            print("The most expensive product is: ")
            print(store.get_most_expensive_product())
        elif number == 9:
            lst = store.get_all_phones()
            for p in lst:
                print(p)
        elif number == 10:
            lst = store.get_all_laptops()
            for l in lst:
                print(l)
        elif number == 11:
            print("The average price is:", store.phone_average_price())
        elif number == 12:
            print("The largest Screen is:", store.get_max_screen())
        elif number == 13:
            print("The most common camera resolution:", store.get_common_cam())
        elif number == 14:
            print("The most popular products are:")
            lst = store.list_popular()
            for p in lst:
                print(p)
        elif number == 15:
            store.print_shirts()
        elif number == 16:
            client_id = int(input("insert client Id: "))
            product_id = int(input("Insert Product ID: "))
            quantity = int(input("Insert the quantity for this order: "))
            if store.add_order(client_id, product_id, quantity):
                print("order added")
        elif number ==  17:
            store.print_orders()

        elif number == 18:
            print("See you soon!")
            break
analysis()
if __name__ == "__main__":
    main()
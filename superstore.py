from client import *
from Smartphone import *
from laptop import *
from ClientNotFoundError import *
from ShirtNotFoundError import *
from Product import *
from Order import *
from Shirt import *
import csv

class superstore:
    def __init__(self, file_products, file_clients, file_shirts, file_orders):
        self.products = []
        self.clients = []
        self.Orders = []


        with open(file_products) as b:
            lines = csv.reader(b)
            next(lines)
            for row in lines:
                product_id = row[0]
                product_type = row[1]
                brand = row[2]
                model = row[3]
                year = row[4]
                price = row[5]
                if product_type == "laptop":
                    # cpu = row[6]
                    # hard_disk = row[7]
                    # screen = row[8]
                    cpu = ""
                    hard_disk = ""
                    screen = 0
                    lap = laptop(product_id, brand, model, year, price, cpu, hard_disk, screen)
                    self.products.append(lap)
                if product_type == "smartphone":
                    # cell_net = row[9]
                    # num_cores = row[10]
                    # cam_res = row[11]
                    cell_net = ""
                    num_cores = ""
                    cam_res = ""
                    sma = SmartPhone(product_id, brand, model, year, price, cell_net, num_cores, cam_res)
                    self.products.append(sma)

        with open(file_clients) as b:
            lines = csv.reader(b)
            next(lines)
            for row in lines:
                client_id = row[0]
                name = row[1]
                email = row[2]
                address = row[3]
                phone_number = row[4]
                gender = row[5]
                cli = Client(client_id, name, email, address, phone_number, gender)
                self.clients.append(cli)

        with open(file_shirts) as b:
            lines = csv.reader(b)
            next(lines)
            for row in lines:
                product_id = row[0]
                product_name = row[1]
                price = int(row[2])
                units_in_stock = row[3]
                shirt = Shirt(product_id, product_name, 2023, price, units_in_stock)
                self.products.append(shirt)



        with open(file_orders) as b:
            lines = csv.reader(b)
            next(lines)
            for row in lines:
                order_id = row[0]
                client_id = row[1]
                product_id = row[2]
                quantity = row[3]
                order = Order(order_id, client_id, product_id, quantity)
                self.Orders.append(order)

    def print_products(self):
        for pro in self.products:
            print(pro)

    def print_clients(self):
        for cli in self.clients:
            print(cli)

    def print_shirts(self):
        for s in self.products:
            if type(s) == Shirt:
                print(s)

    def print_orders(self):
        for o in self.Orders:
            print(o)

    def get_product(self, pid):
        for pro in self.products:
            if pro.product_id == pid:
                return pro
        return None

    def get_client(self, cid):
        for cli in self.clients:
            if cli.client_id == cid:
                return cli
        return None

    def add_product(self, n_product):
        if self.get_product(n_product.product_id):  # != None
            return False
        self.products.append(n_product)
        return True

    def add_client(self, n_client):  # != None
        if self.get_client(n_client.client_id):
            return False
        self.clients.append(n_client)
        return True

    def remove_product(self, pid):
        p = self.get_product(pid)
        if p:  # != None
            self.products.remove(p)
            return True
        return False

    def remove_client(self, cid):
        c = self.get_client(cid)
        if c:  # != None
            self.clients.remove(c)
            return True
        return False

    def get_all_by_brand(self, brand):  # brand = "NIKE"
        pro_by_brand = []
        for p in self.products:
            if p.brand.lower() == brand.lower():
                pro_by_brand.append(p)
        return pro_by_brand

    def get_all_by_price_number(self, price):
        pro_by_price = []
        for p in self.products:
            if p.price < price:
                pro_by_price.append(p)
        return pro_by_price

    def get_most_expensive_product(self):
        most = None
        expensive = 0
        for p in self.products:
            if expensive < p.price:
                expensive = p.price
                most = p
        return most

    def get_all_phones(self):
        phones = []
        for i in self.products:
            if type(i) == SmartPhone:
                phones.append(i)
        return phones

    def get_all_laptops(self):
        laptops = []
        for l in self.products:
            if type(l) == laptop:
                laptops.append(l)
        return laptops

    def get_shirt(self, sid):
        for pro in self.products:
            if isinstance(pro, Shirt) and pro.product_id == sid:
                return pro
        return None

    def checkClient(self, client_id):
        if self.get_client(client_id) is None:
            raise ClientNotFoundError

    def checkProduct(self, product_id):
        if self.get_product(product_id) is None:
            raise ShirtNotFoundError

    def exceptions_out(self, client_id, product_id, Product,quantity):
        try:
            self.checkClient(client_id)
            self.checkProduct(product_id)
            if type(Product) == Shirt:
                if self.get_shirt(product_id).units_in_stock < quantity:
                    raise ValueError
            else:
                if quantity > 1:
                    raise ValueError
        except ClientNotFoundError:
            print("\n##########\nClientNotFoundError\n##########\n")
        except ShirtNotFoundError:
            print("\n##########\nShirtNotFoundError\n##########\n")
        except ValueError:
            print("\n##########\nquantity is too much!\n##########\n")



    def add_order(self,client_id, product_id, quantity):
        order_id = int(self.get_max_order_id()) + 1

        n_ord = Order(order_id, client_id, product_id, quantity)
        self.exceptions_out(client_id, product_id, Product,quantity)


    def get_max_order_id(self):
        max_id = self.Orders[0].order_id
        for order in self.Orders:
            if order.order_id > max_id:
                max_id = order.order_id
        return max_id

    def phone_average_price(self):
        lst_phones = self.get_all_phones()
        price = 0
        for p in lst_phones:
            price += p.price
        return price / len(lst_phones)

    def get_max_screen(self):
        screen_size = 0
        lst = self.get_all_laptops()
        for l in lst:
            if l.screen > screen_size:
                screen_size = l.screen
        return screen_size

    def get_common_cam(self):
        phones = self.get_all_phones()
        if not phones:  # == []
            return 0
        most = 0
        most_res = phones[0].cam_res
        counters = {}
        for P in phones:
            if P.cam_res in counters.keys():
                counters[P.cam_res] += 1
            else:
                counters[P.cam_res] = 1
            if counters[P.cam_res] > most:
                most = counters[P.cam_res]
                most_res = P.cam_res
        if most: # != 0
            return most_res
        return None

    def list_popular(self):
        list_popular = []
        for p in self.products:
            if p.Is_popular():
                list_popular.append(p)
        return list_popular

    def __iadd__(self, pro):
        if not self.get_product(pro.product_id): # == None
            self.products.append(pro)
        return self

# s = SuperStore("products_supply.csv", "clients.csv")

# s.print_products()
# s.print_clients()
# print(s.get_product(35821925))
# print(s.get_client(59769))
# p = Product("26838785", "Shoes", "Nike", "Air Jordan 1", "2022", "500")
# if s += p:
#     print("Added!")
# else:
#     print("Failed")
# c = Client("59769", "HEN", "CHENHEN", "AMIL ZULA", "0506565654", "f")
# if s.add_client(c):
#     print("Added!")
# else:
#     print("Failed")
# s.print_products()
# if s.remove_product(5555):
#     print("Removed!")
# else:
#     print("Failed to remove")
# lst = s.get_all_by_brand("Lenovo")
# for item in lst:
#     print(item)
# lst = s.get_all_by_price_number(700)
# for item in lst:
#     print(item)
# print(s.get_most_expensive_product())
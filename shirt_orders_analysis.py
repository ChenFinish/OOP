import numpy as np
from superstore import *
import csv
import matplotlib.pyplot as plt


class analysis():
    orders = np.genfromtxt("orders.csv", delimiter=',', skip_header=True, dtype = "int32")
    clients = np.genfromtxt("clients.csv", delimiter=',', skip_header=True, dtype=str, usecols=(0, 1))
    payment = np.zeros(shape=(len(orders), 1), dtype="int32")

    S = superstore("products_supply.csv", "clients.csv", "shirts.csv", "orders.csv")

    i = 0
    for order in orders:

        price=0
        quantity = int(order[3])
        id = int(order[2])
        with open('shirts.csv') as b:
            lines = csv.reader(b)
            next(lines)
            for row in lines:
                if int(id) == int(row[0]):
                    price = int(row[2])
        final = quantity * price

        payment[i][0] = final
        i = i+1

    orders = np.append(orders,payment, axis=1)







    max_order=orders[0]

    for order in orders:
        if int(order[4])>int(max_order[4]):
            max_order=order


    print(S.get_client(int(max_order[1])))




    count=0
    sum=0
    clientName=""


    clientID=int(input("enter client id:"))
    client = S.get_client(clientID)

    try:
        if client is None:
            raise ClientNotFoundError
        else:
            for order in orders:
                if int(order[1])==clientID:
                    count=count+1
                    sum=sum+int(order[4])

            for client in clients:
                if int(client[0])==clientID:
                    print(client[1])
                    clientName=client[1]

            print(f"Client Name: {clientName}, Amount of orders: {count}, Total pay: {sum}")

    except ClientNotFoundError:
        print("\n##########\nClientNotFoundError\n##########\n")


    average=0
    sum=0
    count=0

    for order in orders:
        count=count+1
        sum=sum+order[4]

    average=sum/count

    for order in orders:
        if order[4]>average:
            print(order[0],order[1],order[2],order[3])


    # clients_dict = dict()
    # for order in orders:
    #     if order[1] not in clients_dict.keys():
    #         clients_dict[int(order[1])] = amount_orders = np.count_nonzero(orders == order[1])
    # print(clients_dict)
    #
    # names = [S.get_client(key) for key in clients_dict.keys()]
    # fig = plt.figure(figsize=(10, 7))
    # plt.bar(names, clients_dict.values())
    # plt.title("Clients")
    # plt.ylabel("Orders Count")
    # plt.xlabel("Names")
    # values=clients_dict.values()
    #
    # plt.show()



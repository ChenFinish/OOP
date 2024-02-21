class Product:
    def __init__(self, product_id, brand, model, year, price):
        self.product_id = int(product_id)
        self.brand = brand
        self.model = model
        self.year = int(year)
        self.price = int(price)

    def __str__(self):
        return f'{self.product_id}, {self.brand}, {self.model}, {self.year}, {self.price}'

    def print_me(self):
        print(f'----{self.product_id}----\nbrand:{self.brand}\nmodel:{self.model}\nyear:{self.year}\nprice:{self.price}')

    def __repr__(self):
        return self

    def Is_popular(self):
        if self.year > 2017 and self.price <= 3000:
            return True
        return False
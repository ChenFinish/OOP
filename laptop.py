from Product import *

class laptop(Product):
    def __init__(self,product_id, brand, model, year, price, CPU, hard_disk, screen):
        super().__init__(product_id, brand, model, year, price)
        self.CPU = CPU
        self.hard_disk = hard_disk + "GB"
        self.screen = int(screen)

    def print_me(self):
        super().print_me()
        print(f"CPU:{self.CPU}\nhard_disc:{self.hard_disk}\nscreen:{self.screen}")

    def __str__(self):
        return f"{super().__str__()},{self.CPU},{self.hard_disk},{self.screen}"

    def __repr__(self):
        return str(self)



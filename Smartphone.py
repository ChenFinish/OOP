from Product import *

class SmartPhone(Product):
    def __init__(self, product_id, brand, model, year, price, cell_net, num_cores, cam_res):
        super().__init__(product_id, brand, model, year, price)
        self.cell_net = cell_net
        self.num_cores = num_cores
        self.cam_res = cam_res + "MP"

    def print_me(self):
        super().print_me()
        print(f"cell_net:{self.cell_net}\nnum_cores:{self.num_cores}\ncam_res:{self.cam_res}")

    def __str__(self):
        return f"{super().__str__()},{self.cam_res},{self.num_cores},{self.cam_res}"
    def __repr__(self):
        return str(self)
class Client:
    def __init__(self, client_id, name, email, address, phone_number, gender):
        self.client_id = int(client_id)
        self.name = name
        self.email = email
        self.address = address
        self.phone_number = phone_number
        if gender.upper() != 'F' or gender.upper() != 'M':
            gender = 'F'
        self.gender = gender

    def __str__(self):
        return f'{self.client_id}, {self.name}, {self.email}, {self.address}, {self.phone_number}, {self.gender}'

    def print_me(self):
        print(f'----{self.client_id}----\nname:{self.name}\nemail: {self.email}\naddress: {self.address}\nphone number: {self.phone_number}\ngrnder:{self.gender}')

    def __repr__(self):
        return self

# p3 = client("123", "HEN", "CHENHEN", "AMIL ZULA", "0506565654", "f")
# p3.print_me()
# print(p3)
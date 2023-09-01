import csv
from pprint import pprint
from abc import ABC, abstractmethod


def read_csv(file):
    with open("sample.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            pprint(row)

def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None

def add_cupcake_dictionary(file, cupcake):
    fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]

    with open(file, "a", newline="\n") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)

class Cupcake(ABC):
    size = "regular"
    def __init__(self, name, price, flavor, frosting, filling,):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []
        
    
    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)
    
    @abstractmethod
    def calculate_price(self, quantity):
        return quantity * self.price
        
class Mini(Cupcake):
    size = "mini"
    
    def calculate_price(self, quantity):
        return quantity * self.price * 0.50
    
class Regular(Cupcake):
    size = "regular"
    
    def calculate_price(self, quantity):
        return quantity * self.price
    
class Large(Cupcake):
    size = "large"
    
    def calculate_price(self, quantity):
        return quantity * self.price * 1.34
        

def add_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if hasattr(cupcake, "filling"):
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles, "filling": cupcake.filling})
        else:
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})

#cupcake list
cupcake_1 = Regular("stars and stripes", 2.99, "vanilla", "vanilla", "chocolate")
cupcake_1.add_sprinkles("red", "white", "Blue")
cupcake_2 = Mini("Oreo", 1.50, "chocolate", "Cookies and Cream", "vanilla")
cupcake_2.add_sprinkles("Oreo crumbs")
cupcake_3 = Large("Red Velvet", 3.99, "Red Velvet", "Cream Cheese", None)

# Added cupcake
cupcake_4 = Mini("Vanilla", 1.50, "Vanilla", "chocolate", None,)
cupcake_list = [
    cupcake_1,
    cupcake_2,
    cupcake_3
]


def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles, "filling": cupcake.filling})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})

write_new_csv("sample.csv", cupcake_list)


def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader
    
def get_cupcake_order():
    cupcakes = []

    with open('orders.csv', 'r',) as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            cupcakes.append(row)

    return cupcakes


add_cupcake("sample.csv", cupcake_4)
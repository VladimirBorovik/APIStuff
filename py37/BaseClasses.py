from enum import Enum
from abc import ABCMeta, abstractmethod


class ProductType(Enum):
    """Class which describes product types. It presents as enumeration member.
       If it necessary you can add unique enumeration member."""

    BREAD = "Simple bread"
    VEGETABLES = "Potato"
    FRUIT = "Orange"
    MEAT = "Beef meat"

    def __str__(self):
        return "{0}".format(self.value)

    @staticmethod
    def info():
        for e in ProductType:
            print("{0} - {1}".format(e.name, e.value))


class Food(metaclass=ABCMeta):
    """Abstract class which set ups inheritance and behavioral models for program."""

    @abstractmethod
    def product_type(self):
        raise NotImplementedError()

    @abstractmethod
    def product_type(self):
        raise NotImplementedError()

    @abstractmethod
    def product_name(self):
        raise NotImplementedError()

    @abstractmethod
    def product_price(self):
        raise NotImplementedError()

    @abstractmethod
    def product_weight(self):
        raise NotImplementedError()


class Product(Food):
    """Inherited class for product. Additional information for product."""

    def __init__(self, product_type: str, name: str, price: float, weight: int):
        self.__product_type = product_type
        self.__product_name = name
        self.__product_price = price
        self.__product_weight = weight

    @property
    def product_type(self):
        return self.__product_type

    @property
    def product_name(self):
        return self.__product_name

    @property
    def product_price(self):
        return self.__product_price

    @property
    def product_weight(self):
        return self.__product_weight

    @product_type.setter
    def product_type(self, value: str) -> str:
        if isinstance(value, str):
            self.__product_type = value
        else:
            raise ValueError("Wrong value type!")

    @product_name.setter
    def product_name(self, value: str) -> str:
        if isinstance(value, str):
            self.__product_name = value
        else:
            raise ValueError("Wrong value type!")

    @product_price.setter
    def product_price(self, value: float) -> float:
        if isinstance(value, float):
            self.__product_price = value
        else:
            raise ValueError("Wrong value type!")

    @product_weight.setter
    def product_weight(self, value: int) -> int:
        if isinstance(value, int):
            self.__product_weight = value
        else:
            raise ValueError("Wrong value type!")

    def __str__(self):
        return "Product type: |{0}| - " \
               "Name: |{1}| - " \
               "Price: |{2}| - " \
               "Weight: |{3}|".format(self.product_type, self.product_name, self.product_price, self.product_weight)

    def get_attribute_info(self, attr):
        if attr == "_Product__product_name":
            return "-- Product name: |{0}| --".format(self.__dict__[attr])
        if attr == "_Product__product_price":
            return "-- Product price: |{0}| --".format(self.__dict__[attr])
        if attr == "_Product__product_weight":
            return "-- Product weight: |{0}| --".format(self.__dict__[attr])

    def price(self):
        return self.product_price

    def weight(self):
        return self.product_weight


class Buy(Product):
    """Presents list of products, which includes to buy. Hab for products.
       Inherited from class Product"""

    # Container for list of products.
    __list_of_products = []

    def __init__(self, name, obj):
        self.__name = name
        self.__list_of_products.append(obj)

    @property
    def name(self):
        return self.__name

    @staticmethod
    def add_for_cart(obj):
        Buy.__list_of_products.append(obj)

    @staticmethod
    def drop_from_cart(obj):
        Buy.__list_of_products.remove(obj)

    def count_of_items(self):
        print("Count of products is: " + str(len(self.__list_of_products)))

    def main_info(self):
        print(self.name)
        for item in range(len(Buy.__list_of_products)):
            print(Buy.__list_of_products[item])

    @staticmethod
    def total_price():
        total_price = 0.0
        for item in range(len(Buy.__list_of_products)):
            if isinstance(Buy.__list_of_products[item], Product):
                total_price += float(Buy.__list_of_products[item].price())
        print("Total price is: " + str(total_price))

    @staticmethod
    def total_weight():
        total_weight = 0
        for item in range(len(Buy.__list_of_products)):
            if isinstance(Buy.__list_of_products[item], Product):
                total_weight += int(Buy.__list_of_products[item].weight())
        print("Total weight is: " + str(total_weight))

    def __str__(self):
        return "{0}".format(self.name)

    def __getitem__(self, index):
        if isinstance(index, tuple):
            return [self.__list_of_products[i] for i in index]
        elif index == Ellipsis:
            return self.__list_of_productsl.copy()
        return self.__list_of_products[index]


class Check(Buy):
    """Presents info about buy product list.
       Inherited from class Buy"""

    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str) -> str:
        if isinstance(value, str):
            self.__name = value
        else:
            raise ValueError("Wrong value type!")

    def __str__(self):
        return "{0}".format(self.name)

    def check_info(self, obj):
        print("\n")
        print(self.name)
        Buy.main_info(obj)

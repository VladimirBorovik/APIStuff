from BaseClasses import ProductType, Product, Buy, Check

if __name__ == '__main__':
    p1 = Product(ProductType.MEAT, "Product_1", 200.0, 150)
    p2 = Product(ProductType.VEGETABLES, "Product_2", 50.0, 500)
    p3 = Product(ProductType.BREAD, "Product_3", 20.0, 400)
    print(p1)

    b = Buy("Buy_1", p1)
    b.add_for_cart(p2)
    b.add_for_cart(p3)

    b.count_of_items()

    b.total_price()
    b.total_weight()

    # b.drop_from_cart(p1)
    # b.count_of_items()

    b.total_price()
    b.total_weight()

    ch = Check("Vapiano: order for table number #42")
    ch.check_info(b)

    ProductType.info()

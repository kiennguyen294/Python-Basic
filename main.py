# persion = input("what your name?")
# print (persion)

# radius = int(input("Enter the radius of a circle"))
# area_of_a_circle = 3.14*radius*radius
# circumference_of_circle = 2*3.14*radius
#
# print(f"Area = {area_of_a_circle} and Circumference = {circumference_of_circle}")

def apply_discount(product, discount):
    price = int(product['price'] * (1-discount))
    assert (1 == 2, 'this should fail')
    assert 0 <= price < product['price']
    return price

shoes = {'name': 'Fancy Shoes', 'price': 14900}

if __name__ == '__main__':
    print(apply_discount(shoes, 0.3))
# persion = input("what your name?")
# print (persion)

# radius = int(input("Enter the radius of a circle"))
# area_of_a_circle = 3.14*radius*radius
# circumference_of_circle = 2*3.14*radius
#
# print(f"Area = {area_of_a_circle} and Circumference = {circumference_of_circle}")

# with open('/home/kiennn/example.txt', 'a') as file_handler:
#     file_handler.write('Here is some more text')
# def apply_discount(product, discount):
#     price = int(product['price'] * (1-discount))
#     assert (1 == 2, 'this should fail')
#     assert 0 <= price < product['price']
#     return price
#
# shoes = {'name': 'Fancy Shoes', 'price': 14900}
#
# if __name__ == '__main__':
#     print(apply_discount(shoes, 0.3))

#
# data = [['ABC', 'DEF', 'XYZ'], [20,26,19], ['ABC.com', 'DEF.com', 'XYZ.com']]
# name,age,email = data
# for name, age in data:
#     print(name)
#     print(age)

# data = [{1,2,3}, {4,5,6}, {7,8,9}]
# name,age,email = data

def log(number):
    print(f'Processing {number}')
    print(f'Adding 2 to number: {number + 2}')


def looper(number):
    for i in range(number):
        log(i)


if __name__=='__main__':
    looper(5)
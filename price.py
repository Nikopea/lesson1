# def discounted(price, discount):
#     price = abs(price)
#     discount = abs(discount)
#     if discount >= 100:
#         price_with_discount = price
#     else:
#         price_with_discount = price - (price * discount / 100)
#     return price_with_discount

# product = {'name': 'Samsung Galaxy S21', 'price': 50000.0, 'discount': 5}
# product['with_discount'] = discounted(product['price'], product['discount'])
# print(product)

# def get_summ(one, two, delimiter='&'):
#     words_summ = f'{one}{delimiter}{two}'.upper()
#     return words_summ

# a = get_summ(1.0, 'python')
# print(a)

def format_price(price):
    price = int(price)
    return f"Цена: {price} руб."
price_2 = format_price(56.24)
print(price_2)

print('Hello world')
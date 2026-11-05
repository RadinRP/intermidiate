product = {
    "name" : "laptop",
    "price" : 5000000,
    "stock" : 6
}
print(product["price"])

if (product["stock"] > 0):
    print("available")
else:
    print("unavailable")

for i in range (product["stock"]):
    product["stock"] -= 1

product["price"] *=1.1
print(product["price"])

print(product)

for i in product:
    print(product[i])

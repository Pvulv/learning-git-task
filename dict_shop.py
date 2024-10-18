shops = {
    "piekarnia" : ["chleb", "bułki", "pączek"],
    "warzywniak" : ["marchew", "seler", "rukolę"]
}
print("Lista zakupów")
for shop, products in shops.items():
    capitalized_products = [product.capitalize() for product in products]
    print("idę do", shop.capitalize(), "i kupuję", capitalized_products)

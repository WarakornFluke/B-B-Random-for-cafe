import random

bakery = ["Cheese bread","Glazzed Donut","Chicken pie","Chocolate Croissant	","Blueberry Scone","Salted Caramel Tart ","Banana Nut Bread	","Iced Lemon Pound Cake","Cheese Danish","Butter Croissant	","Chocolate Chip Cookie"]
drink_beverage= ["Ice Latte","Espresso","Hot milk","Iced Tea","Caramel Flan Latte","Caramel Macchiato","Caffe Mocha","White Chocolate Mocha","Freshly Brewed Coffee","Caramel Frappuccino","Iced Peach Green Tea Lemonade"]
price_bakery = 120
price_beverage = 80
print("Welcome to Bakery and Beverage random machine")
print("Option 0 = Only beverage / Option 1 = Only bakery / Option 2 = Bakery and beverage " )
print("Please select options 0, 1 or 2 (Special discount 10% for option 2)")
def random_some_bakery():
  return int(random.random() * 10)

while True:
  n = int(input(" Choose option : ")) 
  if n == 2:
    print("You have choose option 2 [Bakery and beverage]")       
    print("Random of bakery = ",bakery[random_some_bakery()])
    print("Random of beverage =",drink_beverage [random_some_bakery()])
    print("Total payment : ", int((price_bakery + price_beverage) * (100 - 10) / 100))
    break
  elif n == 1:
    print("You have choose option 1 [Only bakery] ")       
    print("Random of bakery = ",bakery[random_some_bakery()])
    print("Price for bakery = ", int(price_bakery))
    break
  elif n == 0:
    print("You have choose option 0 [Only beverage] ")       
    print("Random of beverage = ",drink_beverage [random_some_bakery()])
    print("Price for beverage = ", int(price_beverage))
    break
  else:
    print("Option Error please choose again")
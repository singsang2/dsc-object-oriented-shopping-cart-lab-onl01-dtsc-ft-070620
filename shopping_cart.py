class ShoppingCart:
    # write your code here
   def __init__(self, emp_discount=None):
      self.total = 0
      self.items = []
      self.employee_discount = emp_discount

   def add_item(self, name, price, quantity=1):
      # exist = False
      # for idx, item in enumerate(self.items):
      #    if item['name'] == name:
      #       exist = idx
      # if exist:
      #    self.items[idx]['quantity'] += quantity
      # else:
      self.items.append({'name': name, 'price': price, 'quantity': quantity})
      self.total += price * quantity
      return self.total

   def mean_item_price(self):
      sum_unit_price = 0
      item_num = 0
      for item in self.items:
         sum_unit_price += item['price']*item['quantity']
         item_num += item['quantity']
      return round(sum_unit_price/item_num,2)

   def median_item_price(self):
      price_list = []
      for item in self.items:
         price_list += [item['price']] * item['quantity']
      
      if len(price_list)%2 == 0:
         first = price_list[int(len(price_list)/2)]-1
         second = price_list[int(len(price_list)/2)]
         return round((first + second)/2,2)
      else: 
         return round(price_list[int((len(price_list)-1)/2)], 2)

   def apply_discount(self):
      if self.employee_discount:
         return self.total*(100-self.employee_discount)/100
      else:
         print("Sorry, there is no discount to apply to your cart :(")

   def void_last_item(self):
      print(len(self.items))
      if len(self.items)>0:
         last_item = self.items[-1]
         if last_item['quantity'] > 1:
            self.items[-1]['quantity'] -= 1
         else:
            self.items.pop()
         self.total -= last_item['price']
      else:
         print("There are no items in your cart!")
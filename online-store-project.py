####   online store

class Product:
    def __init__(self,name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
 
    
    def update_details(self,updated_name,updated_price,updated_quantity):
        self.name=updated_name
        self.price=updated_price
        self.quantity=updated_quantity



    def check_availiblity(self):
        if self.quantity>0:
            return True
        
        


    



class Electronics(Product):
    def __init__(self, name, price, quantity,warranty):
        super().__init__(name, price, quantity)
        self.warranty=warranty
        # self.rating=rating
    
    def update_details(self, updated_name, updated_price, updated_quantity,updated_warrenty):
        super().update_details(updated_name, updated_price, updated_quantity)
        self.warranty=updated_warrenty
    

class Clothing(Product):
    def __init__(self, name, price, quantity,size,brand):
        super().__init__(name, price, quantity)
        self.size=size
        self.brand=brand
        
    def update_details(self, updated_name, updated_price, updated_quantity,updated_size,updated_brand):
        super().update_details(updated_name, updated_price, updated_quantity)
        self.size=updated_size
        self.brand=updated_brand


class Customer:
    def __init__(self,name, email,address):
        self.name=name
        self.email=email
        self.address=address
    #adding func
    def adding_details(self,*added):
        for i in added:
            self.new_value=i

    def updated_details(self,new_name,new_email,new_address):
        self.name=new_name
        self.email=new_email
        self.address=new_address



class RegularCustomer(Customer):
    def __init__(self, name, email, address,regular_point):
        super().__init__(name, email, address)
        self.regular_point=regular_point

    def updated_details(self, new_name, new_email, new_address,new_regular_point):
        super().updated_details(new_name, new_email, new_address)
        self.regular_point=new_regular_point


class VIPCustomer(Customer):
    def __init__(self, name, email, address,vip_id):
        super().__init__(name, email, address)
        self.vip_id=vip_id

    def updated_details(self, new_name, new_email, new_address,new_vip_id):
        super().updated_details(new_name, new_email, new_address)
        self.vip_id=new_vip_id


class Order:
    def __init__(self,order_id,date):
        self.order_id=order_id
        self.date=date
        self.status="Pending"

    def add_order(self,product,customer,quantity):
        self.status="product is added in Order list."
        print(self.status)
        print(f"The product of name:{product.name} with quantity:{quantity} is been ordered by the customer-{customer.name}")

    def  removing_order(self,product,customer,quantity):
        self.status="product is removed from order list."
        print(self.status)
        print(f"The product of name:{product.name} of quantity:{quantity} is been cancelled!!! by the customer-{customer.name}")

    def order_price(self,product,quantity):
        if quantity<product.quantity:
            v=(product.price+(product.price*18/100))*quantity
            print(f"the final price (GST) of product:{product.name} of quantity:{quantity} including is :{v}")
        else:
            print("the quantity of product is out of range")
    
    def place_order(self,product,customer,quantity):
        self.quantity=quantity
        print(f"customer:{customer.name} with Email:{customer.email}")
        print(f"order a product:{product.name} of quantity:{quantity}form shopping cart")




class ShoppingCart:
    def __init__(self):
        self.product_list=[]

    def adding(self,product):
        if product not in self.product_list:
            self.product_list.append(product)
            print(f"the product name:{product.name} ,item:{product.quantity} is adding in shopping cart")
        else:
            print(f"the product name:{product.name} already in shopping cart")

    def removing(self,product):
        found=[i for i in self.product_list if i.name==product.name]
        if found:
            self.product_list.remove(product)
            print(f"the product name:{product.name} is removed from shopping cart")
        else:
            print(f"the product is not found")



p1=Product("Shirt",400,1)
p2=Product("T-shirt",500,4)
p3=Product("Jeans",860,3)
p4=Product("watch",1100,1)


s=ShoppingCart()
s.adding(p1)
s.adding(p2)
s.adding(p3)
s.adding(p3)
s.adding(p3)
print('-------'*30)
s.removing(p3)
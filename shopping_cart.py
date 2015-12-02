import datetime

products={

    1:["Shirt",920],
    2:["Jeans",2550],
    3:["Trouser",1299],
    4:["Hat",199],
    5:["T-Shirt",299]
}

def timeStamped(fmt='   Date :%Y-%m-%d   Time :%H-%M-%S'):
    return datetime.datetime.now().strftime(fmt)



class Item(object):
    def __init__(self, unq_id, name, price, qty):
        self.unq_id = unq_id
        self.product_name = name
        self.price = price
        self.qty = qty



class Cart(object):
    def __init__(self):
        self.content = dict()

    def update(self, item):
        if item.unq_id not in self.content:
            self.content.update({item.unq_id: item})
            return

    def get_total(self):
        return sum([v.price * v.qty for _, v in self.content.iteritems()])

    def get_num_items(self):
        return sum([v.qty for _, v in self.content.iteritems()])

    def remove_item(self, key):
        self.content.pop(key)

    def show_menu(self):
    		print "****MENU****" \
                  "  1.Show Products" \
                  "  2.Add in Cart" \
                  "  3.Place Order" \
                  "  4.Check cart"
   		return input("Please make a selection: ")


if __name__ == '__main__':
    cart = Cart()
    running = 1

    while running:
    	selection = cart.show_menu()
        if selection == 1:

            print "{:<8} {:<15} {:<10}".format('ID','Product','Price')
            for k, v in products.iteritems():
                 label, num=v
                 print "{:<8} {:<15} {:<10}".format(k, label, num)

        elif selection==2:
            ch=raw_input("Enter the ID:")
            qty=input("Enter Quantity")



            for k,v in products.iteritems():
                if k==int(ch):
                    name,price=v
                    item=Item(ch,name,price,qty)
                    cart.update(item)

        elif selection==3:
            if cart.get_num_items()==0:
                print "select a product first"
                continue


            cust_name=raw_input("Enter Your Name")
            cust_address=raw_input("Enter your Address")
            cust_mob=raw_input("Enter your mobile no.")
            with open("orders.txt", "a") as myfile:
                t=timeStamped()
                total=str(cart.get_total())
                myfile.write("\n")
                myfile.write(" %s"%cust_name)

                myfile.write(" %s"%cust_address)

                myfile.write(" %s"%cust_mob)

                myfile.write("   %s"%total)
                myfile.write(t)
                print"******* Bill *******"
                print "{0}   {1}   {2}".format(cust_name,cust_address,cust_mob)
                print "{:<8} {:<15} {:<10} {:<10}".format('ID','Product','Price','Qty')
                for k,v in cart.content.iteritems():
                     print "{:<8} {:<15} {:<10} {:<10}".format(k, v.product_name, v.price,v.qty)
                print "Total:%s rs"%cart.get_total()



                break

        else:

            if cart.get_num_items()==0:
                print "Your Cart is Empty"
                continue

            else:

                print "You have %i items in your cart for a total of %.02f .rs" % (cart.get_num_items(), cart.get_total())
                print "{:<8} {:<15} {:<10} {:<10}".format('ID','Product','Price','Qty')
                for k,v in cart.content.iteritems():
                     print "{:<8} {:<15} {:<10} {:<10}".format(k, v.product_name, v.price,v.qty)




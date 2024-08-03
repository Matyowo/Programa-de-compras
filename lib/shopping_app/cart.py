from ownable import Ownable
from item_manager import show_items

class Cart(Ownable):
    
    def __init__(self, owner):
        super().__init__()  
        self.set_owner(owner)  
        self.items = []  

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        return sum(item.price for item in self.items)

    def check_out(self):
        total = self.total_amount()

        if self.owner.wallet.balance < total:
            print("Saldo insuficiente en la billetera del propietario del carrito.")
            return

        for item in self.items:
            item.owner.wallet.deposit(item.price)
            item.owner = self.owner  

        self.owner.wallet.withdraw(total)  

        self.items = [] 

        print("Compra realizada exitosamente.")
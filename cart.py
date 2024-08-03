from ownable import Ownable
from item_manager import show_items

class Cart(Ownable):
    
    def __init__(self, owner):
        super().__init__()  # Llama al constructor de Ownable
        self.set_owner(owner)  # Asigna el propietario al carrito
        self.items = []  # Inicializa la lista de artículos en el carrito

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
            item.owner.wallet.deposit(item.price)  # Transfiere el precio del artículo a la billetera del propietario del artículo
            item.owner = self.owner  # Transfiere la propiedad del artículo al propietario del carrito

        self.owner.wallet.withdraw(total)  # Deduce el monto total de la billetera del comprador

        self.items = []  # Vacía el carrito después de la compra

        print("Compra realizada exitosamente.")
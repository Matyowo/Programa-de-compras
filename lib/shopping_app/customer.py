from user import User
from cart import Cart
from ownable import Ownable


class Customer(User):

    def __init__(self, name):
        super().__init__(name)
        self.cart = Cart(self)  # Asigna un carrito al cliente y lo establece como su propietario.

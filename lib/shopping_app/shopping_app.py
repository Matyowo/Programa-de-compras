from customer import Customer
from item import Item
from seller import Seller

vendedor = Seller("DIC Store")
for i in range(10):
    Item("CPU", 40830, vendedor)
    Item("Memoria", 13880, vendedor)
    Item("Placa base", 28980, vendedor)
    Item("Fuente de alimentación", 8980, vendedor)
    Item("Caja para PC", 8727, vendedor)
    Item("HDD de 3.5 pulgadas", 10980, vendedor)
    Item("SSD de 2.5 pulgadas", 13370, vendedor)
    Item("SSD M.2", 12980, vendedor)
    Item("Refrigerador de CPU", 13400, vendedor)
    Item("Tarjeta gráfica", 23800, vendedor)

print("🤖 Por favor, dime tu nombre")
cliente = Customer(input())

print("🏧 Por favor, ingresa la cantidad a cargar en la billetera")
cliente.wallet.deposit(int(input()))

print("🛍️ Comenzando las compras")
fin_compras = False
while not fin_compras:
    print("📜 Lista de productos")
    vendedor.show_items()

    print("⛏ Por favor, ingresa el número del producto")
    numero = int(input())

    print("⛏ Por favor, ingresa la cantidad del producto")
    cantidad = int(input())

    items = vendedor.pick_items(numero, cantidad)
    for item in items:
        cliente.cart.add(item)
    print("🛒 Contenido del carrito")
    cliente.cart.show_items()
    print(f"🤑 Importe total: {cliente.cart.total_amount()}")

    print("😭 ¿Quieres finalizar las compras? (sí/no)")
    fin_compras = input() == "si"

print("💸 ¿Quieres confirmar la compra? (sí/no)")
if input() == "si":
    vendedor.wallet.deposit(cliente.cart.total_amount())
    

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈Resultado┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"🛍️ Posesiones de {cliente.name}")
cliente.show_items()
print(f"😱👛 Saldo de la billetera de {cliente.name}: {cliente.wallet.balance}")

print(f"📦 Estado del inventario de {vendedor.name}")
vendedor.show_items()
print(f"😻👛 Saldo de la billetera de {vendedor.name}: {vendedor.wallet.balance}")

print("🛒 Contenido del carrito")
cliente.cart.show_items()
print(f"🌚 Importe total: {cliente.cart.total_amount()}")

print("🎉 Fin")

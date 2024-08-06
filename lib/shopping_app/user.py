from wallet import Wallet

class User:
    from item_manager import show_items, items_list, pick_items, show_items

    def __init__(self, name):
        self.name = name
        self.wallet = Wallet(self)   # UserインスタンスまたはUserを継承したクラスのインスタンスは生成されると、自身をオーナーとするウォレットを持ちます。

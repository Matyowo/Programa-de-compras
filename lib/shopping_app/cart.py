class Cart:
    from item_manager import show_items

    def __init__(self, owner):
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            pass    # check_outメソッドをコーディングする際はpassは削除してください。
        # 要件
        #   - カートの中身（Cart#items）のすべてのアイテムの購入金額が、カートのオーナーのウォレットからアイテムのオーナーのウォレットに移されること。
        #   - カートの中身（Cart#items）のすべてのアイテムのオーナー権限が、カートのオーナーに移されること。
        #   - カートの中身（Cart#items）が空になること。
        # ヒント
        #   - カートのオーナーのウォレット ==> self.owner.wallet
        #   - アイテムのオーナーのウォレット ==> item.owner.wallet
        #   - お金が移されるということ ==> (？)のウォレットからその分を引き出して、(？)のウォレットにその分を入金するということ
        #   - アイテムのオーナー権限がカートのオーナーに移されること ==> オーナーの書き換え（item.owner = ?）
# Classes had to be moved to question_b folder because imports were not working from here
class StockPurchase:

    def __init__(self, symbol, date, shares, price):
        self.__symbol = symbol
        self.__date = date
        self.__shares = shares
        self.__price = price

    def get_symbol(self):
        return self.__symbol

    def get_date(self):
        return self.__date

    def get_shares(self):
        return self.__shares

    def get_price(self):
        return self.__price

    def get_purchase_price(self):
        self.purchase_price = self.__shares*self.__price
        return self.purchase_price

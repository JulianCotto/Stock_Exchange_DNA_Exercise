def get_stock_list():
    with open('stocklist.txt') as f:
        stock_dictionary = dict(i.rstrip().split(None, 1) for i in f)
    return stock_dictionary


def get_stock_purchases():
    ifile = open("stockpurchases.txt", "r")
    lines = ifile.readlines()
    get_stock_purchases_list = [(line.strip().split()) for line in lines]
    return get_stock_purchases_list


def stock_purchase_history(stock_dictionary, stock_purchases_list):
    i = stock_dictionary
    comp0 = i["AAPL"]
    symbol0 = [key for key in i.keys()][0]
    ob0 = Stock(comp0, symbol0)
    comp1 = i["CAT"]
    symbol1 = [key for key in i.keys()][1]
    ob1 = Stock(comp1, symbol1)
    comp2 = i["EK"]
    symbol2 = [key for key in i.keys()][2]
    ob2 = Stock(comp2, symbol2)
    comp3 = i["GOOG"]
    symbol3 = [key for key in i.keys()][3]
    ob3 = Stock(comp3, symbol3)
    comp4 = i["MSFT"]
    symbol4 = [key for key in i.keys()][4]
    ob4 = Stock(comp4, symbol4)

    g = stock_purchases_list
    symb0 = g[0][0]
    date0 = g[0][1]
    shar0 = g[0][2]
    pric0 = g[0][3]
    symb1 = g[1][0]
    date1 = g[1][1]
    shar1 = g[1][2]
    pric1 = g[1][3]
    symb2 = g[2][0]
    date2 = g[2][1]
    shar2 = g[2][2]
    pric2 = g[2][3]
    symb3 = g[3][0]
    date3 = g[3][1]
    shar3 = g[3][2]
    pric3 = g[3][3]
    symb4 = g[4][0]
    date4 = g[4][1]
    shar4 = g[4][2]
    pric4 = g[4][3]
    symb5 = g[5][0]
    date5 = g[5][1]
    shar5 = g[5][2]
    pric5 = g[5][3]
    symb6 = g[6][0]
    date6 = g[6][1]
    shar6 = g[6][2]
    pric6 = g[6][3]
    symb7 = g[7][0]
    date7 = g[7][1]
    shar7 = g[7][2]
    pric7 = g[7][3]
    symb8 = g[8][0]
    date8 = g[8][1]
    shar8 = g[8][2]
    pric8 = g[8][3]
    symb9 = g[9][0]
    date9 = g[9][1]
    shar9 = g[9][2]
    pric9 = g[9][3]
    symb10 = g[10][0]
    date10 = g[10][1]
    shar10 = g[10][2]
    pric10 = g[10][3]
    symb11 = g[11][0]
    date11 = g[11][1]
    shar11 = g[11][2]
    pric11 = g[11][3]
    symb12 = g[12][0]
    date12 = g[12][1]
    shar12 = g[12][2]
    pric12 = g[12][3]
    symb13 = g[13][0]
    date13 = g[13][1]
    shar13 = g[13][2]
    pric13 = g[13][3]
    symb14 = g[14][0]
    date14 = g[14][1]
    shar14 = g[14][2]
    pric14 = g[14][3]
    obj0 = StockPurchase(symb0, date0, shar0, pric0)
    obj1 = StockPurchase(symb1, date1, shar1, pric1)
    obj2 = StockPurchase(symb2, date2, shar2, pric2)
    obj3 = StockPurchase(symb3, date3, shar3, pric3)
    obj4 = StockPurchase(symb4, date4, shar4, pric4)
    obj5 = StockPurchase(symb5, date5, shar5, pric5)
    obj6 = StockPurchase(symb6, date6, shar6, pric6)
    obj7 = StockPurchase(symb7, date7, shar7, pric7)
    obj8 = StockPurchase(symb8, date8, shar8, pric8)
    obj9 = StockPurchase(symb9, date9, shar9, pric9)
    obj10 = StockPurchase(symb10, date10, shar10, pric10)
    obj11 = StockPurchase(symb11, date11, shar11, pric11)
    obj12 = StockPurchase(symb12, date12, shar12, pric12)
    obj13 = StockPurchase(symb13, date13, shar13, pric13)
    obj14 = StockPurchase(symb14, date14, shar14, pric14)

    print('\033[1m' + "Stock Purchase History Report" + '\033[0m')
    print("Company\tSymbol\t\tShares\tPrice\t\tPurchase Price")
    print(ob0.get_company_name(), "\t", ob0.get_symbol(), "\t", obj0.get_shares(), "\t",
          obj0.get_price(), "\t\t", obj0.get_purchase_price())

    print(ob0.get_company_name(), "\t", ob0.get_symbol(), "\t", obj1.get_shares(), "\t",
          obj1.get_price(), "\t\t", obj1.get_purchase_price())

    print(ob0.get_company_name(), "\t", ob0.get_symbol(), "\t", obj2.get_shares(), "\t",
          obj2.get_price(), "\t", obj2.get_purchase_price())

    print(ob1.get_company_name(), "\t", ob1.get_symbol(), "\t", obj3.get_shares(), "\t",
          obj3.get_price(), "\t", obj3.get_purchase_price())

    print(ob1.get_company_name(), "\t", ob1.get_symbol(), "\t", obj4.get_shares(), "\t",
          obj4.get_price(), "\t", obj4.get_purchase_price())

    print(ob1.get_company_name(), "\t", ob1.get_symbol(), "\t", obj5.get_shares(), "\t",
          obj5.get_price(), "\t", obj5.get_purchase_price())

    print(ob2.get_company_name(), "\t", ob2.get_symbol(), "\t", obj6.get_shares(), "\t",
          obj6.get_price(), "\t\t", obj6.get_purchase_price())

    print(ob2.get_company_name(), "\t", ob2.get_symbol(), "\t", obj7.get_shares(), "\t",
          obj7.get_price(), "\t\t", obj7.get_purchase_price())

    print(ob2.get_company_name(), "\t", ob2.get_symbol(), "\t", obj8.get_shares(), "\t",
          obj8.get_price(), "\t\t", obj8.get_purchase_price())

    print(ob3.get_company_name(), "\t", ob3.get_symbol(), "\t", obj9.get_shares(), "\t",
          obj9.get_price(), "\t", obj9.get_purchase_price())

    print(ob3.get_company_name(), "\t", ob3.get_symbol(), "\t", obj10.get_shares(), "\t",
          obj10.get_price(), "\t", obj10.get_purchase_price())

    print(ob3.get_company_name(), "\t", ob3.get_symbol(), "\t", obj11.get_shares(), "\t",
          obj11.get_price(), "\t", obj11.get_purchase_price())

    print(ob4.get_company_name(), "\t", ob4.get_symbol(), "\t", obj12.get_shares(), "\t",
          obj12.get_price(), "\t", obj12.get_purchase_price())

    print(ob4.get_company_name(), "\t", ob4.get_symbol(), "\t", obj13.get_shares(), "\t",
          obj13.get_price(), "\t", obj13.get_purchase_price())

    print(ob4.get_company_name(), "\t", ob4.get_symbol(), "\t", obj14.get_shares(), "\t",
          obj14.get_price(), "\t", obj14.get_purchase_price())


def company_purchase_history(stock_dictionary, stock_purchases_list):
    i = stock_dictionary
    comp0 = i["AAPL"]
    symbol0 = [key for key in i.keys()][0]
    ob0 = Stock(comp0, symbol0)
    comp1 = i["CAT"]
    symbol1 = [key for key in i.keys()][1]
    ob1 = Stock(comp1, symbol1)
    comp2 = i["EK"]
    symbol2 = [key for key in i.keys()][2]
    ob2 = Stock(comp2, symbol2)
    comp3 = i["GOOG"]
    symbol3 = [key for key in i.keys()][3]
    ob3 = Stock(comp3, symbol3)
    comp4 = i["MSFT"]
    symbol4 = [key for key in i.keys()][4]
    ob4 = Stock(comp4, symbol4)

    g = stock_purchases_list
    symb0 = g[0][0]
    date0 = g[0][1]
    shar0 = g[0][2]
    pric0 = g[0][3]
    symb1 = g[1][0]
    date1 = g[1][1]
    shar1 = g[1][2]
    pric1 = g[1][3]
    symb2 = g[2][0]
    date2 = g[2][1]
    shar2 = g[2][2]
    pric2 = g[2][3]
    symb3 = g[3][0]
    date3 = g[3][1]
    shar3 = g[3][2]
    pric3 = g[3][3]
    symb4 = g[4][0]
    date4 = g[4][1]
    shar4 = g[4][2]
    pric4 = g[4][3]
    symb5 = g[5][0]
    date5 = g[5][1]
    shar5 = g[5][2]
    pric5 = g[5][3]
    symb6 = g[6][0]
    date6 = g[6][1]
    shar6 = g[6][2]
    pric6 = g[6][3]
    symb7 = g[7][0]
    date7 = g[7][1]
    shar7 = g[7][2]
    pric7 = g[7][3]
    symb8 = g[8][0]
    date8 = g[8][1]
    shar8 = g[8][2]
    pric8 = g[8][3]
    symb9 = g[9][0]
    date9 = g[9][1]
    shar9 = g[9][2]
    pric9 = g[9][3]
    symb10 = g[10][0]
    date10 = g[10][1]
    shar10 = g[10][2]
    pric10 = g[10][3]
    symb11 = g[11][0]
    date11 = g[11][1]
    shar11 = g[11][2]
    pric11 = g[11][3]
    symb12 = g[12][0]
    date12 = g[12][1]
    shar12 = g[12][2]
    pric12 = g[12][3]
    symb13 = g[13][0]
    date13 = g[13][1]
    shar13 = g[13][2]
    pric13 = g[13][3]
    symb14 = g[14][0]
    date14 = g[14][1]
    shar14 = g[14][2]
    pric14 = g[14][3]
    obj0 = StockPurchase(symb0, date0, shar0, pric0)
    obj1 = StockPurchase(symb1, date1, shar1, pric1)
    obj2 = StockPurchase(symb2, date2, shar2, pric2)
    obj3 = StockPurchase(symb3, date3, shar3, pric3)
    obj4 = StockPurchase(symb4, date4, shar4, pric4)
    obj5 = StockPurchase(symb5, date5, shar5, pric5)
    obj6 = StockPurchase(symb6, date6, shar6, pric6)
    obj7 = StockPurchase(symb7, date7, shar7, pric7)
    obj8 = StockPurchase(symb8, date8, shar8, pric8)
    obj9 = StockPurchase(symb9, date9, shar9, pric9)
    obj10 = StockPurchase(symb10, date10, shar10, pric10)
    obj11 = StockPurchase(symb11, date11, shar11, pric11)
    obj12 = StockPurchase(symb12, date12, shar12, pric12)
    obj13 = StockPurchase(symb13, date13, shar13, pric13)
    obj14 = StockPurchase(symb14, date14, shar14, pric14)

    print(ob0.get_company_name(), ob0.get_symbol())
    print("Shares\tPrice\t\tPurchase Price")
    print(obj0.get_shares(), "\t", obj0.get_price(),
          "\t\t", obj0.get_purchase_price())
    print(obj1.get_shares(), "\t", obj1.get_price(),
          "\t\t", obj1.get_purchase_price())
    print(obj2.get_shares(), "\t", obj2.get_price(),
          "\t", obj2.get_purchase_price())
    print("______________________________________\n")
    print(ob1.get_company_name(), ob1.get_symbol())
    print("Shares\tPrice\t\tPurchase Price")
    print(obj3.get_shares(), "\t", obj3.get_price(),
          "\t", obj3.get_purchase_price())
    print(obj4.get_shares(), "\t", obj4.get_price(),
          "\t", obj4.get_purchase_price())
    print(obj5.get_shares(), "\t", obj5.get_price(),
          "\t", obj5.get_purchase_price())
    print("______________________________________\n")
    print(ob2.get_company_name(), ob2.get_symbol())
    print("Shares\tPrice\t\tPurchase Price")
    print(obj6.get_shares(), "\t", obj6.get_price(),
          "\t\t", obj6.get_purchase_price())
    print(obj7.get_shares(), "\t", obj7.get_price(),
          "\t\t", obj7.get_purchase_price())
    print(obj8.get_shares(), "\t", obj8.get_price(),
          "\t\t", obj8.get_purchase_price())
    print("______________________________________\n")
    print(ob3.get_company_name(), ob3.get_symbol())
    print("Shares\tPrice\t\tPurchase Price")
    print(obj9.get_shares(), "\t", obj9.get_price(),
          "\t", obj9.get_purchase_price())
    print(obj10.get_shares(), "\t", obj10.get_price(),
          "\t", obj10.get_purchase_price())
    print(obj11.get_shares(), "\t", obj11.get_price(),
          "\t", obj11.get_purchase_price())
    print("______________________________________\n")
    print(ob4.get_company_name(), ob4.get_symbol())
    print("Shares\tPrice\t\tPurchase Price")
    print(obj12.get_shares(), "\t", obj12.get_price(),
          "\t", obj12.get_purchase_price())
    print(obj13.get_shares(), "\t", obj13.get_price(),
          "\t", obj13.get_purchase_price())
    print(obj14.get_shares(), "\t", obj14.get_price(),
          "\t", obj14.get_purchase_price())
    print("______________________________________\n")


class Stock:

    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name


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
        self.purchase_price = int(self.__shares) * float(self.__price)
        return "{:.2f}".format(self.purchase_price)

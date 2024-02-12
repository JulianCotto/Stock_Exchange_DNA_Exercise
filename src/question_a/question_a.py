#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_stock_list():
    with open('stocklist.txt') as f:
        stock_dictionary = dict(i.rstrip().split(None, 1) for i in f)
        stock_dictionary
    return stock_dictionary 

def get_stock_purchases():
    ifile=open("stockpurchases.txt", "r")
    lines=ifile.readlines()
    stock_purchases_list=[tuple(line.strip().split()) for line in lines]
    return stock_purchases_list

def stock_purchase_history(stock_dictionary, stock_purchases_list):
    print('\033[1m' + "Stock Purchase History Report" + '\033[0m')
    print("Company\t\tSymbol\tShares\tPrice\t\tPurchase Price")
    print(stock_dictionary["AAPL"], "\t", stock_purchases_list[0][0], "\t", stock_purchases_list[0][2], "\t", stock_purchases_list[0][3], "\t\t", ("{:.2f}".format(int(stock_purchases_list[0][2]) * float(stock_purchases_list[0][3]))))

    print(stock_dictionary["AAPL"], "\t", stock_purchases_list[1][0], "\t", stock_purchases_list[1][2], "\t", stock_purchases_list[1][3], "\t\t", ("{:.2f}".format(int(stock_purchases_list[1][2]) * float(stock_purchases_list[1][3]))))

    print(stock_dictionary["AAPL"], "\t", stock_purchases_list[2][0], "\t", stock_purchases_list[2][2], "\t", stock_purchases_list[2][3],"\t", ("{:.2f}".format(int(stock_purchases_list[2][2]) * float(stock_purchases_list[2][3]))))

    print(stock_dictionary["CAT"], "\t", stock_purchases_list[3][0], "\t", stock_purchases_list[3][2], "\t", stock_purchases_list[3][3], "\t", ("{:.2f}".format(int(stock_purchases_list[3][2]) * float(stock_purchases_list[3][3]))))

    print(stock_dictionary["CAT"], "\t", stock_purchases_list[4][0], "\t", stock_purchases_list[4][2], "\t", stock_purchases_list[4][3], "\t", ("{:.2f}".format(int(stock_purchases_list[4][2]) * float(stock_purchases_list[4][3]))))

    print(stock_dictionary["CAT"], "\t", stock_purchases_list[5][0], "\t", stock_purchases_list[5][2], "\t", stock_purchases_list[5][3], "\t", ("{:.2f}".format(int(stock_purchases_list[5][2]) * float(stock_purchases_list[5][3]))))

    print(stock_dictionary["EK"], "\t", stock_purchases_list[6][0], "\t", stock_purchases_list[6][2], "\t", stock_purchases_list[6][3], "\t\t", ("{:.2f}".format(int(stock_purchases_list[6][2]) * float(stock_purchases_list[6][3]))))

    print(stock_dictionary["EK"], "\t", stock_purchases_list[7][0], "\t", stock_purchases_list[7][2], "\t", stock_purchases_list[7][3], "\t\t", ("{:.2f}".format(int(stock_purchases_list[7][2]) * float(stock_purchases_list[7][3]))))

    print(stock_dictionary["EK"], "\t", stock_purchases_list[8][0], "\t", stock_purchases_list[8][2], "\t", stock_purchases_list[8][3], "\t\t", ("{:.2f}".format(int(stock_purchases_list[8][2]) * float(stock_purchases_list[8][3]))))

    print(stock_dictionary["GOOG"], "\t\t", stock_purchases_list[9][0], "\t", stock_purchases_list[9][2], "\t", stock_purchases_list[9][3], "\t", ("{:.2f}".format(int(stock_purchases_list[9][2]) * float(stock_purchases_list[9][3]))))

    print(stock_dictionary["GOOG"], "\t\t", stock_purchases_list[10][0], "\t", stock_purchases_list[10][2], "\t", stock_purchases_list[10][3], "\t", ("{:.2f}".format(int(stock_purchases_list[10][2]) * float(stock_purchases_list[10][3]))))

    print(stock_dictionary["GOOG"], "\t\t", stock_purchases_list[11][0], "\t", stock_purchases_list[11][2], "\t", stock_purchases_list[11][3], "\t", ("{:.2f}".format(int(stock_purchases_list[11][2]) * float(stock_purchases_list[11][3]))))

    print(stock_dictionary["MSFT"], "\t", stock_purchases_list[12][0], "\t", stock_purchases_list[12][2], "\t", stock_purchases_list[12][3], "\t", ("{:.2f}".format(int(stock_purchases_list[12][2]) * float(stock_purchases_list[12][3]))))

    print(stock_dictionary["MSFT"], "\t", stock_purchases_list[13][0], "\t", stock_purchases_list[13][2], "\t", stock_purchases_list[13][3], "\t", ("{:.2f}".format(int(stock_purchases_list[13][2]) * float(stock_purchases_list[13][3]))))

    print(stock_dictionary["MSFT"], "\t", stock_purchases_list[14][0], "\t", stock_purchases_list[14][2], "\t", stock_purchases_list[14][3], "\t", ("{:.2f}".format(int(stock_purchases_list[14][2]) * float(stock_purchases_list[14][3]))))
    
def company_purchase_history(stock_dictionary, stock_purchases_list):
    print(stock_dictionary["AAPL"], stock_purchases_list[0][0])
    print("Shares\tPrice\t\tPurchase Price")
    print(stock_purchases_list[0][2], "\t", stock_purchases_list[0][3], "\t\t", ("{:.2f}".format(int(stock_purchases_list[0][2]) * float(stock_purchases_list[0][3]))))
    print(stock_purchases_list[1][2], "\t", stock_purchases_list[1][3], "\t\t", ("{:.2f}".format(int(stock_purchases_list[1][2]) * float(stock_purchases_list[1][3]))))
    print(stock_purchases_list[2][2], "\t", stock_purchases_list[2][3],"\t", ("{:.2f}".format(int(stock_purchases_list[2][2]) * float(stock_purchases_list[2][3]))))
    print("______________________________________\n")
    print(stock_dictionary["CAT"], stock_purchases_list[0][0])
    print("Shares\tPrice\t\tPurchase Price")
    print(stock_purchases_list[3][2], "\t", stock_purchases_list[3][3], "\t", ("{:.2f}".format(int(stock_purchases_list[3][2]) * float(stock_purchases_list[3][3]))))
    print(stock_purchases_list[4][2], "\t", stock_purchases_list[4][3], "\t", ("{:.2f}".format(int(stock_purchases_list[4][2]) * float(stock_purchases_list[4][3]))))
    print(stock_purchases_list[5][2], "\t", stock_purchases_list[5][3],"\t", ("{:.2f}".format(int(stock_purchases_list[5][2]) * float(stock_purchases_list[5][3]))))
    print("______________________________________\n")
    print(stock_dictionary["EK"], stock_purchases_list[0][0])
    print("Shares\tPrice\t\tPurchase Price")
    print(stock_purchases_list[6][2], "\t", stock_purchases_list[6][3], "\t\t", ("{:.2f}".format(int(stock_purchases_list[6][2]) * float(stock_purchases_list[6][3]))))
    print(stock_purchases_list[7][2], "\t", stock_purchases_list[7][3], "\t\t", ("{:.2f}".format(int(stock_purchases_list[7][2]) * float(stock_purchases_list[7][3]))))
    print(stock_purchases_list[8][2], "\t", stock_purchases_list[8][3],"\t\t", ("{:.2f}".format(int(stock_purchases_list[8][2]) * float(stock_purchases_list[8][3]))))
    print("______________________________________\n")
    print(stock_dictionary["GOOG"], stock_purchases_list[0][0])
    print("Shares\tPrice\t\tPurchase Price")
    print(stock_purchases_list[9][2], "\t", stock_purchases_list[9][3], "\t", ("{:.2f}".format(int(stock_purchases_list[9][2]) * float(stock_purchases_list[9][3]))))
    print(stock_purchases_list[10][2], "\t", stock_purchases_list[10][3], "\t", ("{:.2f}".format(int(stock_purchases_list[10][2]) * float(stock_purchases_list[10][3]))))
    print(stock_purchases_list[11][2], "\t", stock_purchases_list[11][3],"\t", ("{:.2f}".format(int(stock_purchases_list[11][2]) * float(stock_purchases_list[11][3]))))
    print("______________________________________\n")
    print(stock_dictionary["MSFT"], stock_purchases_list[0][0])
    print("Shares\tPrice\t\tPurchase Price")
    print(stock_purchases_list[12][2], "\t", stock_purchases_list[12][3], "\t", ("{:.2f}".format(int(stock_purchases_list[12][2]) * float(stock_purchases_list[12][3]))))
    print(stock_purchases_list[13][2], "\t", stock_purchases_list[13][3], "\t", ("{:.2f}".format(int(stock_purchases_list[13][2]) * float(stock_purchases_list[13][3]))))
    print(stock_purchases_list[14][2], "\t", stock_purchases_list[14][3],"\t", ("{:.2f}".format(int(stock_purchases_list[14][2]) * float(stock_purchases_list[14][3]))))
    print("______________________________________\n")
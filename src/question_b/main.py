from question_b import get_stock_list, get_stock_purchases, Stock, StockPurchase, stock_purchase_history, company_purchase_history


print("Welcome to my Stocks Program")


def main():
    stock_dictionary = get_stock_list()
    stock_purchases_list = get_stock_purchases()

    run_again = "y"
    while run_again.lower() == "y":

        decision = input(
            "1-Display stock purchase history\n2-Display stock purchase history by company\n3-Exit")

        if decision == "1":
            print("Displaying Stock Purchase History")
            print(stock_purchase_history(stock_dictionary, stock_purchases_list))
            run_again = input("Do you have another report to pull? Y or N")
            if run_again.lower() == "n":
                print("Thanks for running my Stocks Program")
                quit()

        elif decision == "2":
            print("Displaying Stock Purchase History by Company")
            print(company_purchase_history(
                stock_dictionary, stock_purchases_list))
            run_again = input("Do you have another report to pull? Y or N")
            if run_again.lower() == "n":
                print("Thanks for running my Stocks Program")
                quit()

        elif decision == "3":
            print("GoodBye")
            quit()


main()

def cop (amount):
    return amount * 0.00026

def mxn (amount):
    return amount * 0.049

def exchanges (amount, typeMoney):
    change = 0
    if typeMoney == 1:
        change = cop(amount)
    elif typeMoney == 2:
        change =  mxn(amount)
    return round(change, 2)

def main ():
    try:
        typeMoney = input('''
            Input the index number between [] for type of money to be exchange to dollar
                [1] COP to USD
                [2] MXN to USD
            Select: ''')
        print("-- Type of money selected: [" + typeMoney + "] --")
        amount = input("Enter the amount of money you want to change to dollar: ")
        change = exchanges(int(amount), int(typeMoney))
        print("The change from money to dollars is: " + str(change) + " USD")
    except:
        print("--- ERROR ---")
        print("Only number value")

main()

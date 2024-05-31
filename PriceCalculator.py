
#TODOs : Rename all python porjects, files, GitHub REPO to more 'MASUK AKAL dan MUDAH DIINGAT'

BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'
print(f"\n{CYAN}Actually {BLUE}Price {RESET}\n")
print(f"Please type {GREEN}'yes' {RESET}to continue and {RED}'no' {RESET}to cancel")
Prep = input("Do you want to use it? ")
if Prep == "Yes" or Prep == "yes" or Prep == "YES" or Prep == "Y" or Prep == "y":
    print("\nOkay, I got this!\n")
    TotalItems = int(input("How many items did you buy? "))
    print()
    PricePerItem = float(input("How much money did you spend for each item? "))
    print()
    TaxPerItem = float(input("How many percentage should you pay the tax for each item? "))
    TotalTaxes = (TaxPerItem / 100) * PricePerItem #! TAX Percentage Calculation Formula
    FinalPrice1 = (PricePerItem + TotalTaxes) * TotalItems
    print("\nPlease type 'yes' to continue and 'no' to cancel")
    Discount = input("Is your item have a discount? ")
    if Discount == "Yes" or Discount == "yes" or Discount == "YES" or Discount == "y" or Discount == "Y":
        DiscountPerItem = float(input("What percentage discount for each item? "))
        print("\nOk! No Problem! \n")
        TotalDiscount = (DiscountPerItem / 100) * PricePerItem * TotalItems #! DISCOUNT Percentage Calculation Formula
        FinalPrice2 = FinalPrice1 - TotalDiscount
        print("Please type 'yes' to continue and 'no' to cancel")
        Tip = input("Do you want to give a tip? ")
        if Tip == "Yes" or Tip == "yes" or Tip == "YES" or Tip == "y" or Tip == "Y":
            TotalTip = float(input("How much money would you like to give a tip? "))
            FinalPrice3a = FinalPrice2 + TotalTip #! TIP-Alt: 1 /// Calculation Formula
            print(f"\n1) {FinalPrice1} Here is the price only with the tax! \n2) {FinalPrice2} Here is the price with the tax and got discounted! \n3) {FinalPrice3a} Here is your final price that has added with tax and tip and also reduced by discount!")
        elif Tip == "No" or Tip == "no" or Tip == "NO" or Tip == "n" or Tip == "N":
            print("\nOkay for that! \n")
            print(f"1) {FinalPrice1} Here is the price only with the tax! \n2) {FinalPrice2} Here is your final price with the tax and reduced by discount! \n")
        else:
            print("Not VALID Input, Please try again! \n")
            exit()
    elif Discount == "No" or Discount == "no" or Discount == "NO" or Discount == "n" or Discount == "N":
        print("\nOkay!\n")
        print("Please type 'yes' to continue and 'no' to cancel")
        Tip = input("Do you want to give a tip? ")
        if Tip == "Yes" or Tip == "yes" or Tip == "YES" or Tip == "y" or Tip == "Y":
            TotalTip = float(input("How much would you like to give a tip? "))
            FinalPrice3b = FinalPrice1 + TotalTip #! TIP-Alt: 2 /// Calculation Formula
            print(f"\n1) {FinalPrice1} Here is your the price only with the tax! \n2) {FinalPrice3b} Here is your final price with the tax and tip! \n")
            print("Please give me some feedback to improve my programming skill =)! \n")
        elif Tip == "No" or Tip == "no" or Tip == "NO" or Tip == "n" or Tip == "N":
            print("\nOkay for that!\n")
            print(f"{FinalPrice1} Here is your final price only with the tax! \n")
        else:
            print("\nNOT Valid input, Please try again!\n")
            exit()
    else:
        print("\nInvalid input, Please try again!\n")
        exit()
elif Prep == "No" or Prep == "no" or Prep == "NO" or Prep == "N" or Prep == "n":
    print(f"\n{MAGENTA}Okie Dokie!{RESET}\n")
    print(f"{CYAN}Please give me some feedback to improve my programming skill!{RESET}\n")
    quit()
else:
    print(f"\n{RED}Invalid input{RESET}, {YELLOW}Please try again!{RESET}\n")
    quit()

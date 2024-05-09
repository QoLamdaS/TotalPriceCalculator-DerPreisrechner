print("\n'Actually Price'\n") 
print("Please type 'yes' to continue and 'no' to cancel")
Prep = input("Do you want to use it? ")
if Prep == "Yes" or Prep == "yes" or Prep == "YES" or Prep == "Y" or Prep == "y":
    print("\nOkay, I got this!\n")
    TotalItems = int(input("How many items did you buy? "))
    print()
    PricePerItem = float(input("How much money did you spend for each item? "))
    print()
    TaxPerItem = float(input("How many percentage should you pay the tax for each item? "))
    
    TotalTaxes1 = TaxPerItem / 100 #! Discount Percentage Calculation Formula
    TotalTaxes2 = TotalTaxes1 * PricePerItem #* Priority for normal price with Tax
    PricePerItemWithTax = PricePerItem + TotalTaxes2
    FinalPrice1 = PricePerItemWithTax * TotalItems
    
    print("\nPlease type 'yes' to continue and 'no' to cancel")
    Discount = input("Is your item have a discount? ")
    if Discount == "Yes" or Discount == "yes" or Discount == "YES" or Discount == "y" or Discount == "Y":
        DiscountPerItem = float(input("What percentage discount for each item? "))
        print("\nOk! No Problem! \n")
        
        TotalDiscount1 = DiscountPerItem / 100 #! Discount Percentage Calculation Formula
        TotalDiscount2 = TotalDiscount1 * PricePerItem
        TotalDiscount3 = TotalDiscount2 * TotalItems
        FinalPrice2 = FinalPrice1 - TotalDiscount3
        
        print("Please type 'yes' to continue and 'no' to cancel")
        Tip = input("Do you want to give a tip? ")
        if Tip == "Yes" or Tip == "yes" or Tip == "YES" or Tip == "y" or Tip == "Y":
            TotalTip = float(input("How much money would you like to give a tip? "))
            
            FinalPrice3a = FinalPrice2 + TotalTip #! Tip Calculation Formula
            
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
            
            FinalPrice3b = FinalPrice1 + TotalTip #! Tip Calculation Formula
            
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
    print("\nOkie Dokie!\n")
    print("Please give me some feedback to improve my programming skill! \n")
    quit()
else:
    print("\nInvalid input, Please try again!\n")
    quit()

#* NOTES:
#* Start : 4/30/2024
#* End : 5/3/2024
#* Last Update : 5/3/2024
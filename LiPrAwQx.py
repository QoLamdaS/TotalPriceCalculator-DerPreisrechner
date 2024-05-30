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
Prep = input(f"{YELLOW}Do you want to use it?{RESET} ")
if Prep == "Yes" or Prep == "yes" or Prep == "YES" or Prep == "Y" or Prep == "y":
    print(f"\n{BLUE}Okay{RESET}, I got this!\n")
    TotalItems = int(input(f"{YELLOW}How many items did you buy?{RESET} "))
    print()
    PricePerItem = float(input(f"{YELLOW}How much money did you spend for each item?{RESET} "))
    print()
    TaxPerItem = float(input(f"{YELLOW}How many percentage should you pay the tax for each item?{RESET} "))
    TotalTaxes = (TaxPerItem / 100) * PricePerItem #! TAX Percentage Calculation Formula
    FinalPrice1 = (PricePerItem + TotalTaxes) * TotalItems
    print(f"\nPlease type {GREEN}'yes'{RESET} to continue and {RED}'no'{RESET} to cancel")
    Discount = input(f"{YELLOW}Is your item have a discount?{RESET} ")
    if Discount == "Yes" or Discount == "yes" or Discount == "YES" or Discount == "y" or Discount == "Y":
        DiscountPerItem = float(input(f"{YELLOW}What percentage discount for each item?{RESET} "))
        print(f"\n{CYAN}Ok! No Problem!{RESET}\n")
        TotalDiscount = (DiscountPerItem / 100) * PricePerItem * TotalItems #! DISCOUNT Percentage Calculation Formula
        FinalPrice2 = FinalPrice1 - TotalDiscount
        print(f"Please type {GREEN}'yes'{RESET} to continue and {RED}'no'{RESET} to cancel")
        Tip = input(f"{YELLOW}Do you want to give a tip?{RESET} ")
        if Tip == "Yes" or Tip == "yes" or Tip == "YES" or Tip == "y" or Tip == "Y":
            TotalTip = float(input(f"{YELLOW}How much money would you like to give a tip?{RESET} "))
            FinalPrice3a = FinalPrice2 + TotalTip #! TIP-Alt: 1 /// Calculation Formula
            print(f"\n1) {RED}{FinalPrice1}{RESET} Here is the price only with the tax! \n2) {CYAN}{FinalPrice2}{RESET} Here is the price with the tax and got discounted! \n3) {BLUE}{FinalPrice3a}{RESET} Here is your final price that has added with tax and tip and also reduced by discount!")
        elif Tip == "No" or Tip == "no" or Tip == "NO" or Tip == "n" or Tip == "N":
            print(f"\n{CYAN}Okay for that!{RESET}\n")
            print(f"1) {RED}{FinalPrice1}{RESET} Here is the price only with the tax! \n2) {CYAN}{FinalPrice2}{RESET} Here is your final price with the tax and reduced by discount!\n")
        else:
            print(f"{RED}Not VALID Input, Please try again!{RESET}\n")
            exit()
    elif Discount == "No" or Discount == "no" or Discount == "NO" or Discount == "n" or Discount == "N":
        print(f"\n{CYAN}Okay!{RESET}\n")
        print(f"Please type {GREEN}'yes'{RESET} to continue and {RED}'no'{RESET} to cancel")
        Tip = input(f"{YELLOW}Do you want to give a tip?{RESET} ")
        if Tip == "Yes" or Tip == "yes" or Tip == "YES" or Tip == "y" or Tip == "Y":
            TotalTip = float(input(f"{YELLOW}How much would you like to give a tip?{RESET} "))
            FinalPrice3b = FinalPrice1 + TotalTip #! TIP-Alt: 2 /// Calculation Formula
            print(f"\n1) {RED}{FinalPrice1}{RESET} Here is your the price only with the tax! \n2) {CYAN}{FinalPrice3b}{RESET} Here is your final price with the tax and tip!\n")
            print(f"{BLUE}Please give me some feedback to improve my programming skill =)!{RESET}\n")
        elif Tip == "No" or Tip == "no" or Tip == "NO" or Tip == "n" or Tip == "N":
            print(f"\n{CYAN}Okay for that!{RESET}\n")
            print(f"{RED}{FinalPrice1}{RESET} Here is your final price only with the tax!\n")
        else:
            print(f"\n{RED}NOT Valid input, Please try again!{RESET}\n")
            exit()
    else:
        print(f"\n{RED}Invalid input, Please try again!{RESET}\n")
        exit()
elif Prep == "No" or Prep == "no" or Prep == "NO" or Prep == "N" or Prep == "n":
    print(f"\n{MAGENTA}Okie Dokie!{RESET}\n")
    print(f"{BLUE}Please give me some feedback to improve my programming skill!{RESET}\n")
    quit()
else:
    print(f"\n{RED}Invalid input, Please try again!{RESET}\n")
    quit()
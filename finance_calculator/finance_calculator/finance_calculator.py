import math

################# PSEUDOCODE ##################

# create a menu for user to choose between 'bond' or 'investment'
# get user input of 'bond' or 'investment'
# create calculations & conditionals for 'investment' input choice
# create calculations & conditionals for 'bond' input choice

################ PROGRAM'S CODE ####################
def calculator():
    """This method will be used to calculate the amount of interest you'll earn on your investment or This method will be used to calculate the amount you have to pay for your bond
        
            :return: The Amount from the investment based on type of interest rate chosen (Simple or Compound Interest) Or The Amount you have to pay from the bond
            :rtype: int
        """
    # SELECTION MENU        
    print("investment - to calculate the amount of interest you'll earn on your investment")
    print("bond       - to calculate the amount you'll have to pay on a home loan\n")
    print("Enter either 'investment' or 'bond' from the menu above to proceed:")

    # GETTING USER INPUT
    type_of_deposit = input("").lower()

    # INVESTMENT CONDITIONALS AND CALCULATIONS
    if type_of_deposit == "investment":

        # GETTING INVESTMENT DETAILS 
        amount = float(input("Amount: "))
        percentage = int(input("Interest Rate(Don't Include '%' Sign): "))
        years = int(input("Number Of Years: "))
        interest = input("'Simple' or 'Compound' Interest: ").lower()
        # SIMPLE INTEREST CALCULATION
        if interest == "simple":
            simple_interest = amount * (1 + ( percentage/100 * years))
            print(f"R{simple_interest}")
        # COMPOUND INTEREST CALCULATION
        elif interest == "compound":
            compound_interest = amount * math.pow((1 + percentage/100), years)
            print(f"R{compound_interest}")


    # BOND CONDITIONALS AND CALCULATIONS
    elif type_of_deposit == "bond":

        # GETTING BOND DETAILS
        house_value = float(input("House Valuation: "))
        percentage = int(input("Annual Interest Rate(Don't Include '%' Sign): "))
        months_of_repayment = int(input("Months Of Repayment: "))
        # CONVERTING INTEREST RATE INTO PERCENTAGE
        percentage = percentage/100
        # MONTHLY REPAYMENT CALCULATION
        repayment = (percentage/12 * house_value)/(1 - (1 + percentage/12)**(-months_of_repayment))
        print(f"R{repayment}")

    else:
        print("Please enter 'investment' or 'bond'.")

calculator()
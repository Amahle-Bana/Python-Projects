# OPEN THE 'Investory.txt' FILE TO READ
with open("inventory/inventory.txt", "r") as shoe_data:
        the_data = shoe_data.read()

#=================== The beginning of the class ===================#

###### INITIALIZNG 'Shoe' CLASS #####
class Shoe:

    """This is a class representation of a shoe collection
    """

    ##### INITIALIZNG 'Shoe' OBJECT #####
    def __init__(self, country, code, product, cost, quantity):
        """Constructor
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity


    ##### FUNCTION TO GET THE COST OF THE SHOE TYPE #####
    def get_cost(self):
        '''Returns the cost of the shoe in this method.

        :return: the shoe cost
        :rtype: int
        '''

        # REPLACING THE SKIP LINE WITH COMMA
        the_list = the_data.replace("\n",",")
        # SPLITTING THE DATA WITH COMMA
        the_price_list = the_list.split(",")
        print("The Shoe Prices:")
        # LOOPING THE DATA TO PRINT OUT THE PRICE
        for price in the_price_list[8::5]:
            print(f"{price}")
    


    ###### FUNCTION TO GET THE QUANTITY OF THE SHOE TYPE ######
    def get_quantity(self):
        '''Returns the quantity of the shoes.

        :return: the quuantity of the shoe
        :rtype: int
        '''

        # REPLACING THE SKIP LINE WITH COMMA
        the_list = the_data.replace("\n",",")
        # SPLITTING THE DATA WITH COMMA
        the_quantity_list = the_list.split(",")
        print("The Quantity:")
        # LOOPING THE DATA TO PRINT OUT THE QUANTITY
        for quantity in the_quantity_list[9::5]:
            print(f"{quantity}")
        


    ##### RETURNS A STRING REPRESENTATION OF A CLASS #####
    def __str__(self):
        '''Returns a string representation of a class.

        :return: string representation of each object
        :rtype: str
        '''
        # PRINTING OUT THE STRING OF EACH SHOE
        print(f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}")



#=============Shoe list===========
shoe_list = []


#==========Functions outside the class==============
while True:
    ##### INPUT SELECTION FOR THE PROGRAM ######
    question = int(input('''Select a Query:
    1 - Read Shoes Data
    2 - Capture Data
    3 - View All
    4 - Restock
    5 - Search Shoe
    6 - Value Per Item
    7 - Highest Quantity
    8 - Exit   
    '''))

    if question == 1:
        # RETURNS THE STRING REPRESENTATION OF A CLASS
        def read_shoes_data():
            """This method will be used to read shoes data

            :return: Show Data from file 
            :rtype: str
            """

            try:
                # OPENS THE 'Investory.txt' FILE
                with open("inventory/inventory.txt", "r") as shoes_data:
                    # READS THE LINES OF THE FILE
                    data = shoes_data.readlines()
                    # LOOPS THROUGH THE LINES
                    for line in data[1::]:
                        # REPLACING THE SKIP LINE WITH COMMA
                        raw_data = line.replace("\n","")
                        # SPLITTING THE DATA WITH COMMA
                        raw_data_2 = raw_data.split(",")
                        # APPEND THE SHOE DATA TO THE SHOE LIST
                        shoe_list.append(Shoe(str(raw_data_2[0]),raw_data_2[1],raw_data_2[2],int(raw_data_2[3]),int(raw_data_2[4])))
            # FILE ERROR EXCEPTION            
            except FileNotFoundError:
                print("The requested file does not exist.")
        read_shoes_data()
        


    if question == 2:
        # CAPTURE THE SHOE DATA
        def capture_shoes():
            """This method will capture shoe data into the 'inventory.txt'
            """

            # CAPTURE INPUT FOR NEW SHOE DATA 
            print("Register A New Shoe:")
            the_country = input("Country: ").capitalize()
            the_code = input("Code: ").upper()
            the_product = input("Product: ").capitalize()
            the_cost = int(input("Cost: "))
            the_quantity = int(input("Quantity: "))

            # APPENDS THE NEW SHOE DATA TO THE SHOE LIST
            shoe_list.append(Shoe(the_country, the_code, the_product, the_cost, the_quantity))
        capture_shoes()



    if question == 3:
        """This method views all of the shoes

            :return: The shoe data of all the shoes 
            :rtype: str
        """

        # VIEW ALL THE SHOE DATA
        def view_all():
            # LOOPS THROUGH THE SHOE LIST
            for shoe in shoe_list:
                # PRINT OUT ALL THE SHOE DATA
                print(shoe.__str__())
        view_all()



    if question == 4:
        def re_stock():
            """This method adds more quantity to the product with the minimun quantity
            """

            # STORING THE VALUE OF THE MINIMUM QUANTITY AND CLOSEST NAME
            minimum = min(shoe_list, key=lambda x: x.product and x.quantity)
            # STORING THEM INDIVIDUALLY
            min_product = minimum.product
            min_quantity = minimum.quantity
            # STRING RESPRESENTATION
            the_minimum = f"{minimum.country},{minimum.code},{minimum.product},{minimum.cost},{minimum.quantity}\n"
            # PRINTING STRING REPRESENTATION
            print(f"The Lowest Quantity is the {minimum.product} shoe with {min_quantity} pairs.")
            # QUANTITY ADDITION INPUT
            quantity_addition = int(input("How much quantity would you add? "))

            # OPENS THE 'Investory.txt' FILE 
            with open("inventory/inventory.txt", "r+") as quantity_data:
                    # READS THE LINES OF THE FILE
                    data = quantity_data.readlines()
                    # LOOPS THROUGH THE LINES
                    for line in data[1::]:
                        # REPLACING THE SKIP LINE WITH COMMA
                        final_data = line.replace("\n","")
                        # SPLITTING THE DATA WITH COMMA
                        final_data_2 = final_data.split(",")
                        # DATA VALIDATION
                        if final_data_2[4] == f'{min_quantity}':
                            final_data_2[4] = int(quantity_addition) + int(final_data_2[4])
                            # WRITING DATA INTO 'Investory.txt' FILE
                            quantity_data.write(f"\n{final_data_2[0]},{final_data_2[1]},{final_data_2[2]},{final_data_2[3]},{final_data_2[4]}")
             
            # OPENS THE 'Investory.txt' FILE
            with open("inventory/inventory.txt", "r") as quantity_data2:
                # READS THE LINES OF THE FILE
                the_data = quantity_data2.readlines()

            # WRITES THE 'Investory.txt' FILE
            with open("inventory/inventory.txt", "w") as quantity_data3:
                # LOOPING THOROUGH THE DATA
                for the_line in the_data:
                    # STRING VALIDATION
                    if the_line != the_minimum:
                        quantity_data3.write(the_line)
        re_stock()



    if question == 5: 
        def search_shoe():
            """ This method helps search shoe using code

                :return: the shoe data
                :rtype: str
            """

            # SHOE CODE INPUT FOR SEARCH 
            search = input("Enter The Code: ").upper()
            # OPENS THE 'Investory.txt' FILE
            with open("inventory/inventory.txt", "r+") as code_data:
                    # READS THE LINES OF THE FILE
                    code_line = code_data.readlines()
                    # LOOPING THROUGH DATA LINES
                    for line in code_line[1::]:
                        # SPLITTING DATA WITH COMMA
                        code_line2 = line.split(",")
                        # SHOE CODE VALIDATION
                        if code_line2[1] == search:
                            print(line)
        search_shoe()



    if question == 6:
        def value_per_item():
            """ This method returns the value of the shoe

                :return: the shoe value
                :rtype: int
            """
            # OPENS THE 'Investory.txt' FILE
            with open("inventory/inventory.txt", "r+") as code_data:
                    # READS THE LINES OF THE FILE
                    code_line = code_data.readlines()
                    # LOOPING THROUGH DATA LINES
                    for line in code_line[1::]:
                        # SPLITTING DATA WITH COMMA
                        code_line2 = line.split(",")
                        # MULTIPLYING PRICE AND QUANTITY
                        value = int(code_line2[3]) * int(code_line2[4])
                        print(f"{value}")
        value_per_item()



    if question == 7:
        def highest_qty():
            """ This method returns the shoe with the highest quantity

                :return: the highest quantity
                :rtype: int
            """
            # STRONG HIGHEST QUANTITY
            maximum = max(shoe_list, key=lambda x: x.product and x.quantity)
            # STORING HIGHEST QUANTITY CHARACTER NAME
            max_product = maximum.product
            # PRINTING
            print(f"The {max_product} is for sale!!!")
            
        highest_qty()



    if question == 8:
        exit()

from datetime import datetime
import csv

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open (filename, "rt") as csv_file:
        reader = csv.reader (csv_file)
        next(reader)
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row
    return dictionary

def main():
    filename = "products.csv"
    key_value_index = 0
    try:
        """opens the products.csv file and converts to a dictionary using the 
        products_dict function"""
        products_dict = read_dictionary(filename, key_value_index )

        """ opens the request.csv file and starts reading each line"""
        with open ("request.csv", "rt") as request_csv:
            reader = csv.reader(request_csv)
            next(reader)
            print ("Inkom Imporium")
            print ("")
            print ("Requested items")
            current_date_and_time = datetime.now()
            num_items = 0
            subtotal = 0.0
            tax = 0.92
            """begins reading line by line from request file"""   
            for line in reader:
                product_num = line[0]
                quantity = line[1]
                """reads line by line from product dictionary
                looking specifically at the key"""  
                for item in products_dict.items():
                    key = item[0]
                    name = item[1][1]
                    price = item[1][2]
                    """when the """
                    if key == product_num:
                        num_items= int(quantity) + num_items
                        subtotal = subtotal + (float(price) * int(quantity))
                        print(f"{name}: {quantity} @ {price}") 
                        
    except FileNotFoundError as not_found_err:
        print(f"Error: cannot open {filename}"
                 " because it doesn't exist.")
    except KeyError:
        print (f"Error: Product ID does not exist.")
              
            
    print("")
    print (f"Number of Items: {num_items}")
    total = (subtotal*tax)+subtotal
    print (f"Subtotal: {subtotal:.2f}")
    print (f"Sales Tax: {tax}")
    print (f"Total: {total:.2f}")
    print ("")
    print ("Thank you for shopping at Inkom Emporium")
    print (f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")
    print("")
    print("""Please feel free to fill out an online  
survey and let us know how we are doing. 
    www.inkemporium.com/survey""")
    print ("")
    
                    

if __name__ == "__main__":
    main()
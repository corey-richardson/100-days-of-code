# dec_to_bin(bits)

from dec_to_bin import dec_to_bin
from bin_to_dec import bin_to_dec

def main():
    while True:
        selection = select()
        
        match selection:
            
            case "1": # need to be str values, not int else an error is thrown when "end" is inputted
                try:
                    dec = int(input("Enter decimal value to convert: "))
                except TypeError:
                    import sys
                    sys.exit("Enter an integer value") 
                dec_to_bin(dec)
                
            case "2":
                bin = input("Enter binary value to convert: ")
                bin_to_dec(bin)
                
            case "3":
                print("to add")
                
            case "4":
                print("to add")
                
            case "5":
                print("to add")
                
            case "6":
                print("to add")
                
            case "end":
                import sys
                sys.exit("User requested exit")
            case _:
                print("Reprompt")
        
def select():
    print("\nConverter:")
    print("1. decimal (base 10) --> binary (base 2)")
    print("2. binary (base 2) -- > decimal (base 10)")
    print("3. decimal (base 10) --> hexadecimal (base 16)")
    print("4. hexadecimal (base 16) --> decimal (base 10)")
    print("5. binary (base 2) --> hexadecimal (base 16)") # bin --> dec --> hex
    print("6. hexadecimal (base 16) --> binary (base 2)") # hex --> dex --> bin
    return input()
    
        
if __name__ == "__main__":
    main()
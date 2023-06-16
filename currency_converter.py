def main():
    print("This program converts US dollars to Sterling Pounds")
    print()
    
    dollars = eval(input("Enter amount in shillings: "))
    
    pounds = convert_to_pounds(dollars)
    
    print("That is", pounds, "pounds.")
    
convert_to_pounds = lambda dollars: dollars * 0.82

main()

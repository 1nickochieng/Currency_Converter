def main():
    print("This program converts US dollars to Kenya Shillings")
    print()
    
    dollars = eval(input("Enter amount in Kenyan shillings: "))
    
    pounds = convert_to_shillings(dollars)
    
    print("That is", shillings, "shillings.")
    
convert_to_shillings = lambda dollars: dollars * 0.82

main()

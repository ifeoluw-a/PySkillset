def coke_machine(amount_due=50):
    # Continue until the amount due is zero or less
    while amount_due > 0:
        # Display the current amount due
        print(f"Amount Due: {amount_due}")
        # Prompt the user to insert a coin and convert the input to an integer
        coin = int(input("Insert Coin: "))
        
        # Check if the coin is of a valid denomination
        if coin in [5, 10, 25]:
            # Deduct the value of the coin from the amount due
            amount_due -= coin
        else:
            # Ignore invalid coins
            continue
    
    # Print the amount of change owed (if any)
    return print(f"Change owed: {-1 * amount_due}")

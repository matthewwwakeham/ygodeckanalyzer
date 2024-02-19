import csv
import random

print(".~`PYTHON DECK ANALYZER`~.")

# Open a CSV file in write mode ('w', newline='') as csv_file
try:
    with open('output.csv', 'w', newline='') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)

        # Initialize total quantity
        total_quantity = 0
        card_quantities = {}

        # Write headers
        headers = ["NAME OF CARD", "QUANTITY"]
        csv_writer.writerow(headers)

        # Loop to allow the user to enter information
        while True:
            try:
                name_of_card = input("Enter the card name (or type 'end' to finish): ")
        
                # Check if the user wants to end
                if name_of_card.lower() == 'end':
                    break

                # Input validation for quantity
                while True:
                    quantity = int(input("Enter the quantity: "))
                    if 1 <= quantity <= 3:
                        break
                    else:
                        print("Please enter a number between 1 and 3.")
            except ValueError:
                print("Please try again.")

            # Update total quantity
            total_quantity += quantity
            card_quantities[name_of_card] = quantity
        
            # Write the data to the CSV file
            csv_writer.writerow([name_of_card, quantity, ""])

            print(f"Total quantity: {total_quantity}")
            print("Data has been successfully written to 'output.csv'.")

        # Calculate probabilities with replacement
        probabilities = {card: quantity / total_quantity for card, quantity in card_quantities.items()}

        # Write probabilities to the CSV file
        csv_writer.writerow(["", "PROBABILITY"])
        for card, probability in probabilities.items():
            csv_writer.writerow([card, f"{probability * 100:.2f}%"])

        # Print probabilities
        print("\nProbabilities:")
        for card, probability in probabilities.items():
            print(f"{card}: {probability * 100:.2f}%")

        # Simulate drawing 10 beginning hands with replacement
        num_hands = min(10, total_quantity)

        for _ in range(num_hands):
            # Get keys (card names) for random sample
            cards_in_hand = random.choices(list(card_quantities.keys()), weights=probabilities.values(), k=5)

            print(f"\nRandom Starting Hand: {cards_in_hand}")

except Exception as e:
    print(f"An error occurred: {e}")
print("===== SMART ELECTRICITY BILL SYSTEM =====")

# Challenge 1 & 2: Validate number of households and handle non-numeric input
while True:
    try:
        households = int(input("Enter the number of households: "))
        if households > 0:
            break
        print("Please enter a number greater than zero.")
    except ValueError:
        print("Invalid input! Please enter a valid whole number.")

total_revenue = 0
successful_counts = 0  # Challenge 3: Track successful calculations
highest_bill = 0       # Challenge 4: Track highest individual bill
highest_household = 0  # Challenge 6: Track household number with highest bill

for household in range(1, households + 1):
    print(f"\n--- Household {household} ---")
    
    # Challenge 2: Handle non-numeric input for units
    try:
        units = int(input("Enter electricity units consumed: "))
    except ValueError:
        print("Invalid input! Skipping this household due to non-numeric entry.")
        continue

    if units < 0:
        print("Invalid units! Please enter a non-negative value.")
        continue

    # Tiered pricing calculation
    if units <= 100:
        bill = units * 10
    elif units <= 200:
        bill = (100 * 10) + ((units - 100) * 15)
    else:
        bill = (100 * 10) + (100 * 15) + ((units - 200) * 20)

    print(f"Units Consumed: {units}")
    print(f"Electricity Bill: Rs. {bill}")

    # Accumulate totals and metrics
    total_revenue += bill
    successful_counts += 1
    
    # Challenge 4 & 6: Find the highest bill and corresponding household
    if bill > highest_bill:
        highest_bill = bill
        highest_household = household

print("\n===== MONTHLY REVENUE REPORT =====")
print(f"Households Processed: {households}")
print(f"Successful Calculations: {successful_counts}")

# Challenge 5: Calculate and display average bill safely
if successful_counts > 0:
    average_bill = total_revenue / successful_counts
    print(f"Total Revenue: Rs. {total_revenue}")
    print(f"Average Bill: Rs. {average_bill:.2f}")
    print(f"Highest Bill: Rs. {highest_bill} (Household {highest_household})")
else:
    print("No valid household bills were calculated.")

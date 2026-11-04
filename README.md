# Python Loops: Smart Electricity Bill Calculator

A beginner-friendly, console-based Python program that calculates tiered electricity bills for multiple households. It demonstrates `while` loops, `for` loops, `range()`, accumulators, conditional statements, input validation, exception handling, `continue`, and summary calculations.

## Repository Information

- **Repository Name:** `python-loops-electricity-bill-calculator`
- **Program File:** `smart_electricity_bill.py`
- **Description:** A Python practice project that calculates household electricity bills, validates user input, and reports total revenue, successful calculations, the average bill, and the highest bill.

## 1. Real-World Scenario

An electricity company needs to calculate monthly electricity bills for multiple households.

The program first asks how many households should be processed. It then collects the electricity consumption for each household, calculates a bill when the input is valid, and maintains summary statistics for the valid bills.

**Important:** The electricity rates in this project are fictional and are used for programming practice only. They do not represent actual electricity tariffs.

## 2. Electricity Billing Rules

The program uses progressive (tiered) billing:

| Electricity consumption | Rate |
|---|---:|
| First 100 units | Rs. 10 per unit |
| Units 101–200 | Rs. 15 per unit |
| Units above 200 | Rs. 20 per unit |

Each rate applies only to the units within its tier.

### Example Calculations

**Example 1: 80 units**

- 80 × 10 = Rs. 800
- **Total bill: Rs. 800**

**Example 2: 150 units**

- First 100 units: 100 × 10 = Rs. 1,000
- Remaining 50 units: 50 × 15 = Rs. 750
- **Total bill: Rs. 1,750**

**Example 3: 250 units**

- First 100 units: 100 × 10 = Rs. 1,000
- Next 100 units: 100 × 15 = Rs. 1,500
- Remaining 50 units: 50 × 20 = Rs. 1,000
- **Total bill: Rs. 3,500**

## 3. Program Logic

### A. Validate the number of households with a `while` loop

The program repeatedly asks for the number of households until the user enters a valid whole number greater than zero.

- Non-numeric input is handled with `try` and `except`.
- Zero or a negative number is rejected.
- `break` exits the validation loop once the input is valid.

### B. Process households with a `for` loop and `range()`

```python
for household in range(1, households + 1):
    ...
```

This processes household numbers from `1` through the number entered by the user.

### C. Validate electricity-unit input

For each household, the program attempts to convert the entered consumption to an integer.

- Non-numeric input displays an error and skips that household.
- Negative units are rejected and the household is skipped.
- Zero units are accepted and produce a bill of Rs. 0.
- Valid entries continue to the billing calculation.

The `continue` statement skips the remaining steps for the current household and moves to the next loop iteration.

### D. Calculate the bill with conditional statements

The `if`, `elif`, and `else` statements select the appropriate progressive billing calculation:

```python
if units <= 100:
    bill = units * 10
elif units <= 200:
    bill = (100 * 10) + ((units - 100) * 15)
else:
    bill = (100 * 10) + (100 * 15) + ((units - 200) * 20)
```

### E. Maintain totals and statistics with accumulators

The program initializes these variables before processing households:

```python
total_revenue = 0
successful_counts = 0
highest_bill = 0
highest_household = 0
```

For every valid household bill:

- `total_revenue` adds the bill to the running revenue total.
- `successful_counts` increases by one.
- `highest_bill` and `highest_household` are updated when a bill is greater than the current highest bill.

### F. Calculate the average safely

After all households have been processed, the program checks whether at least one valid bill exists.

```python
if successful_counts > 0:
    average_bill = total_revenue / successful_counts
```

The average is calculated using only successful bill calculations. If there are no valid entries, the program displays a message instead of dividing by zero.

## 4. Program Features

1. Validates that the household count is a whole number greater than zero.
2. Handles non-numeric household-count input using `try` and `except`.
3. Processes each household with a `for` loop.
4. Handles non-numeric electricity-unit input and skips that household.
5. Rejects negative electricity-unit values.
6. Accepts zero as a valid consumption value.
7. Calculates bills using progressive electricity rates.
8. Displays the units consumed and bill for each valid household.
9. Tracks the number of successful bill calculations.
10. Calculates total revenue from valid bills only.
11. Calculates the average bill from valid bills only.
12. Tracks and displays the highest bill and its household number when a bill exceeds the current highest amount.
13. Displays a final monthly revenue report.

**Counting note:** `Households Processed` displays the total number originally requested. `Successful Calculations` counts only households with valid, non-negative whole-number unit entries.

## 5. Python Concepts Demonstrated

| Concept | How it is used |
|---|---|
| `while` loop | Repeats household-count input until it is valid |
| `for` loop | Processes each household |
| `range()` | Generates household numbers |
| `if`, `elif`, `else` | Validates input and selects a billing tier |
| `try` and `except` | Handles non-numeric input |
| `break` | Exits the household-count validation loop |
| `continue` | Skips a household with invalid unit input |
| Accumulators | Tracks total revenue and successful calculations |
| Comparison | Finds a bill greater than the current highest bill |
| Arithmetic | Calculates bills and the average |

## 6. How to Run the Program

### Prerequisites

- Python 3 installed on your computer.
- A terminal or code editor, such as Visual Studio Code or PyCharm.

### Execution

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python smart_electricity_bill.py
```

On some systems, use `python3` instead of `python`.

## 7. Example Output

For three households consuming 80, 150, and 250 units, the program displays:

```text
===== SMART ELECTRICITY BILL SYSTEM =====
Enter the number of households: 3

--- Household 1 ---
Enter electricity units consumed: 80
Units Consumed: 80
Electricity Bill: Rs. 800

--- Household 2 ---
Enter electricity units consumed: 150
Units Consumed: 150
Electricity Bill: Rs. 1750

--- Household 3 ---
Enter electricity units consumed: 250
Units Consumed: 250
Electricity Bill: Rs. 3500

===== MONTHLY REVENUE REPORT =====
Households Processed: 3
Successful Calculations: 3
Total Revenue: Rs. 6050
Average Bill: Rs. 2016.67
Highest Bill: Rs. 3500 (Household 3)
```

## 8. Input Validation Examples

- **Household count entered as text:** The program displays an error and asks again.
- **Household count entered as zero or a negative number:** The program asks for a number greater than zero.
- **Electricity units entered as text:** The program skips that household and continues.
- **Negative electricity units:** The program displays an error and skips that household.
- **No successful calculations:** The report displays `No valid household bills were calculated.` and avoids calculating an average.

## 9. Learning Outcomes

After studying this program, students should be able to:

- Use `while` and `for` loops for repetition.
- Use `range()` to control loop iterations.
- Apply conditional statements to implement business rules.
- Validate user input with `try` and `except`.
- Understand the use of `break` and `continue`.
- Use accumulators and counters.
- Calculate totals, averages, and a maximum value.
- Convert a real-world tiered pricing rule into Python code.

## 10. Possible Future Improvements

- Track and display the household with the highest bill when multiple households have the same bill.
- Allow decimal electricity consumption if the billing rules require it.
- Store household results in a list and display a detailed summary table.
- Add automated tests for billing boundaries such as 100, 101, 200, and 201 units.

## Suggested Git Commit

```text
Update README to document electricity bill calculator logic
```

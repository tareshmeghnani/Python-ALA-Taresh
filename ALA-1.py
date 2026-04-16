print("Series Sum Program") 
# ✅ Correct: Prints the program title.

n = int(input("Enter Limit: "))
# ✅ Correct: Takes user input as integer.

i = 1
# ✅ Correct: Initializes loop counter.

Series_sum = 0
# ❌ Mistake: Using `sum` shadows Python’s built-in sum() function.
# ✔ Fix: Rename to `Series_sum` or another variable name.

while i <= n:
    # ✅ Correct: Loop condition is fine here.

    square = i**2
    cube = i**3
    Series_sum = Series_sum + square + cube
    # ✅ Logic is correct: adds square and cube to total.

    if square % 2 == 0:
        # ❌ Syntax Error: Missing colon (:) at the end of the if statement.
        # ✔ Fix: `if square % 2 == 0:`

        print("Even square:", square)
        # ✅ Correct: Prints even squares.

    else:
        print("Odd Square:", square)
        # ✅ Correct: Prints odd squares.
    
    
    i = i + 1
    # ✅ Correct: Increments loop counter.

print("Total sum:", Series_sum)
# ❌ Syntax Error: Missing closing parenthesis. # ✔ Fix: `print("Total sum:", sum)`


if Series_sum > 500:
    print("Large Total")
    # ✅ Correct: Prints when sum is greater than 500.

else:
    print("Small Total")
    # ✅ Correct: Prints when sum is less than or equal to 500.

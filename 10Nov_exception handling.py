
# try + except
print("try + except")
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")
print()

# -------------------------------------------------------------------
# try + finally
print("try + finally")
try:
    print("In try block")
finally:
    print("This will always execute (even without except)")
print()

# -------------------------------------------------------------------
# try + except + else
print("try + except + else")
try:
    x = 5 / 1
except ZeroDivisionError:
    print("Error occurred!")
else:
    print("No error occurred, so else block executed")
print()

# -------------------------------------------------------------------
# try + except + finally
print("try + except + finally")
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error caught in except block")
finally:
    print("Finally block always runs")
print()

# -------------------------------------------------------------------
# try + except + else + finally
print("try + except + else + finally")
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Division error occurred")
else:
    print("No error, else block executed")
finally:
    print("Finally block executed no matter what")
print()

# -------------------------------------------------------------------
# will cause an error because 'try' is missing
"""
else:
    print("This will cause an error if run alone")
"""
# 'except', 'else', and 'finally' cannot exist without 'try'


# -------------------------------------------------------------------
# Nested try-except demonstration
try:
    # Outer try block
    print("Outer try block started")
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))

    try:
        # Inner try block
        print("\nInner try block started")
        result = num1 / num2
        print("Division Result:", result)

        # Simulate another possible error
        lst = [1, 2, 3]
        index = int(input("Enter index to access list element: "))
        print("Element at index:", lst[index])

    except ZeroDivisionError:
        print("Inner except: Cannot divide by zero.")
    except IndexError:
        print("Inner except: Invalid index for the list.")

    print("Inner try-except completed.")

except ValueError:
    print("Outer except: Invalid input. Please enter integers only.")

except Exception as e:
    print("Outer except: Some unexpected error occurred ->", e)

finally:
    print("Finally block executed — program ended safely.")

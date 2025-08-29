# String in-built methods

# ------------------ CASE CONVERSION ------------------

# upper()
text1 = "hello"
print("# upper()")
print(text1.upper())   # HELLO
print()

# lower()
text2 = "PYTHON"
print("# lower()")
print(text2.lower())   # python
print()

# title()
text3 = "python programming"
print("# title()")
print(text3.title())   # Python Programming
print()

# capitalize()
text4 = "good morning"
print("# capitalize()")
print(text4.capitalize())   # Good morning
print()

# swapcase()
text5 = "PyThOn"
print("# swapcase()")
print(text5.swapcase())   # pYtHoN
print()


# ------------------ SEARCHING ------------------

# find()
text6 = "hello world"
print("# find()")
print(text6.find("world"))   # 6
print()

# index()
text7 = "banana"
print("# index()")
print(text7.index("n"))   # 2
print()

# count()
text8 = "banana"
print("# count()")
print(text8.count("a"))   # 3
print()


# ------------------ TRIMMING ------------------

# strip()
text9 = "   python   "
print("# strip()")
print(text9.strip())   # python
print()

# lstrip()
print("# lstrip()")
print(text9.lstrip())  # "python   "
print()

# rstrip()
print("# rstrip()")
print(text9.rstrip())  # "   python"
print()


# ------------------ REPLACE / SPLIT / JOIN ------------------

# replace()
text10 = "I like Java"
print("# replace()")
print(text10.replace("Java", "Python"))  # I like Python
print()

# split()
text11 = "apple,banana,cherry"
print("# split()")
print(text11.split(","))  # ['apple', 'banana', 'cherry']
print()

# join()
words = ["I", "love", "Python"]
print("# join()")
print(" ".join(words))  # I love Python
print()


# ------------------ CHECKING ------------------

# startswith()
text12 = "hello"
print("# startswith()")
print(text12.startswith("he"))  # True
print()

# endswith()
print("# endswith()")
print(text12.endswith("lo"))  # True
print()

# isalpha()
text13 = "Python"
print("# isalpha()")
print(text13.isalpha())  # True
print()

# isdigit()
text14 = "12345"
print("# isdigit()")
print(text14.isdigit())  # True
print()

# isalnum()
text15 = "Python123"
print("# isalnum()")
print(text15.isalnum())  # True
print()


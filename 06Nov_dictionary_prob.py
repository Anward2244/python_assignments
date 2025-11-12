# --------------------------------------------------------------
# 1. Check if the second string is a substring of the first string

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

found = False
index = -1

for i in range(len(s1) - len(s2) + 1):
    if s1[i:i+len(s2)] == s2:
        found = True
        index = i
        break

if found:
    print("Second string is a substring of the first string.")
    print("Starting index:", index)
else:
    print("Second string is NOT a substring of the first string.")


# --------------------------------------------------------------
# 2. Find the largest word in a string without using split()

sentence = input("Enter a sentence: ")

word = ""
largest = ""
for ch in sentence + " ":
    if ch != " ":
        word += ch
    else:
        if len(word) > len(largest):
            largest = word
        word = ""

print("Largest word:", largest)

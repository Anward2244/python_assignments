#'(a+b-c*[e/f])' Remove brackets from string----------------------------
#a+b-c*e/f
str = '(a+b-c*[e/f])'
new_str = ''
for i in str:
    if i not in '[]()}{':
        new_str += i
print(new_str)


#reverse a string  - 4 ways-----------------------------------------------
# method 1
name1 = "Anwar Dudekula"
print(name1[::-1])

# method 2
name1 = "Anwar Dudekula"
new_name = ''
for i in name1:
    new_name = i + new_name
print(new_name)

# method 3
name1 = "Anwar Dudekula"
new_name = ''
for i in range(len(name1) - 1, -1, -1):
    new_name = new_name + name1[i]
print(new_name)

# method 4
def rev_string(str):
    
    if len(str) == 1:
        return str

    return str[len(str) - 1] + rev_string(str[:-1])

name1 = "Anwar Dudekula"
print(rev_string(name1))


#vowel, consonant, spaces count in a string-------------------------------------
str8 = 'Mahavatar Narasimha'
vowels_count = 0
cons_count = 0
spaces = 0
for i in str8:
    if i in 'AEIOUaeiou':
        vowels_count +=1
    elif  i not in 'AEIOUaeiou' and (('a'<= i <='z') or ('A'<= i <='Z')):
        cons_count += 1
    elif i == " ":
        spaces += 1
print('vowels = ', vowels_count)
print('consonants = ', cons_count)
print('spaces = ', spaces)

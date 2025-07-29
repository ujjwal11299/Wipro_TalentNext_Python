#Create a Python module with the following functions:

def ispalindrome(name):
    name = name.replace(" ", "").lower()
    return name == name[::-1]

def count_the_vowels(name):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in name if char in vowels)

def frequency_of_letters(name):
    name = name.replace(" ", "")
    freq = {}
    for char in name:
        freq[char] = freq.get(char, 0) + 1
    return freq


name1 = "bob"
print("Sample input 1:", name1)

if ispalindrome(name1):
    print("Yes it is a palindrome.")
else:
    print("No it is not a palindrome.")

print("No of vowels:", count_the_vowels(name1))

freq1 = frequency_of_letters(name1)
print("Frequency of letters:", ', '.join(f"{k}-{v}" for k, v in freq1.items()))

print()

name2 = "marcel bentok tanaka"
print("Sample input 2:", name2)

if ispalindrome(name2):
    print("Yes it is a palindrome.")
else:
    print("No it is not a palindrome.")

print("No of vowels:", count_the_vowels(name2))

freq2 = frequency_of_letters(name2)
print("Frequency of letters:", ', '.join(f"{k}-{v}" for k, v in freq2.items()))

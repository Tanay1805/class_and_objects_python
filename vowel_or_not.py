vowel=input("Enter a letter:")
lowercase_string=vowel.lower()

if lowercase_string == 'a'and'e'and'i'and'o'and'u':
    print(lowercase_string,"is a vowel")
elif len(vowel) > 1:
    print("Invalid entry")
else:
    print(lowercase_string,"it is not a vowel")
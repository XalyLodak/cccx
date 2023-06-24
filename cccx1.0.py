import string
print("CCCX 1.0 : César Code Creator by XalyLodak")
offset = int(input("What offset ? (0 à 25) : "))

if offset >= 0 and offset <= 25:
    word = input("Type your word : ")
    letters = string.ascii_uppercase
    letters_offset = letters[offset:] + letters[:offset]
    encrypted_word = ""

    for i, lettre in enumerate(word):
        if lettre.isalpha():
            v1 = (letters.index(lettre.upper()) + offset) % 26
            encrypted_word += letters_offset[v1]
        else:
            encrypted_word += lettre

    print("Your encrypted word : " + encrypted_word)

else:
    print("E: Your number does not correspond to a valid shift in the alphabet. Please try a number between 0 and 25 again.")

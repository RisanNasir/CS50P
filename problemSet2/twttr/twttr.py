def main():
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    phrase = input("Input: ")
    for vowel in vowels:
        phrase = omit_vowel(vowel, phrase)
    print("Output:",phrase)

def omit_vowel(vowel, str):
    return str.replace(vowel,"")




main()

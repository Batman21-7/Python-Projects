import pandas as pd


def function():
    try:
        arr = [alpha_dict[letter] for letter in input("Enter a word: ").upper()]
    except KeyError:
        print("Sorry, only letters in the alphabets please")
        function()
    else:
        print(arr)


df = pd.read_csv("nato_phonetic_alphabet.csv")
alpha_dict = {row.letter: row.code for (index, row) in df.iterrows()}

function()

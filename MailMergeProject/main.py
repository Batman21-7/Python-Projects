# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("./Input/Letters/starting_letter.txt", 'r') as letter:
    og_array = letter.readlines()

with open("./Input/Names/invited_names.txt", 'r') as names:
    names_arr = names.readlines()

for name in names_arr:
    new_name = name.strip()
    new_array = og_array.copy()
    new_array[0] = og_array[0].replace("[name]", new_name)
    with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", 'w') as new_letter:
        new_letter.write("".join(new_array))

# It just replaces a special word from your already created email file with the one you made in ".txt" file.
#Some Basics
with open("File_name","r") as names:
    name_list = names.readlines()

with open("letter_name","r") as letter:
    letter_content = letter.read()

for name in name_list:
    new_contents = letter_content.replace("[name]", name.strip())
    with open(f'file_name{name.strip()}.txt', 'w') as files:
        files.write(new_contents)


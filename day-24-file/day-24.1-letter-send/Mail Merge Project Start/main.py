#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

list_of_invited_name = []
format_letter = []
with open("./Input/Names/invited_names.txt", "r") as name_list:
    for name in name_list:
        list_of_invited_name.append(name.replace("\n", ""))

with open("./Input/Letters/starting_letter.txt", "r") as letter:
    for line in letter:
        format_letter.append(line)

begin_regard = format_letter[0]
letter_for_send = format_letter


for name in list_of_invited_name:
    letter_for_send[0] = begin_regard.replace("[name],", f"{name},")

    data_outputs = open(f"./Output/ReadyToSend/letter_{name}.txt", mode="a")
    for line in letter_for_send:
        data_outputs.write(line)
    data_outputs.close()
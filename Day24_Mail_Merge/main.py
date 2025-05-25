#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
#C:\Users\lenovo\PycharmProjects\PythonProject\Day24_Mail_Merge\Input\Names\invited_names.txt
#C:\Users\lenovo\PycharmProjects\PythonProject\Day24_Mail_Merge\main_states.py

invites = []
with open('Input/Names/invited_names.txt', 'r+') as invitees:
    lines = invitees.readlines()
    for line in lines:
        invites.append(line.strip())
print(invites)


for invite in invites:
    print(f'For {invite}')
    with open('Input/Letters/starting_letter.txt', 'r') as rite:
        lines = rite.readlines()
        for line in lines:
            with open(f'Output/ReadyToSend/{invite}.txt','a') as infile:
                 if '[name]' in line:
                     updated = line.replace('[name]', invite)
                     infile.write(updated)
                 else:
                     infile.write(line)


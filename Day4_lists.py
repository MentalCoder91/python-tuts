states_india = ["Maharashtra", "Madhya Pradesh", "Gujrat", "Andhra Pradesh"]

#Index based printing
print(states_india[-1])

# Lists are mutable
states_india[0] = "India"
print(states_india)

#Add Element
states_india.append("Anish")
print(states_india)

#Extend lists
states_india.extend(["Ruchi", "Piyaa"])
print(states_india)

import numpy as np
import sys

#FIRST DFA
dfa1 = {
    "iStates": [], 
    "fStates": [],
    "nfStates": [],
    "states": [], 
    "transitions": [], 
}

dfa1["iStates"] = [i.strip() for i in (input("Enter the initial states in the first DFA: ")).split(",")]
dfa1["fStates"] = [i.strip() for i in (input("Enter the final states in the first DFA: ")).split(",")]
dfa1["nfStates"] = [i.strip() for i in (input("Enter the non-final / non-initial states in the first DFA: ")).split(",")]

#removing any empty strings from array
while("" in dfa1["iStates"]) :
    dfa1["iStates"].remove("")

while("" in dfa1["fStates"]) :
    dfa1["fStates"].remove("")

while("" in dfa1["nfStates"]) :
    dfa1["nfStates"].remove("")
  
dfa1["states"] = [i for i in np.unique(sorted(dfa1["iStates"] + dfa1["fStates"] + dfa1["nfStates"]))]

if len(dfa1["iStates"]) == 0 or len(dfa1["fStates"]) == 0:
    sys.exit("ERROR, DFA must have atleast one final and one initial state")
#   exit(0)

for state in dfa1["nfStates"]:
  if state in dfa1["fStates"] or state in dfa1["iStates"]:
    sys.exit("ERROR in values, please input a valid DFA")

print("Enter transitions")
for i in dfa1["states"]:
  s = str(i) + " + 0 -> "
  temp = input(s)
  if temp not in dfa1["states"]:
    sys.exit("Error, enter valid values")
  arr1 = [i, 0, temp]
  s = str(i) + " + 1 -> "
  temp = input(s)
  if temp not in dfa1["states"]:
    sys.exit("Error, enter valid values")
  arr2 = [i, 1, temp]
  dfa1["transitions"].append([arr1, arr2])

#SECOND DFA
dfa2 = {
    "iStates": [], 
    "fStates": [],
    "nfStates": [],
    "states": [], 
    "transitions": [], 
}

dfa2["iStates"] = [i.strip() for i in (input("Enter the initial states in the second DFA: ")).split(",")]
dfa2["fStates"] = [i.strip() for i in (input("Enter the final states in the second DFA: ")).split(",")]
dfa2["nfStates"] = [i.strip() for i in (input("Enter the non-final / non-initial states in the second DFA: ")).split(",")]

#removing any empty strings from array
while("" in dfa2["iStates"]) :
    dfa2["iStates"].remove("")

while("" in dfa2["fStates"]) :
    dfa2["fStates"].remove("")

while("" in dfa2["nfStates"]) :
    dfa2["nfStates"].remove("")
  
dfa2["states"] = [i for i in np.unique(sorted(dfa2["iStates"] + dfa2["fStates"] + dfa2["nfStates"]))]

if len(dfa2["iStates"]) == 0 or len(dfa2["fStates"]) == 0:
    sys.exit("ERROR, DFA must have atleast one final and one initial state")
#   exit(0)

for state in dfa2["nfStates"]:
  if state in dfa2["fStates"] or state in dfa2["iStates"]:
    sys.exit("ERROR in values, please input a valid DFA")

print("Enter transitions")
for i in dfa2["states"]:
  s = str(i) + " + 0 -> "
  temp = input(s)
  if temp not in dfa2["states"]:
    sys.exit("Error, enter valid values")
  arr1 = [i, 0, temp]
  s = str(i) + " + 1 -> "
  temp = input(s)
  if temp not in dfa2["states"]:
    sys.exit("Error, enter valid values")
  arr2 = [i, 1, temp]
  dfa2["transitions"].append([arr1, arr2])

#checking equivalence
if (len(dfa1["iStates"]) != len(dfa2["iStates"])) or (len(dfa1["fStates"]) != len(dfa2["fStates"])):
    print("Not equivalent")
elif (len(dfa1["states"]) != len(dfa2["states"])):
    print("Not equivalent")
else:
    temp = []
    for i in range(len(dfa1["transitions"])):
        if dfa1["transitions"][i][0][2] in dfa1["fStates"]:
            temp.append(1)
        else:
            temp.append(0)
        if  dfa2["transitions"][i][0][2] in dfa2["fStates"]:
            temp.append(1)
        else:
            temp.append(0)
        if (temp[0] != temp[1]):
            sys.exit("Not equivalent")
        temp = []
        if dfa1["transitions"][i][1][2] in dfa1["fStates"]:
            temp.append(1)
        else:
            temp.append(0)
        if  dfa2["transitions"][i][1][2] in dfa2["fStates"]:
            temp.append(1)
        else:
            temp.append(0)
        if (temp[0] != temp[1]):
            sys.exit("Not equivalent")
    print("Equivalent")

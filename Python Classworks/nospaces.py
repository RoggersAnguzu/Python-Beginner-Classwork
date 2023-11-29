s = "The money is hidden under the floor."
print("The length of the string is", len(s))

spaces = 0
for ch in s:
    if ch == ' ':
        spaces += 1
        
print("Without spaces: ", len(s)-spaces)

notsp = 0
for ch in s:
    if ch != ' ':
        notsp = notsp + 1
print("Without spaces: ", notsp)
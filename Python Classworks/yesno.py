response = input("Are you 18 or older? ")

if response == 'yes' or response == 'Yes':
    print("You can vote.")
elif response == 'no':
    print("You are not ready to vote.")
else:
    print("Answer the question please!")

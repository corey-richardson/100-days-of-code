#100 days of code readME maker

with open("text.txt","w") as file:
    pass

with open("text.txt","a") as file:
    for number in range(100):
        file.write(f"Day {number+1}:\n\n")
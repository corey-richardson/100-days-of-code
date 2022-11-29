# links
with open("links.txt","w") as file:
    pass

for i in range(100):
    url = "https://github.com/corey-richardson/100DaysOfCode/blob/main/README.md#day-"
    dated_url = url + str(i+1)
    full = f"[day-{i+1}]({dated_url})"
    with open("links.txt","a") as file:
        file.write(full + " ")

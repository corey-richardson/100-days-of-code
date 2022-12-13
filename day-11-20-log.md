### Day 11: 2/12/2022

**Today's Tasks and Progress:** CS50P Final Project | Mathworks MATLAB Fundamentals Course: Programming Constructs, Increasing Automation with Functions, Troubleshooting Code, Review Project II, Conclusion, COMPLETED :)

**About:** Tried to regular expressions to find the absolute file path of the script so the created files always go to that location rather than the location of the terminal window which is often not right. Didn't work. :) Instead, run this command ```cd Week9/project``` to make sure the terminal is in the right location
```
# There was an attempt:
import re
project_name = re.search("/.[^/]+\.py$",__file__)
project_name = project_name.group(0)
ROOT = __file__.strip(project_name)
DIRECTORY_NAME             = ROOT + "/files"
```
Also, replaced an if-else statement with a switch/match statement which is more readable and cleaner.
```
  match play_again[0].lower():
      case "y":
          return True
      case "n":
          return False
      case _:
          print("Reprompt:")
```
**Links:** [cs50p-final-project-repository](https://github.com/corey-richardson/cs50p-2022-final-project) | [matlab-fundamentals-course-progress-report](https://matlabacademy.mathworks.com/progress/share/report.html?id=518eaaf3-1c34-46b0-9d24-7bfc242ba1a3&) | [matlab-fundamentals-course-certificate](https://matlabacademy.mathworks.com/progress/share/certificate.html?id=518eaaf3-1c34-46b0-9d24-7bfc242ba1a3&)




### Day 12: 3/12/2022

**Today's Tasks and Progress:** CS50P Regular Expressions: Working 9 to 5, Regular Um Expressions, Response Validation | README file setup update

**About:** In a file called working.py, implement a function called convert that expects a str in either of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically. | Seperated the logs into groups of 10 days to prevent it from being a 1000 line long block of text; this makes editing easier as time goes on and the file expands. This script setup markdown files titled "day-x-y-log.md" and filled each with the correct formatting. 
```
starts = [1,11,21,31,41,51,61,71,81,91]
ends =   [10,20,30,40,50,60,70,80,90,100]
values = list(zip(starts, ends))

for i, value in enumerate(values):
  with open(name,"a") as file:
      for number in range(start,end+1):
          file.write(f"### Day {number}: \n\n")
          file.write("**Today's Tasks and Progress:**\n\n")
          file.write("**About:**\n\n")
          file.write("**Links:** []()\n\n")
          file.write("\n\n\n")
```
Then once I had uplaoded those to this repository I added the "create link" section which correctly formats the link for each log group to be added to the main README file.
```
with open("links.txt","a") as links:
    to_write = f" - [days-{start}-{end}-log](https://github.com/corey-richardson/100-days-of-code/blob/main/day-{start}-{end}-log.md)\n\n"
    links.write(to_write)
```
**Links:** [working-9-to-5](https://cs50.harvard.edu/python/2022/psets/7/working/) | [regular-um-expressions](https://cs50.harvard.edu/python/2022/psets/7/um/) | [response-validation](https://cs50.harvard.edu/python/2022/psets/7/response/) | [read-me-setup-seperated](https://github.com/corey-richardson/100-days-of-code/tree/main/day-1/read-me-setup/100-days-logs)


MISSED: 4/12/2022

### Day 13: 5/12/2022

**Today's Tasks and Progress:** Reviewing and understanding (or at least attempting to understand) a company software which is literally older than me | Experimenting with OpenAI's ChatGPT | Started working on a decimal/binary/hexadecimal converter

**Links:** [open-gpt-suggested-code-for-read-me-setup](https://github.com/corey-richardson/100-days-of-code/blob/main/day-1/read-me-setup/read-me-setup.py) | [converter](https://github.com/corey-richardson/100-days-of-code/tree/main/converter)




### Day 14: 6/12/2022

**Today's Tasks and Progress:** More investigations on company software | More work on the dec/hex/bin converter | CS50P Week 8 Object-Oriented Programming: Seasons of Love, Cookie Jar, CS50 Shirtificate

**About:** Fixed the previously made functions which were returning wrong values and added the dec_to_hex function.

    Enter the value you want to convert: 255
    Decimal --> Binary: 0b11111111       
    Binary --> Decimal: 0
    Decimal --> Hexadecimal: 0xFF        
    Hexadecimal --> Decimal:
    Binary --> Hexadecimal: 0x0
    Hexadecimal --> Binary:

    Enter the value you want to convert: 256
    Decimal --> Binary: 0b100000000      
    Binary --> Decimal: 0
    Decimal --> Hexadecimal: 0x100       
    Hexadecimal --> Decimal:
    Binary --> Hexadecimal: 0x0
    Hexadecimal --> Binary:

    Enter the value you want to convert: 11101011
    Decimal --> Binary: 0b101010010110001101010011
    Binary --> Decimal: 235
    Decimal --> Hexadecimal: 0xA96353
    Hexadecimal --> Decimal:
    Binary --> Hexadecimal: 0xEB
    Hexadecimal --> Binary:

    Enter the value you want to convert: end
    End
    
 CS50P Completed :)
 All exercises have been completed, now all to do is present my final project which I have roped some friends into helping me on 10/12/22 :)

**Links:** [converter](https://github.com/corey-richardson/100-days-of-code/tree/main/converter) | [seasons](https://cs50.harvard.edu/python/2022/psets/8/seasons/) | [cookie-jar](https://cs50.harvard.edu/python/2022/psets/8/jar/) | [cs50-shirtificate](https://cs50.harvard.edu/python/2022/psets/8/shirtificate/)




### Day 15: 7/12/2022

**Today's Tasks and Progress:** Populate Test Input and Map Data Files | Hardware Testing | Test Data Analysis | STARTED: Mathworks' MATLAB for Data Processing and Visualization Course: Getting Started

**Links:** [matlab-data-proc-and-viz-progress-report](https://matlabacademy.mathworks.com/progress/share/report.html?id=547e0b1f-be01-4f38-b862-3d2fb0e356bc&)




### Day 16: 8/12/2022

**Today's Tasks and Progress:** Finished Test Data Analysis | Software Investigation Task | CS50P Final Project | Mathworks' MATLAB for Data Processing and Visualization Course: Graphics Functions | STARTED CS50X: [Week 0 Previously Completed Months Ago] Week 1: Hello, Mario (Less), Mario (More), Cash. Also working through "Credit" but struggling (C sucks.)

**Links:** [matlab-data-proc-and-viz-progress-report](https://matlabacademy.mathworks.com/progress/share/report.html?id=547e0b1f-be01-4f38-b862-3d2fb0e356bc&) | [CS50X](https://cs50.harvard.edu/x/2022/) | [pset1-hello](https://cs50.harvard.edu/x/2022/psets/1/hello/) | [pset1-mario-less](https://cs50.harvard.edu/x/2022/psets/1/mario/less/) | [pset1-mario-more](https://cs50.harvard.edu/x/2022/psets/1/mario/more/) | [pset1-cash](https://cs50.harvard.edu/x/2022/psets/1/cash/) | [pset1-credit](https://cs50.harvard.edu/x/2022/psets/1/credit/)




### Day 17: 9/12/2022

**Today's Tasks and Progress:** Mathworks' MATLAB for Data Processing and Visualization Course: Graphics Functions, Customizing Graphics Objects | Looking through to try and understand a company MATLAB script with no documentation. 

**About:**

**Links:** [matlab-data-proc-and-viz-progress-report](https://matlabacademy.mathworks.com/progress/share/report.html?id=547e0b1f-be01-4f38-b862-3d2fb0e356bc&)




### Day 18: 10/12/2022

**Today's Tasks and Progress:** Recorded and submitted presentation for CS50P Final Project :)

**About:**

**Links:** []()




### Day 19: 12/12/2022

**Today's Tasks and Progress:** More attempts at PSET1 Credit, still incomplete :') | Mathworks' MATLAB for Data Processing and Visualization Course: Customizing Graphics Objects

**About:** Week 1 is complete but I want to do all the PSETs if possible, maybe I should come back to it down the line

**Links:** [pset1-credit](https://cs50.harvard.edu/x/2022/psets/1/credit/) | [matlab-data-proc-and-viz-progress-report](https://matlabacademy.mathworks.com/progress/share/report.html?id=547e0b1f-be01-4f38-b862-3d2fb0e356bc&)




### Day 20: 13/12/2022

**Today's Tasks and Progress:** RGB Normaliser, Plotter and Dataset Creator | FlightRadar24 3D Flight Data Plotter | Type Speed Tester

**About:** RGB: Gets user to label the colour name of randomly generated and displayed RGB values to use in a ML colour predictor application. Also allows you to see which colours have been included in the dataset already using a 3d coloured scatter plot. | Continuing on from this, I wrote a program which takes lat/long/alt/speed data from FlightRadar24 or any other csv source and plots a 3D scatter plot. The colour of the line changes depending on the speed at that time, and it can be set to animate rotation or in a more interactive mode.

**Links:** [rgb](https://github.com/corey-richardson/100-days-of-code/tree/main/rgb) | [flight-data-plotter]( https://github.com/corey-richardson/100-days-of-code/tree/main/flight_data_plotter) | [type-speed-tester](https://github.com/corey-richardson/100-days-of-code/tree/main/type)

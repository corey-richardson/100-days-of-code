### Day 11:
2/12/2022

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




### Day 12: 
3/12/2022

**Today's Tasks and Progress:** CS50P Regular Expressions: Working 9 to 5

**About:** In a file called working.py, implement a function called convert that expects a str in either of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

**Links:** [working-9-to-5](https://cs50.harvard.edu/python/2022/psets/7/working/)




### Day 13: 

**Today's Tasks and Progress:**

**About:**

**Links:** []()




### Day 14: 

**Today's Tasks and Progress:**

**About:**

**Links:** []()




### Day 15: 

**Today's Tasks and Progress:**

**About:**

**Links:** []()




### Day 16: 

**Today's Tasks and Progress:**

**About:**

**Links:** []()




### Day 17: 

**Today's Tasks and Progress:**

**About:**

**Links:** []()




### Day 18: 

**Today's Tasks and Progress:**

**About:**

**Links:** []()




### Day 19: 

**Today's Tasks and Progress:**

**About:**

**Links:** []()




### Day 20: 

**Today's Tasks and Progress:**

**About:**

**Links:** []()
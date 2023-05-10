### Day 71: 2023-03-10

> 

**Software Engineering Placement at an Aerospace Company:**

More testing; giving it the largest possible chance of failure. <br>
40 data loads, 0 fails. <br>
Try with larger data sets: fails each time. Syncing issue?




### Day 72: 2023-03-13

> 

**Software Engineering Placement at an Aerospace Company:**

Tested the data loads using various delays; they have no impact on the outcome.

**Codecademy's Learn Software Engineering for Data Scientists Skill Path:**

*"Welcome to Software Engineering for Data Scientists" Article*

- apply object-oriented programming, functional programming, and concurrent programming to make your code more efficient
- use unit testing and logging to make your code more relisient
- keep your code up to date and work collaboratively on the same code with git and Github
- use version control and branching
- deploy code with Flask and launch websites with Github
- become proficient in markdown, an invaluable formatting tool
- save time with bash scripts!

<br>

- Lingua Franca: An offline project where you will help a translation service set up its file system and configure its environment.
- ASCII Portfolio: Practice git commits by making some art with the characters found on your keyboard.
- Excursion: Publish a webpage that advertises a product called “Excursion”

*Functional Programming:* <br>
Processing Data From a JSON File, Review, "Create your own Higher Order Functions" Project, Quiz

> Functional programming follows the declarative approach to programming; the programmer describes what needs to be done as opposed to how it is done.

`Complete the following code that computes the sum of all numbers in nums that are divisible by 3.`
```py
nums = (13, 3, 7, 9, 12, 4, 8, 2, 15)
 
total = reduce(lambda x, y: x + y, 
               filter(lambda n: n % 3 == 0, nums))
```
`Given the tuple of numbers nums, complete the code that first finds all numbers that are greater than 10, squares them, and then finds the minimum of those numbers.`
```py
nums = (2, 12, 14, 1, 8, 10, 3, 7, 5, 15)
mn = reduce(lambda x, y: x if x < y else y, 
            map(lambda k: k**2, 
                filter(lambda q: q > 10, nums)))
```
`How would you use map() and reduce() to implement the following loop?`
```py
nums = (1, 2, 3, 4, 5, 6, 7, 8)
s = 0
 
for i in nums:
    s += i**2
```
```py
s = reduce(lambda x, y: x + y, map(lambda h: h**2, nums))
```
`Complete the function that squares all even numbers in a tuple called nums.`
```py
map(lambda k: k**2, filter(lambda x: x % 2 == 0, nums))
```

*Logging:* <br>
"Logging in Python" Article, Introduction to Logging, Creating a Logger, Log Levels, Logging Errors and Messages

> By importing Python’s logging module, we can:
> - Identify the date and time of a custom or error message
> - Format logs to make debugging easier
> - Set severity levels for the logs
> - Output the logs to various streams

> An advantage of using the logging module over console print statements is that the logs can be saved to a file, allowing the log messages to be accessed beyond code execution time.


**Links:** [learning-python](https://github.com/corey-richardson/learning/tree/main/learning-python)




### Day 73: 2023-03-14

> happy pi day

**Software Engineering Placement at an Aerospace Company:**

Wrote Python File I/O script to process output data taking the start end times of a procedure and calculating the time delta; it then also calculates min / max / average code execution time.

```py
from tkinter import filedialog as fd
input_file = fd.askopenfile()

with open(input_file.name, "r") as src:
    output_file = input_file.name.replace(".","_processed.")
    for line in src:
        if not phrase in line:
            continue
        with open(output_file, "a+") as dst:
            dst.write(line)
```

**Links:** [file-io](https://github.com/corey-richardson/learning/blob/main/learning-python/file_io/procedure_call_time_deltas.py) | [learning-python](https://github.com/corey-richardson/learning/tree/main/learning-python)




### Day 74: 2023-03-15

> 

**Software Engineering Placement at an Aerospace Company:**

Robustness testing on data load and software load program on two generations of hardware.

Old build standard is brokey and don't work none; second box does *appear* to work, will test further tomorrow.

**Script for Friend:**

Reviewed and modified a script sent to me by a friend.




### Day 75: 2023-03-16

> 

**Software Engineering Placement at an Aerospace Company:**

More robustness testing on data and software load programs. <br>
20 data loads and 20 software loads all passing `:)`

**Codecademy's Learn Software Engineering for Data Scientists Skill Path:**

*Logging in Python:* <br>
Setting the Log Level, Logging to a File, Logging to Console and File, Formatting the Logs, Using basicConfig(), Review, 'ATM Logging' Project, Quiz

**Codecademy's Introduction to Front-End Engineer Career Path:**

*Semantic HTML:* <br>
Header and Nav, Main and Footer, Article and Section

**Codecademy's Learn Recursion with Python Course:**

*Recursion - Conceptual:* <br>
Introduction to Recursion, Recursion Outline, Call Stacks and Execution Frames, Base Case and Recursive Step, Quiz

*Recursion - Python:* <br>
Building Our Own Call Stack I, Building Our Own Call Stack II, Sum to One with Recursion, Recursion and Big O, Stack Over-Whoa!, No Nested Lists Anymore I Want Them to Turn Flat, Fibonacci? Fibonaccu!, Recursive Data Structures, Quiz

```py
def fibonacci(n):
    print(n)
    # base case
    if n == 0 or n == 1:
        return n
    # recursive step
    return fibonacci(n-1) + fibonacci(n-2) 
```

![ca recursion animation](https://content.codecademy.com/programs/cs-path/recursion-conceptual/CS-Path---Algorithms---Recursion-Intro_v3.gif)

**Links:** [learning-python](https://github.com/corey-richardson/learning/tree/main/learning-python) | [learning-html](https://github.com/corey-richardson/learning/tree/main/learning-frontend/learning-html)




### Day 76: 2023-03-17

> 

**Codecademy's Learn Recursion with Python Course:**

*Recursion vs. Iteration:* <br>
Rules of the Throwdown, When Fibs are Good, Let's Give'em Sum Digits to Talk About, It Was Min To Be, Taco Cat, Multiplication? Schmultiplication!, How Deep is Your Tree?

> who comes up with these lesson names????

**Codecademy's Learn Software Engineering for Data Scientists Skill Path:**

*Learn the Command Line:* <br>

*Viewing and Changing the File System:* <br>
Manipulation: Introduction, ls revisted, ls & Combining Operators, cat, cp Part I, cp Part II, Wildcards, mv, rm, Review, Quiz, "Artusi" Project <br>

*Redirecting Input and Output:* <br>
Redirection: Introduction, Your First Redirect, >, >>, <, |, sort, uniq, grep I, grep II, sed, Review, Quiz, "Athletica" Project <br>

**Links:** [learning-python](https://github.com/corey-richardson/learning/tree/main/learning-python) | [learning-softeng](https://github.com/corey-richardson/learning/tree/main/learning-softeng)




### Day 77: 2023-03-20

> now that this project has been handed off to the test equipement team and i have nothing to do again im so bored - its 44 minutes into the day.

**Codecademy's Learn Software Engineering for Data Scientists Skill Path:**

*Configuring the Enviroment:* <br>

"Configuring the Command Line Environment" Inforrmational, Enviroment: Intro to Enviroment, Nano, Customisation with .bash_profile, Aliases I, Aliases II, Enviroment Variables, PS1 Enviroment Variable, HOME Enviroment Variable, PATH Enviroment Variable, env, Review, Quiz, "Attica" Project, "Lingua Franca" Project, "Windows Command Line" Article <br>

*Learn Git: Introduction to Version Control:* <br>

Introduction: Git and GitHub: <br>
"Introduction: Git and Github" Article, "The Power of Git and GitHub" Video <br>

Basic Git Workflow: <br>
Hello Git, git init, Git Workflow, git status, git add, git commit, git log, Generalisations, "Manhattan Zoo" Project, "SnapFit Robots Inc." Project, "Basic Git Workflow" Quiz, Git Cheat Sheet <br>

Important Git Operations: <br>
Backtracking Intro, Head Commit, Git Checkout


**Links:** [learning-softeng](https://github.com/corey-richardson/learning/tree/main/learning-softeng)



### Day 78: 2023-03-21

> 

**Codecademy's Learn Software Engineering for Data Scientists Skill Path:**

*Learn Git: Introduction to Version Control:* <br>

Important Git Operations: <br>
How to Backtrack: Backtracking Intro, head commit, git checkout, more git add, git reset I, git reset II, git reset review, Generalisations, "Poem Fiasco" Project, "ASCII Portfolio" Project, Quiz, "Handy Git Operations" Article

Introduction to GitHub: <br>
"What is GitHub?" Article, "Set Up with Git and GitHub" Article, "Getting Started with Git and GitHub" Article, "Starting a Code Base" Video, "How to Push Code to GitHub" Video, The GitHub Flow: Introduction, Managing Branches, Adding and Committing Changes, Creating a Pull Request, Reviewing and Merging a Pull Request, Deleting a Branch and Review, Quiz

*Software Engineering in Python II:* <br>

Concurrent Programming: <br>
"What is Concurrent Programming?" Article <br>
"Processes and Threads" Article, Quiz <br>
Concurrent Programming in Python: Introduction, The Threading Module, Using Multiple Threads, Joining a Thread, The Asyncio Module, Multiple Asychronous Tasks, The Multiprocessing Module, Using Multiple Processes, Review, Quiz, "Concurrent Programming" Project

Deployment for Data Scientists: <br>
"Deploying a Simple Python Script with Flask" Article

*Learn Bash Scripting:* <br>

Learn Bash Scripting: <br>
Introduction to Bash Scripting, Variables, Conditionals

**Links:** [learning-softeng](https://github.com/corey-richardson/learning/tree/main/learning-softeng) | [learning-python](https://github.com/corey-richardson/learning/tree/main/learning-python)




### Day 79: 2023-03-22

> 

**Codecademy's Learn Software Engineering for Data Scientists Skill Path:**

*Learn Bash Scripting:* <br>

Learn Bash Scripting: <br>
Loops, Inputs, Aliases,  Review, Quiz, "Build a Build Script" Project

*Learn Git II: Git for Deployment:* <br>

GitHub and Markdown: <br>
"GitHub and Markdown" Informational, "What is Markdown?" Video, "What is Markdown?" Article, "Mastering Markdown" Article, "How to Write a Good README for Your Project" Article

Git Branching: <br>
git branch, branching overview, git branch 2, git checkout, commit on a new branch, git merge, merge conflict I, merge conflict II, delete branch, Generalisations, "Birthday Party" Project, "Ruby Time Calculator" Project, Quiz

Git Teamwork: <br>
Overview, git clone, git remote -v, git fetch, git merge, Git Workflow, git push, Generalisations, "JavaScript Homework" Project, "Recipe Book" Project, Quiz

**Codecademy's Learn Advanced Python 3:**

*Database Operations:* <br>

Querying SQLite Databases with Python: <br>
What is SQL?, Why Use Python to Access SQLite?, Connecting to SQLite in Python, Executing SQL Statements in Python, inserting Multiple Rows with `.executemany()`, Retrieving Data, Using Loops with SQLite, Committing Changes and Closing the Database Connection, Review, "Analysing Hotel Databases with Python" Project, Quiz

**Codecademy's Learn Web Scraping with Beautiful Soup Course:**

Introduction, Rules of Scraping, Requests, the BeautifulSoup Object, Object Types, Navigating by Tags, Website Structure, Find, Select for CSS Selectors, Reading Text, Review

**Links:** [learning-softeng](https://github.com/corey-richardson/learning/tree/main/learning-softeng) | [learning-python](https://github.com/corey-richardson/learning/tree/main/learning-python)




### Day 80: 2023-03-23

> 

**football-manager-setup-script for friend:**

Wrote README documentation for project.

**Codecademy's Learn Web Scraping with Beautiful Soup Course:**

Quiz, "Chocolate Scraping with Beautiful Soup" Project

**Codecademy's computer Science Career Path:**

*Intro to Data Structures:* <br>

"Introduction: Linked Lists" Article

Nodes: <br>
"Nodes" Article, Nodes Python Introduction, Nodes Python Getters, Nodes Python Setters, Nodes Python Review, Quiz

Linked Lists: <br>
"Linked List: Conceptual" Article, Linked Lists Python: Node Implementation, Link List Implementation I, II and III, Linked List Review, Swapping Elements in a Linked List

Doubly Linked Lists: <br>
"Doubly Linked Lists" Article

**Links:** [football-mananger-setup-script](https://github.com/corey-richardson/football-mananger-setup-script) | [learning-python](https://github.com/corey-richardson/learning/tree/main/learning-python) | [learning-compsci](https://github.com/corey-richardson/learning/tree/main/learning-compsci)





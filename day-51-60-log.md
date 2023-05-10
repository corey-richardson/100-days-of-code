### Day 51: 2023-02-07

**Today's Tasks and Progress:** Software Engineering Placement at an Aerospace Company | Codecademy's Learn Intermediate Python 3: Iterators and Generators, Specialised Collections

**About:** Upgrades to certificate-generator for Eng. Week 2023, including GUI file selection and message boxes. | Generators Quiz, 'Event Coordinator' Project | Introduction to Python Sets, Creating a Set, Creating a Frozenset, Adding to a Set, Removing From a Set, Finding Elements in a Set, Introduction to Set Operations, Set Union, Set Intersection

**Links:** [learning-python](https://github.com/corey-richardson/learning/tree/main/learning-python)




### Day 52: 2023-02-08

**Today's Tasks and Progress:** Software Engineering Placement at an Aerospace Company | Codecademy's Learn Intermediate Python 3: Specialised Collections

**About:** Set Difference, Symmetric Difference, Sets Review

**Links:** [learning-python](https://github.com/corey-richardson/learning/tree/main/learning-python)




### Day 53: 2023-02-09

**Today's Tasks and Progress:** Software Engineering Placement at an Aerospace Company | Codecademy's Learn Intermediate Python 3: Specialised Collections

**About:** Sets Review, Sets Quiz | BOGOSORT!

**Links:** [learning-python](https://github.com/corey-richardson/learning/tree/main/learning-python)




### Day 54: 2023-02-10

> i want to change the formatting of everything here but it would take so long to go back and rewrite everything ahhhh

**100-days-of-code Log Files Creation Script Update:** Changed formatting so the name and about sections of a task are together instead of seperate. I will *not* be updating the previous formats, only those going forwards.

```py
starts = [i*10 + 1 for i in range(10)]
ends = [i*10 + 10 for i in range(10)]
values = list(zip(starts, ends))

for i, value in enumerate(values):
    start = values[i][0]
    end = values[i][1]
    name = f"day-{start}-{end}-log.md"

    with open(name,"w") as file:
        pass

    with open(name,"a") as file:
        for number in range(start,end+1):
            file.write(f"### Day {number}: \n\n")
            file.write("> \n\n")
            file.write("** **\n\n")
            file.write("** **\n\n")
            file.write("**Links:** []()\n\n")
            file.write("\n\n\n")
        print("done")
```

This creates:

```md
### Day 54:         <-- Date goes here

>                   <-- Optional Comment

** **               <-- **Task:** 

Task Description

** **               <-- **Task:** 

Task Description

**Links:** []()     <-- Link to relecant repositories
```
**Software Engineering Placement at an Aerospace Company:** 

Peer Review Meeting for a FOUR character change.

> note to self: use spaces not tabs oopsies

**Codecademy's Learn Intermediate Python 3:** 

Python Containers Recap, Introduction to Specialised Containers, Deque, Named Tuple

**Links:** [learning-python](https://github.com/corey-richardson/learning/tree/main/learning-python)




### Day 55: 2023-02-13

> will try to include more of a general overview at what i'm doing at my placement, not neccessarily always coding

**Software Engineering Placement at an Aerospace Company:**  

Ran hardware tests with added log instrumentation. Created a markdown file to document the processes involved in planning Engineers Week 2023 to be used by next years group.

**Codecademy's Learn Intermediate Python 3:** 

Collections: DefaultDict, OrderedDict

**Links:** [learning-python](https://github.com/corey-richardson/learning/tree/main/learning-python)




### Day 56: 2023-02-14

> to non-programmers: happy valentines day <br>
> to programmers: haha youre alone <br>
> programmers dont have valentines

**Software Engineering Placement at an Aerospace Company:**  

Ran more hardware tests, recording two formats of log (RS232 / 1553), and then tracing through the code to determine the path it takes for clues on why it brokey.




### Day 57: 2023-02-15

> 

**Software Engineering Placement at an Aerospace Company:**

Ran more hardware tests, recording two formats of log (RS232 / 1553), and then tracing through the code to determine the path it takes for clues on why it brokey. Again.




### Day 58: 2023-02-16

> 

**Software Engineering Placement at an Aerospace Company:**

More hardware testing / log outputs.

Last minute preparations for Engineers Week, including a script to record scoring for 'Makeathon' competition.

**Links:** [certificate-generator/scores](https://github.com/corey-richardson/certificate-generator/tree/main/scores)




### Day 59: 2023-02-17

> 

**Software Engineering Placement at an Aerospace Company:**

More hardware testing / log outputs analysis.




### Day 60: 2023-02-20

> first day of engineers week 2023 `:)`<br>
> still no one signed up to the makeathon `:(`

**Software Engineering Placement at an Aerospace Company:**

Log output analysis, comparison of time deltas between WinXP and Win10 system; Win10 is ~8x slower.

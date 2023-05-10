### Day 61: 2023-02-21

> 

**Software Engineering Placement at an Aerospace Company:**

Software build and testing: need to add timestamps to log output.

**Codecademy's Learn Intermediate Python 3:** 

Collections: ChainMap, Counter, Container Wrappers, UserDict, UserList

**Links:** [learning-python](https://github.com/corey-richardson/learning/tree/main/learning-python)





### Day 62: 2023-02-22

> 

**Software Engineering Placement at an Aerospace Company:**

Software build including log timestamps.

> ada disgusts me

**Codecademy's Learn Intermediate Python 3:** 

Specialised Collections: UserString, Review, Quiz <br>
Context Managers: Introduction to Resource Management, The 'With' Statement, Class Based Context Manager notes

**Links:** [learning-python](https://github.com/corey-richardson/learning/tree/main/learning-python)




### Day 63: 2023-02-23

> ada is atrocious

**Software Engineering Placement at an Aerospace Company:**

Ran a power up test on hardware, showing as a fail on the program but log output says "all tests passed" so I will proceed. <br>
Loaded profile to hardware. <br>
Ran a map load test, one fail then one pass. Not very consistent. <br> 
Instrumentation I added not apparent in log output. <br>
Checked the build output. The procedure I changed is being overridden. `>:(` <br>
Copied changes I made over the the procedure which is overriding; now getting compile errors in the build output which atleast shows me that it's trying to build from the right file now... <br>
Added `Common_Types` import and semicolon after `end if` statement. <br>
Still won't build. <br>
`Cannot assign to IN parameter` ok. <br>
For Ada, `in` parameters are read only, and `out` parameters are initialised to 0. <br>
`in out` should work: "An in out parameter is like an out parameter except that the previous value is of interest and can be read by the subprogram before assignment." <br>
Doesn't work. <br>
*Cry.* <br>
"Prior to Ada 2012, functions were only allowed to have in parameters." <br>
I imagine the version of Ada we are running is pre-2012. I love industry. <br>
Made a local copy of the variable to use as opposed to the passed in value. <br>
`Var_Copy : STRING := Var;` <br>
**IT BUILDS!** <br>
This all took about 2 and a half hours but I smiled so much when it finally built omg. <br>
ada sucks.

Got so excited by the fact that the software finally successfully built that I forgot to actually use the copy of the variable instead of the original and only realised the mistake as a senior was about to go downstairs to production and test it on the hardware oopsies.

Update: Didn't work lol

<br>

Engineers Week Talks: Next Generation Inertial Sensors Presentation, SSSL Joint Venture Presentation, PZT Gyroscope Engineered Crystal to Usable Signal to Direct Ordinance Presentation

> ### Day 63 and 1/3: 2023-02-24
> 
> **Software Engineering Placement at an Aerospace Company:**
> 
> Hosted a Makeathon Competition for Engineers Week 2023: This event was the result of 2-3 months of planning and preparation including sourcing materials to provide competitors, co-ordinating with the H&S team, (basic) 3D modelling to design a trophy representing aerospace engineering and a Python script to collate the scores. Then celebrated with a >£700 Dominoes order and air hockey with the other YINIs. `:)`
>
> ### Day 63 and 2/3: 2023-02-26
>
> **Archery:** DCAS 45
>
> Scored 525/600 and came 6th place out of 9 other archers in my classification. Personal best score! <br>
> Was asked to be webmaster for the club; will start looking into web development courses.
>
> [Codecademy's Full-Stack Software Engineer Career Path](https://www.codecademy.com/learn/paths/full-stack-engineer-career-path) <br>
> [Codecademy's Front-End Engineer Career Path](https://www.codecademy.com/learn/paths/front-end-engineer-career-path) <br>
> [freeCodeCamp's Responsive Web Design](https://www.freecodecamp.org/learn/2022/responsive-web-design/)


### Day 64: 2023-03-01 

> Optimal End: 2023-03-01 <br>
> Close enough.

**Software Engineering Placement at an Aerospace Company**

**Codecademy's Learn Intermediate Python 3:** 

Resource Management: Class Based Context Managers I, Class Based Context Managers II, Handling Exceptions I, Handling Exceptions II, Introduction to Contextlib, Contextlib Error Handling, Nested Context Managers, Review, Context Managers Quiz, "Aisha's Greeting" Project

**Links:** [learning-python](https://github.com/corey-richardson/learning/tree/main/learning-python)




### Day 65: 2023-03-02

> 

**Software Engineering Placement at an Aerospace Company:**

Reading documentation for a project dated as the 15th of December 2003; ~6 months older than I am `:)`

Added log instrumentation to software load program. VAX CLI Build. Uploaded to hardware and tested.

Dry run build and test for FQT Testing for a 4 character code change.

**Codecademy's Introduction to Front-End Engineer Career Path:**

**Fundamentals of HTML:** <br>
*Learn HTML: Elements:* <br>
Introduction to HTML, HTML Anatomy, The Body, HTML Structure, Headings, Divs, Attributes, Displaying Text, Styling Text, Line Breaks, Unordered List, Ordered List, Images, Image Alts, Videos, Review, Quiz <br>
*Learn HTML: Structure:* <br>
Preparing for HTML, The `<html>` tag, The Head

> ```md
> **Career Path Name:** 
> 
> **Track Name:** <br>
> *Section Name:* <br>
> List of Lessons Completed <br>
> *Section Name 2:* <br>
> List of Lessons Completed 2 <br>
> ```

**Links:** [learning-frontend](https://github.com/corey-richardson/learning/tree/main/learning-frontend) | [learning-html](https://github.com/corey-richardson/learning/tree/main/learning-frontend/learning-html)




### Day 66: 2023-03-03

> 

**Software Engineering Placement at an Aerospace Company:**

FQT test witnessed by Quality Engineering; passed `:)`

**Codecademy's Introduction to Front-End Engineer Career Path:** 

**Fundamentals of HTML:** <br>
*Learn HTML: Structure:* <br>
Page Titles, Linking to Other Web Pages, Opening Links in a New Window, Linking to a Relative Page, Linking At Will, Linking to Same Page, Whitespace, Indentation, Comments, HTML Tags, 'HTML Document Standards' Quiz, 'Intro to Mozilla Developer Network' Article, 'HTML on MDN Web Docs: Debugging' Article, 'Fashion Blog' Project

**Links:** [learning-frontend](https://github.com/corey-richardson/learning/tree/main/learning-frontend) | [learning-html](https://github.com/corey-richardson/learning/tree/main/learning-frontend/learning-html)




### Day 67: 2023-03-06

> 

**Software Engineering Placement at an Aerospace Company:**

Trying to build some software which generates flight profiles and it's not working ahhhhhh VAX is old and I dont like it

> " VAX stands for "Virtual Address eXtension", made by Digital Equipment Coorperation <br>
> While they were quite popular in the '80's and '90's, you won't see very much DEC VAX hardware anymore. "

got it working, go me 




### Day 68: 2023-03-07

> 

**Software Engineering Placement at an Aerospace Company:**

Added more instrumentation to the log output, build using VAX machine, uploaded to hardware and ran software load test.




### Day 69: 2023-03-08

> 

**Software Engineering Placement at an Aerospace Company:**

More instrumented runs, changed a delay, now seems to work `:)` <br>
Conduct repeats to confirm its working. 10 software load passes. 9 data load passes, 1 fail on the very last one before we were going to be done with it `:')`. <br>
Run more data loads with instrumentation to check if the fail is caused by a timeout condition. <br>




### Day 70: 2023-03-09

> 

**Software Engineering Placement at an Aerospace Company:**

Data load tests with instrumentation x 30 to give it the largest possible chance to fail. <br>
It failed 4 times. <br>
Fault codes suggest hardware issue, need to source a new box but I'm not sure any are available for a while yay.

**Fundamentals of HTML:** <br>
*Learn HTML: Tables:* <br>
Introduction to Tables, Create a Table, Table Rows, Table Data, Table Headings, Table Borders, Spanning Columns, Spanning Rows, Table Body, Table Head, Table Footer, Styling with CS, Review, 'HTML Tables' Quiz, 'Wine Festival Schedule' Project <br>
*Semantic HTML:* <br>
Introduction to Semantic HTML


**Links:** [learning-frontend](https://github.com/corey-richardson/learning/tree/main/learning-frontend) | [learning-html](https://github.com/corey-richardson/learning/tree/main/learning-frontend/learning-html)





### Day 81: 2023-03-24

> 

**Created Bubble Sort Script / Big O / Visualiser**

**Links:** [bubble-sort](https://github.com/corey-richardson/learning/tree/main/learning-python/bubble_sort)




### Day 82: 2023-03-27

> i am now 'Club Webmaster' for Yelverton Bowmen whoa i should actually learn what that involves

**Codecademy's Introduction to Front-End Engineer Career Path:**

*Fundamentals of HTML:*

Semantic HTML: <br>
The Aside Element, Figure and Figcaption, Audio and Attributes, Video and Embed, Review, Quiz, "New York City Blog" Project

*Learn CSS: Selectors and Visual Rules:*

Setup and Syntax: <br>
Intro to CSS, CSS Anatomy, Inline Styles, Internals Stylesheet, External Stylesheet, Linking the CSS File, Review

Selectors: <br>
Type, Universal, Class, Multiple Classes, ID, Attribute, Pseudo-Class, Classes and IDs, Specificity, Chaining, Descendant Combinator, Chaining and Specificity, Multiple Selectors, Review

**Codecademy's Learn HTML Course:**

*Forms:* 

HTML Forms: <br>
Introduction to HTML Forms, How a Form Works, Text Input, Adding a Label 

> github codespaces went down and i cant access my notes 

> back online `:)`

Password Input, Number Input, Range Input, Checkbox Input, Radio Button Input, Dropdown List, Datalist Input, Textarea element, Submit Form, Review

**Links:** [learning-frontend](https://github.com/corey-richardson/learning/tree/main/learning-frontend) | [learning-html](https://github.com/corey-richardson/learning/tree/main/learning-frontend/learning-html) | [learning-css](https://github.com/corey-richardson/learning/tree/main/learning-frontend/learning-css)




### Day 83: 2023-03-28

> 

**Codecademy's Learn Sorting Algorithms with Python Course:**

*Bubble Sort:*

Bubble Sort: Conceptual: <br>
Introduction, Bubble Sort, Algorithm Analysis, Review, Quiz

Bubble Sort: Python: <br>
Swap, Compare, Optimised, Quiz

**Updated 'create_contents.py` script:**

Uses Pythons 'string' module to remove punctuation (except hyphens) when formatting each line into contents form: <br> 
`- [{formatted}](#{formatted})` 

```py
import string
for punc in string.punctuation:
    if punc == "-":
        continue
    unformatted = unformatted.replace(punc,"")
```

**Codecademy's Introduction to Front-End Engineer Career Path:**

*Learn CSS: Selectors and Visual Rules:*

Setup and Selectors: <br>
Quiz

Visual Rules: <br>
Introduction to Visual Rules, Font Fmaily, Font Size, Font Weight, Text Align, Color and Background Color, Opacity, Background Image, Important, Review, Quiz

"Healthy Recipes" Project, "Olivia Woodruff Porfolio" Project

**Links:** [learning-compsci](https://github.com/corey-richardson/learning/tree/main/learning-compsci) | [learning-frontend](https://github.com/corey-richardson/learning/tree/main/learning-frontend) | [learning-html](https://github.com/corey-richardson/learning/tree/main/learning-frontend/learning-html) | [learning-css](https://github.com/corey-richardson/learning/tree/main/learning-frontend/learning-css)




### Day 84: 2023-03-29

> 

**Codecademy's Learn Sorting Algorithms with Python Course:**

*Merge Sort:* <br>

Conceptual: <br>
What is a Merge Sort, How to Merge Sort, Merging, Merge Sort Performance, Quiz

Python: <br>
Seperation, Partitions, Creating the Merge Function, Merging, Finishing the Merge, Finishing the Sort, Testing the Sort, Quiz

Created various version merge sort:
- merge_sort_logged.py
    - Uses my logger script to output information such as location in script to a .txt file.
- merge_sort_datalogged.py
    - Uses my logger script to output the list mid-sort to a .txt file.
- merge_sort_timed.py
    - Times how long a merge sort takes
- repeated.py
    - Dynamically plots (Matplotlib) list length vs time taken over a range of values.

**Codecademy's Introduction to Front-End Engineer Career Path:**

*Learn CSS: The Box Model:*

The Box Model: <br>
Introduction to the Box Model, The Box Model, Height and Width, Borders, Border Radius, Padding, Padding Shorthand, Margin, Margin Shorthand, Auto, Margin Collapse, Minimum and Maximum Height and Width, Overflow, Resetting Defaults, Visibility, Review

Changing the Box Model: <br>
Why Change the Box Model, Box Model Content-Box, Box Model Border-Box, The New Box Model, Review

Quiz, "The Box Model in DevTools" Article, "The Box Model in DevTools" Video, "The Box Model: Davie's Burgers" Project


**Links:** [learning-compsci](https://github.com/corey-richardson/learning/tree/main/learning-compsci) | [learning-frontend](https://github.com/corey-richardson/learning/tree/main/learning-frontend) | [learning-html](https://github.com/corey-richardson/learning/tree/main/learning-frontend/learning-html) | [learning-css](https://github.com/corey-richardson/learning/tree/main/learning-frontend/learning-css)




### Day 85: 2023-03-30

> 

**Codecademy's Learn Sorting Algorithms with Python Course:**

*Quicksort:*

Conceptual: <br>
Introduction to Quicksort, Quicksort Runtime, Quicksort Review, Quiz

Python: <br>
Quicksort Introduction, Pickin' Pivots, Partitioning Party, Recurse Rinse Repeat, Quicksort Review, Quiz

*Radix Sort:* <br>

Conceptual: <br>
What is a Radix, Base Numbering Systems, Sorting by Radix, Radix Sort Performace, Radix Review, Quiz

Python: <br>
Finding the Max Exponent, Setting Up For Sorting, Bucketing Numbers, Rendering the List, Iterating Through Exponents, Review

**Links:** [learning-compsci](https://github.com/corey-richardson/learning/tree/main/learning-compsci)




### Day 86: 2023-03-31

> 

**Codecademy's Introduction to Front-End Engineer Career Path:**

*Learn CSS: Display and Positioning:* <br>

Flow of HTML, Position, Position Relative, Position Absolute, Position Fixed, Position Sticky, Z-Index, Inline Display, Display Block, Display Inline-Block, Float, Clear, Review

**Links:** [learning-frontend](https://github.com/corey-richardson/learning/tree/main/learning-frontend) | [learning-html](https://github.com/corey-richardson/learning/tree/main/learning-frontend/learning-html) | [learning-css](https://github.com/corey-richardson/learning/tree/main/learning-frontend/learning-css)




### Day 87: 2023-04-03

> 

**Codecademy's Computer Science Career Path:**

*CS102 - Data Structures and Algorithms: Linked Lists:* 

Doubly Linked Lists: <br>
"Doubly Linked Lists" Article, Node Class and Constructor, Adding to the Head, Adding to the Tail, Removing the Head, Removing the Tail, Removing by Value I, Removing by Value II, Using the List, Review, Quiz

Intro to Programming Exams: Part 1 (86%) and Part 2 (83% but I'm saying 100% because my solution met the requirements `>:(`)

**Codecademy's Learn Sorting Algorithms with Python Course:**

*Radix Sort:* <br>
Quiz

*Sorting Comprehensive:* <br>
'A Sorted Tale' Project

**Links:** [learning-compsci](https://github.com/corey-richardson/learning/tree/main/learning-compsci)




### Day 88: 2023-04-04

> 

**Codecademy's Computer Science Career Path:**

*CS102 - Data Structures and Algorithms: Queues, Stacks and Hash Maps*

Queues: <br>
"Queues: Conceptual" Informational, Queues Python Introduction, Size, Enque, Dequeue, Review, Quiz

Stacks: <br>
"Stacks: Conceptual" Informational, Stacks Python Introduction, Push and Pop, Size I, Size II, Review, Quiz, "Towers of Hanoi" Project

Hash Maps: <br>

Hash Maps Conceptual: Tables, Maps, Hash Map Methodology, Hash Functions, How to Write a Hash Function, Basic Hash Maps, Collisions, Seperate Chaining, Saving Keys, Open Addressing Linear Probing, Other Open Addressing Techniques, Review, Quiz <br>

Hash Maps Python: Creating the Hash Map Class, Creating the Hashing Function, Creating the Compression Function, Defining the Setter, Defining the Getter, Creating an Instance, Handling Collisions in the Setter, Handling Collisions in the Getter, Open Addressing, Open Addressing in the Setter, Open Addressing in the Getter, Review, Quiz

Review: Queues, Stacks, and HashMaps

- Create and use your own **Queue** class and `enqueue()`, `dequeue()`, and `peek()` methods in Python.
- Create and use your own **Stack** class and `push()`, `pop()`, and `peek()` methods in Python.
- Create, understand, and use your own **HashMap** class to create hashing functions and compression functions, handle collisions, and use open addressing in Python.

*CS102 - Data Structures and Algorithms: Algorithms* <br>

Basic Algorithms: <br>
"Introduction: Basic Algorithms" Informational

Big-O Notation: Time and Space Complexity: <br>
"Why Asymptotic Notation?" Article

**Links:** [learning-compsci](https://github.com/corey-richardson/learning/tree/main/learning-compsci)




### Day 89: 2023-04-05

> 

**Codecademy's Computer Science Career Path:**

*CS102 - Data Structures and Algorithms: Algorithms* <br>

Big O Notation - Time and Space Complexity: <br>

Conceptual: <br>
Conceptual: What is Asymptotic Notation, Big Theta, Common Runtimes, Big Omega and Big O, Adding Runtimes, Review, Quiz, "Space Complexity" Article <br>
Python: <br>
Analysing Runtime, Finding the Maximum Value in a Linked List, Sort a Linked List, Stacks vs Queues Runtime, Hashmaps vs Linked Lists Runtime, Quiz

Naive Pattern Searching: <br>

Conceptual: <br>
"Naive Pattern Search: Conceptual" Article<br>
Python: <br>
Iterating Over the Text, Counting Pattern Matches, Testing the Search, Quiz

Brute Force Algorithms: <br>
"Brute Force Algortiths" Article, Quiz

> Lessons previously completed

"Review: Basic Algorithms" Article

- Analyze runtimes and space complexity using Big-O notation, and use that knowledge to write more efficient programs in Python.
- Understand when, why, and how to use recursion, and implement call stacks and common recursive algorithms in Python.
- Understand and implement Naive Pattern Searching in Python.
- Understand what brute force algorithms are, and implement your own Linear Search algorithm in Python.

Sorting Algorithms: <br>
"Introduction: Sorting Algorithms" Article, "Sorting Algorithm Runtimes" Article, "Review: Sorting Algorithms" Runtime

> Lessons previously completed

- Implement your own Bubble Sort, Merge Sort, and Quicksort algorithms in Python.
- Understand each algorithm’s space and time complexity.

*CS102 - Data Structures and Algorithms: Dynamic Programming:* <br>

"Introduction: Dynamic Programming" Informational, Dynamic Programming Quiz, The Knapsack Problem, "Longest Common Subsequence" Project

**Links:** [learning-compsci](https://github.com/corey-richardson/learning/tree/main/learning-compsci)




### Day 90: 2023-04-11

> 

**Codecademy's Computer Science Career Path:**

*Trees and Tree Traversal:*

Trees: Conceptual, Trees: Python: <br>
Introduction, Planting Seeds, Think of the Children, Pruning, Tuning the Pruning, Traversing, Traversing Root to Leaf, Review, Quiz

*Tree Traversal: Breadth-First Search vs Depth-First Search:*

Breadth First Search: Conceptual, Breadth First Search: Python: <br>
Introduction, Values in a Tree, Initialise the BFS Function, The Frontier, Searching for the Value, Don't forget the Children (like in portugal), Review <br>
Depth First Search: Conceptual, Depth First Search: Python: <br>
Introduction, Getting Started, Getting Recursive, Finding a Path, The Finishing Touches, Review, Quiz

*Divide and Conquer Algorithms: Binary Search and Binary Search Trees:*

Binary Search: Conceptual <br>
Binary Search: Python: <br>
Base Case I, Base Case II, The Recursive Steps, Review and Refactor, Iterative Binary Search

Binary Search Trees: Python: <br>
Introduction, Inserting a Value, Retrieving Node by Value, Traversing a Binary Search Tree, Review, Quiz

*Max-Heaps and Heapsorts:*

Max-Heaps Conceptual, <br>
Max-Heaps Python: <br>
Introduction to Max Heaps, Defining Max-Heap, Adding an Element I, Translating Parent and Child Elements into Indices, Adding an Element II, Review, Quiz <br>



**Links:** [learning-compsci](https://github.com/corey-richardson/learning/tree/main/learning-compsci)





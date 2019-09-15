
# Lab 1: Python basics

__Student:__ abcde123

### A word of caution

There are currently two versions of Python in common use, Python 2 and Python 3, which are not 100% compatible. Python 2 is slowly being phased out but has a large enough install base to still be relevant. This course uses the more modern Python 3 but while searching for help online it is not uncommon to find help for Python 2. Especially older posts on sources such as Stack Exchange might refer to Python 2 as simply "Python". This should not cause any serious problems but keep it in mind whenever googling. With regards to this lab, the largest differences are how `print` works and the best practice recommendations for string formatting.

### References to R

Most students taking this course who are not already familiar with Python will probably have some experience of the R programming language. For this reason, there will be intermittent references to R throughout this lab. For those of you with a background in R (or MATLAB/Octave, or Julia) the most important thing to remember is that indexing starts at 0, not at 1.

### Recommended Reading

This course is not built on any specific source and no specific litterature is required. However, for those who prefer to have a printed reference book, we recommended the books by Mark Lutz:

Learning Python by Mark Lutz, 5th edition, O'Reilly. Recommended for those who have no experience of Python. This book is called LP in the text below.

Programming Python by Mark Lutz, 4th edition, O'Reilly. Recommended for those who have some experience with Python, it generally covers more advanced topics than what is included in this course but gives you a chance to dig a bit deeper if you're already comfortable with the basics. This book is called PP in the text.


### A note about notebooks

When using this notebook, you can enter python code in the empty cells, then press ctrl-enter. The code in the cell is executed and if any output occurs it will be displayed below the square. Code executed in this manner will use the same environment regardless of where in the notebook document it is placed. This means that variables and functions assigned values in one cell will thereafter be accessible from all other cells in your notebook session.

Note that the programming environments described in section 1 of LP is not applicable when you run python in this notebook.

### 1. Strings and string handling

The primary datatype for storing raw text in Python is the string. Note that there is no character datatype, only strings of length 1. This can be compared to how there are no atomic numbers in R, only vectors of length 1. A reference to the string datatype can be found __[here](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)__.

[Litterature: LP: Part II, especially Chapter 4, 7.]

a) Define the variable `parrot` containing the sentence _It is dead, that is what is wrong with it_. 

[Note: If you have been programming in a language such as C or Java, you might be a bit confused about the term "define". Different languages use different terms when creating variables, such as "define", "declare", "initialize", etc. with slightly different meanings. In statically typed languages such as C or Java, declaring a variable creates a name connected to a container which can contain data of a specific type, but does not put a value in that container. Initialization is then the act of putting an initial value in such a container. Defining a variable is often used as a synonym to declaring a variable in statically typed languages but as Python is dynamically typed, i.e. variables can contain values of any type, there is no need to declare variables before initializing them. Thus, defining a variable in python entails simply assigning a value to a new name, at wich point the variable is both declared and initialized. This works exactly as in R.]


```python
parrot = "It is dead, that is what is wrong with it."
parrot
```




    'It is dead, that is what is wrong with it.'



b) Count the number of characters (letters, blank space, commas, periods
etc) in the sentence.


```python
blankSpaceCount = parrot.count(' ')
countLetter  = len(parrot) - blankSpaceCount
commaCount = parrot.count(',')
periodCount =  parrot.count('.')

print("\n letter = {0} \n Blank Space = {1} \n comma = {2} \n period = {3}".format(countLetter,blankSpaceCount, commaCount,periodCount))
```

    
     letter = 33 
     Blank Space = 9 
     comma = 1 
     period = 1


c) Separate the sentence into a list of words. Call the list `ParrotWords`.


```python
parrotWords = parrot.split(' ')
parrotWords
```




    ['It', 'is', 'dead,', 'that', 'is', 'what', 'is', 'wrong', 'with', 'it.']



d) Merge (concatenate) `ParrotWords` into a string again.


```python
parrotWords = ' '.join(parrotWords)
parrotWords
```




    'It is dead, that is what is wrong with it.'



### 2. Iteration, sequences and string formatting

Loops are not as painfully slow in Python as they are in R and thus, not as critical to avoid. However, for many use cases, _comprehensions_, like _list comprehensions_ or _dict comprehensions_ are faster. In this assignment we will see both traditional loop constructs and comprehensions. For an introduction to comprehensions, __[this](https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html)__ might be a good place to start.

It should also be noted that what Python calls lists are unnamed sequences. As in R, a Python list can contain elements of many types, however, these can only be accessed by indexing or sequence, not by name as in R.

a) Write a `for`-loop that produces the following output on the screen:<br>
> `The next number in the loop is 5`<br>
> `The next number in the loop is 6`<br>
> ...<br>
> `The next number in the loop is 10`<br>

[Hint: the `range` function has more than one argument.]<br>
[Literature: For the range construct see LP part II chapter 4 (p.112).]


```python
for i in range(5,11):
    print("The next number in the loop is {0}".format(i))
```

    The next number in the loop is 5
    The next number in the loop is 6
    The next number in the loop is 7
    The next number in the loop is 8
    The next number in the loop is 9
    The next number in the loop is 10


b) Write a `while`-loop that repeatedly generates a random number from a uniform distribution over the interval [0,1], and prints the sentence 'The random number is smaller than 0.9' on the screen until the generated random number is greater than 0.9.

[Hint: Python has a `random` module with basic random number generators.]<br>
[Literature: Introduction to the Random module can be found in LP part III chapter 5 (Numeric Types). Importing modules is introduced in part I chapter 3  and covered in depth in part IV.]


```python
import random

randomNumber = random.uniform(0,1)
while(randomNumber < 0.9):
    print("The random {0} number is smaller than 0.9".format(round(randomNumber,2)))
    randomNumber = random.uniform(0,1)
```

    The random 0.56 number is smaller than 0.9
    The random 0.31 number is smaller than 0.9


c) Write code that counts the number of __letters__ in the sentence _It is dead, that is what is wrong with it_.


```python
count = 0
letterCounter = 0 
while(count < len(parrot)):    
    if parrot[count] not in (' ',",","."):
        letterCounter = letterCounter + 1
    count = count + 1

print("Letter Count = ",letterCounter)
```

    Letter Count =  31


d) Write a for-loop that iterates over the list `names` below and writes the following to the screen:

> `The name Ludwig is nice`<br>
> `The name Rosa is nice`<br>
> ...<br>
> `The name Amadeus is nice`<br>

Use Python's string formatting capabilities (the `format` function in the string class) to solve the problem.

[Warning: The best practices for how to do string formatting differs from Python 2 and 3, make sure you use the Python 3 approach.]<br>
[Literature: String formatting is covered in LP part II chapter 7.]


```python
names = ['Ludwig', 'Rosa', 'Mona', 'Amadeus']
```

e) Write a for-loop that iterates over the list `names` and produces the list `nLetters` (`[6,4,4,7]`) that counts the letters in each name. 


```python
for name in names:
    print("The name {0} is nice".format(name))
```

    The name Ludwig is nice
    The name Rosa is nice
    The name Mona is nice
    The name Amadeus is nice


f) Solve assignment d) using a list comprehension.

[Literature: Comprehensions are covered in LP part II chapter 4.]


```python
l = [print("The name {0} is nice".format(name)) for name in names]
```

    The name Ludwig is nice
    The name Rosa is nice
    The name Mona is nice
    The name Amadeus is nice


g) Use a list comprehension to produce a list `shortLong` that indicates if the name has more than four letters. The answer should be `['long', 'short', 'short', 'long']`.


```python
shortLong = ["long" if len(name) > 4  else "short"  for name in names]
print(shortLong)
```

    ['long', 'short', 'short', 'long']


h) Write a loop that __simultaneously__ loops over the lists `names` and `shortLong` to write the following to the screen:

> `The name Ludwig is a long name`<br>
> `The name Rosa is a short name`<br>
> ...<br>
> `The name Amadeus is a long name`<br>

[Hint: use the `range` function and Python's string formatting.]


```python
for i in range(0,len(shortLong)):
    print("The name {0} is a {1} name".format(names[i],shortLong[i]))
```

    The name Ludwig is a long name
    The name Rosa is a short name
    The name Mona is a short name
    The name Amadeus is a long name


### 3. Dictionaries

Dictionaries are association tables, or maps, connecting a key to a value. For instance a name represented by a string as key with a number representing some attribute as a value. Dictionaries can themselves be values in other dictionaries, creating nested or hierarchical data structures. This is similar to named lists in R but keys in Python dictionaries can be more complex than just strings.

[Literature: Dictionaries are found in LP section II chapter 4.]

a) Make a dictionary named `amadeus` containing the information that the student Amadeus is a male, scored 8 on the Algebra exam and 13 on the History exam. The dictionary should NOT include a name entry.


```python
amadeus = {"gender": "male","algebra" : 8, "history": 13}
```

b) Make three more dictionaries, one for each of the students: Rosa, Mona and Ludwig, from the information in the following table:

| Name          | Gender        | Algebra       | History | 
| :-----------: | :-----------: |:-------------:| :------:|
| Rosa          | Female        | 19            | 22      |
| Mona          | Female        | 6             | 27      |
| Ludwig        | Other         | 12            | 18      |


```python
rosa = {"gender": "female","algebra" : 19, "history": 22}
monda = {"gender": "female","algebra" : 6, "history": 27}
ludWig = {"gender": "male","algebra" : 12, "history": 18}
```

c) Combine the four students in a dictionary named `students` such that a user of your dictionary can type `students['Amadeus']['History']` to retrive Amadeus score on the history test.

[HINT: The values in a dictionary can be dictionaries.]


```python
students = {"Amadeus": amadeus, "Rose": rosa, "Monda" : monda, "Ludwig" :ludWig}
students['Amadeus']['history']
```




    13



d) Add the new male student Karl to the dictionary `students`. Karl scored 14 on the Algebra exam and 10 on the History exam.


```python
karl = {"gender": "male","algebra" : 14, "history": 10}
students["karl"] = karl
students
```




    {'Amadeus': {'algebra': 8, 'gender': 'male', 'history': 13},
     'Ludwig': {'algebra': 12, 'gender': 'male', 'history': 18},
     'Monda': {'algebra': 6, 'gender': 'female', 'history': 27},
     'Rose': {'algebra': 19, 'gender': 'female', 'history': 22},
     'karl': {'algebra': 14, 'gender': 'male', 'history': 10}}



e) Use a `for`-loop to print out the names and scores of all students on the screen. The output should look like something this (the order of the students doesn't matter):

> `Student Amadeus scored 8 on the Algebra exam and 13 on the History exam`<br>
> `Student Rosa scored 19 on the Algebra exam and 22 on the History exam`<br>
> ...

[Hint: Dictionaries are iterables, also, check out the `items` function for dictionaries.]


```python
for k, v in students.items():
    print("Student {0} scored {1} on the Algebra exam and {2} on the History exam".format(k,students[k]["algebra"],students[k]["history"] ))    
```

    Student Amadeus scored 8 on the Algebra exam and 13 on the History exam
    Student Rose scored 19 on the Algebra exam and 22 on the History exam
    Student Monda scored 6 on the Algebra exam and 27 on the History exam
    Student Ludwig scored 12 on the Algebra exam and 18 on the History exam
    Student karl scored 14 on the Algebra exam and 10 on the History exam


f) Use a dict comprehension and the lists `names` and `shortLong` from assignment 2 to create a dictionary of names and wether they are short or long. The result should be a dictionary equivalent to {'Ludwig':'long', 'Rosa':'short', 'Mona':'short', 'Amadeus':'long'}.

[Note: Remember that dictionaries in Python are unordered and that the order of the pairs in the above dictionary is arbitrary, you might not get the same order, this is fine.]<br>
[Hint: Use the `zip` function.]<br>
[Literature: zip usage with dictionary is found in LP part II chapter 8 and dictionary comprehensions in the same place.]

### 4. Functions and conditionals

Functions work similarly in R and Python. However, Python has the `def` statement as "syntactic sugar" for creating functions while R use standard assignments when creating functions.

a) Write a function `circle_area(radius)` that computes the area of a circle with radius `radius`. Call the function to show
that it works.

[Hint: The value of $\pi$ is located in the `math` module and needs to be imported.]
[Literature: LP part IV, especially chapter 16.]


```python
import math

def circle_area(radius):
    return(math.pi * (radius**2))

#calling a function
circle_area(12)
```




    452.3893421169302



b) Write a function `circle_area_safe(radius)` which uses an if statement to check that the radius is positive and prints `The radius must be positive` to the screen if it is not, and otherwise calls the `circle_area` function. Also, if the radius is not positive the `circle_area_safe` function should return `None`.

[Literature: LP part III chapter 12.]


```python
def circle_area_safe(radius):
    if(radius < 0):
        print("Radius must be positive")
        return None
    else:
        return circle_area(radius)
#calling a function when radius is not positive    
circle_area_safe(-12)


```

    Radius must be positive



```python
#calling a function when radius is positive
circle_area_safe(12)
```




    452.3893421169302



c) Recreate the `circle_area_safe` function (call this version `circle_area_safer`) but instead of printing a message to the screen and returning `None` if the radius is negative, _raise_ a ValueError exception with suitable error message as argument.

[Literature: Exceptions are introduced in part I, page 333 and part III chapter 11 page 374 and defined in depth in part VII, raising exceptions part VII page 1107.]


```python
def circle_area_safe(radius):
    if(radius < 0):
       raise ValueError('Radius must be postive')
    else:
        return circle_area(radius)
    
circle_area_safe(-12)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-53-f12b42f8f757> in <module>()
          5         return circle_area(radius)
          6 
    ----> 7 circle_area_safe(-12)
    

    <ipython-input-53-f12b42f8f757> in circle_area_safe(radius)
          1 def circle_area_safe(radius):
          2     if(radius < 0):
    ----> 3        raise ValueError('Radius must be postive')
          4     else:
          5         return circle_area(radius)


    ValueError: Radius must be postive


### 5. File I/O

File I/O in Python is a bit more general than what most R programmers are used to. In R, reading and writing files are usually performed using file type specific functions such as `read.csv` while in Python we usually start with reading standard text files. However, there are lots of specialized functions for different file types in Python as well, especially when using the __[pandas](http://pandas.pydata.org/)__ library which is built around a datatype similar to R DataFrames. Pandas will not be covered in this course though.

[Literature: Files are introduced in LP part II chapter 4 and chapter 9.]

The file `students.tsv` contains tab separated values corresponding to the students in previous assigments.

a) Iterate over the file, line by line, and print each line. The result should be something like this:

> `Amadeus	Male	8	13`<br>
> `Rosa	Female	19	22`<br>
> ...

The file should be closed when reading is complete.

[Hint: Files are iterable in Python.]


```python
lines = open("students.tsv", 'r')

for line in lines:
    print(line)
lines.close()
```

    Amadeus	Male	8	13
    
    Rosa	Female	19	22
    
    Mona	Female	6	27
    
    Ludwig	Other	12	18
    
    Karl	Male	14	10


b) Working with many files can be problematic, especially when you forget to close files or errors interrupt programs before files are closed. Python thus has a special `with` statement which automatically closes files for you, even if an error occurs. Redo assignment 6a using the `with` statement.

[Literature: With is introduced in LP part II chapter 9 page 294.]


```python
with open('students.tsv', 'r') as f:
    for line in f:
        print(line)
```

    Amadeus	Male	8	13
    
    Rosa	Female	19	22
    
    Mona	Female	6	27
    
    Ludwig	Other	12	18
    
    Karl	Male	14	10


c) Recreate the dictionary from assignment 3c by reading the data from the file. Using a dedicated csv-reader is not permitted.

[Hint: Check out the `split` function and look up how to express tab characters.]

d) Using the dictionary from 3c, write the sentences from 3e to a new file, called `students.txt`.

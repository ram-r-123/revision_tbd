# Python Learning Materials - Compiled Notes

*This document contains markdown content extracted from Jupyter notebooks*

---

# Collections

## Collections - Main Content

In the previous notebook we had a look at variables. Often, however, we need a convenient way to represent a collection of data (think a series of proteins, all codons that code for an aminoacid, etc). Python offers several very handy built-in types to deal with this. In the following we will learn about *lists*, *tuples* and *dictionaries*.

# Lists

Lists are the workhorse data type in Python, so it's important to understand them well. A list is essentially an ordered collection of items: 

Since each value in Python "knows" its type, there's no danger in putting together different types of values (however, in general this is better avoided):

**NOTE ON EXAMPLES:** Toy examples on strings and lists get boring quickly. For this reason, I am sourcing some of the examples from Bioinformatics, aka the Empire of Strings. These examples reflect meaningful real-world processing and data, however basic. You don't actually need to know any Biology, and if the terminology bothers you, replace any words you don't like with *foo*, *bar*, *spam* and *ham* - for our purposes, they are just strings.

### Indexing

You can access individual elements of the list by *indexing*. This is done with the ```[]``` operator:

Incidentally, the [] operator also works for strings:

so that this is valid code:

A few other handy tricks:

You can, of course, use indexing to modify lists:

### Operations on lists

The ```dir``` command gives you a handy way to list operations defined for a type (really methods defined for an object). Disregard the entries beginning and ending with ```__``` that have to do with the internal representation of the object. Let's try this on a list:

```append``` and ```pop``` attach or remove an element from the "tail" of the list. They can be used to implement a LIFO (last in first out) queue, also known as a stack.

To concatenate two lists, use ```extend```

Note that strings are sorted in alphabetical order. More details on sorting available [here](https://wiki.python.org/moin/HowTo/Sorting)

### Lists comprehensions

There is a handy way of defining lists in Python starting from other lists. This is similar to what is done with sets in mathematics. Consider the following set: $A=\{1,2,3,4,5\}$. You can define $B=\{3x | x\in A\}$ (read 3 times x for x in A), which explicitly means  $B=\{3,6,9,12,15\}$. The same is possible with Python lists:

We can also use conditionals in comprehensions to pick elements that satisfy a particular property (we will cover conditionals in detail later on):

This can be used to operate on all elements of a list:

### A common pitfall

Be warned that the name of a list is just a reference to a memory area where the list elements are stored. Thus a copy of a list creates another way of accessing the same list containing the exact same objects, not different list or different objects. This makes the copy operation very efficient, but it can lead to some surprises:

If you do want to copy all elements one by one, you can use indexing to enumerate all the elements of list *a* and assign the resulting ~~sub~~list to list *b*:

# Tuples

Tuples are immutable lists. They are more efficient than lists and can be used as keys for dictionaries (see below); with the obvious modificatios, they can be used like lists.

Notice that methods to change the elements are missing

This is slightly tricky:

In this example we are not changing the tuple, we are actually creating the new tuple (1,2,3,4,5) and assigning it to *a* instead than the old one

# Dictionaries

You can think of lists and tuples as a series of variables indexed by an integer. Dictionaries are series of variables indexed by an arbitrary object, typically (but by all means not always) a string:

You can add items one by one to an empty dictionary {}:

**UPDATE:** The language keeps evolving, and as of Python 3.6 a new implementation of ```dict``` was introduced that is more efficient, and also stores the keys in *insertion order*. Since version 3.7, this has become part of the standard, so printing a dictionary or extracting its keys (see below) will return the keys in the order they were inserted.

### Keys and values

You can display the keys and values contained in a dictionary using the corresponding methods:

Or you can have them all together:

Trying to look up an unexisting key can led to an error:

So it may be better to check (this is a conditional expression, more on this later):

Or you can play it safe:

You can use ```del``` to delete items (or you can ```pop``` the dictionary, which returns the deleted item):

We can ```update``` a dictionary with values from another:

And finally, let's turn this around - let's try to use the names as keys, and the three-letter codes as values:

Note that turning a dictionary on its head in this way is not normally possible, as two or more keys may have the same value (meaning you cannot in general use the values as keys) - nor is it necessarily useful, but it's a good exercise nevertheless!

### Dict comprehensions

Removing printouts and intermediate variables, the above solution isn't that verbose:

however, there is a more elegant way of doing it, by using a **dictionary comprehension**. From the [documentation](https://www.python.org/dev/peps/pep-0274/), "Dict comprehensions are just like list comprehensions, except that you group the expression using curly braces instead of square braces. Also, the left part before the ```for``` keyword expresses both a key and a value, separated by a colon. The notation is specifically designed to remind you of list comprehensions as applied to dictionaries." In our case, this what the required comprehension would look like:

the analogy with list comprehensions is evident. You can find a collection of increasingly intricate examples [here](https://towardsdatascience.com/10-examples-to-master-python-dictionary-comprehensions-7aaa536f5960) - you may want to try running and editing them in order to make sense of them.

**(C) 2014,2020 Fabrizio Smeraldi** ([f.smeraldi@qmul.ac.uk](mailto:f.smeraldi@qmul.ac.uk) - [web](http://www.eecs.qmul.ac.uk/~fabri/)), all rights reserved. In: "Computer Programming", School of Electronic Engineering and Computer Science, Queen Mary University of London.

## Collections - Solutions

### Note

You may find it easier to do these exercises directly in the notebook. Feel free to insert text with your comments or write your notes as you proceed. The notebook is yours for keeps.

### List basics

Create an empty list [] called ```myList```.
* Add the following words using the ``` .append() ``` method:
    * "the"
    * "quick"
    * "brown"
    * "fox"
    * "jumps"
    * "over"
* Print the list to check all words are there
* Create another list called ```barker``` containing the words "the", "lazy", "dog"
* Use the ``` .extend() ``` method to add the ```barker``` list at the end of ```myList```
* Print the result
* Print the first word of the list
* Print the word "fox"
* Print the length of the list (use ```len()```) 
* Print the last word of the list using ```myList[len(myList) - 1]```
* Print the last word of the list using ```myList[-1]```
* Print the first three words and the last three words
* Print the sublist ["brown", "fox"]
* Use ```.remove()``` to delete "the"
    * use the ```in``` operator to check if "the" is still in the list
    * inspect the list; call ```.remove()``` again
* Use ```.index('lazy')``` to find the index of the word "lazy".
    * Check the result and store it in variable i
* Use ```del myList[i]``` to delete the word "lazy"
* Use ```.sort()``` to sort the list

### List comprehensions

Use the function ```range() ``` to create a lists of numbers from 0 till 10. Assign it to variable ```nums```

Use a comprehension to create a list of the treble of each number in ```nums```

Use your favourite editor to write a program that asks a user for a number between 1 and 10 and prints a list with the multiplication table for that number

Write a comprehension to create the list ```["#", "##", "###",...]``` (up to 10 hashes)

Write a list comprehension to compute the squares of all the numbers in ```nums```. Call this ```squares``` 

A trickier one: create a list that for each x in ```nums``` and y in ```squares``` contains the sentence "The square of *x* is *y*". Hint: try printing ```zip(nums, squares)```. Then, ```[ ... for (x,y) in zip(nums, squares)]```

### Hunt for Red October

A secret message meant for the submarine Red October has been intercepted by your radio officer. Your intelligence team has established that every third character is good, while the rest is noise. However they cannot say if the secret message starts with the first, second or third character of the scrambled text, nor whether the scrambled text has been transcribed in the correct order or in reverse order.

* use ```list()``` to convert the scrambled message to a list
* index as appropriate to extract every 3rd character (this requires slicing - see the theory notebook)
* try starting with second character, or if that doesn't work the third character of the scrambled message
* use the ```.reverse()``` list method to reverse the scrambled message
* again, try starting from the second and third characters
* use ``` ''.join(some_list)``` to convert the lists back to strings for printing

Can you do the same without converting the scrambled message to a list? (Hint: there's only one step that breaks down)

For more examples of slicing, see this [tutorial](https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/).

### IATA codes

IATA codes are three-letter standard codes that identify airports.

* Create an empty dictionary {} called ```iata_codes```
* Add the IATA code for a few airports and their names, using codes as keys:
    * "LHR": "London Heathrow"
    * "DOG": "Dongola (Sudan)"
    * "CAT": "Cascais (Portugal)"
    * "GOI": "Goa (India)"
    * "GOA": "Genoa (Italy)"
    * ...add your own!
* Print the dictionary and notice the order of the elements
* Print out the list of ```.keys()```
* Print the list of ```.values()```
* Print the list of ```.items()```
* Use the ```in``` operator to find out if "CAT" is a known IATA code
* Use ```.pop() ``` to delete key "DOG"

Write a program that asks the user to enter an IATA code, checks that the code is 3 letter long (printing an error message if it isn't) and converts it to uppercase. The program should then print  "Airport name: " followed by the name of the airport if the code is in the dictionary, or by "unknown" otherwise. Use the ```.get()``` method of Python dictionaries.

### With complements - take 2

The double helix of DNA is made of 2 strands, that latch on to each other like a zipper. Each strand is said to be the "complement" of the other (see the picture [here](https://en.wikipedia.org/wiki/DNA_replication)). Given a sequence, the complement is obtained by substituting ```'A'``` for ```'T'```, ```'T'``` for ```'A'```, ```'C'``` for ```'G'``` and ```'G'``` for ```'C'```, so that for instance the complement of ```"GATTACA"``` is ```"CTAATGT"```.

Write a program that takes a DNA sequence as input and outputs its complement.
* use ```list()``` to convert the input string to a list
* build a dictionary with the complement of each nucleotide
* use this dictionary in a list comprehension to generate the list of complements
* use ``` ''.join(complement_list) ``` to turn the resulting list into a string

### Counting vowels

Write a program that counts the relative frequency of vowels in a string. Your program should
* ask the user to enter a string
* create a dictionary listing the number of time each vowel occurs in that string, such as for instance
    ``` {'A': 1, 'E': 4, 'I': 2, 'O': 1, 'U': 2}```
  (use the ```str.count``` method)
* obtain the total number of vowels in the string (use the ```sum()``` function), and divide the number of occurences of each vowel by the total to get a relative frequency for each vowel
* print out the results as a nice table.

For instance if the input is ```"A* Algorithm."``` your program should output
```
A: 0.5
E: 0.0
I: 0.25
O: 0.25
U: 0.0
```
(consonants, punctuation and other symbols are discarded; both lowercase and uppercase vowels count).
Once you are satisfied that your program works, add the following line at the top:
```
from excerpts import *
```
(this assumes that the excerpts.py file is in the same directory as your program). This will import two excerpts (about 60 lines of text each) from 19th century literary works in English and in Italian, in the variables ```moby_dick``` and ```pinocchio```. Modify your program so that it processes those strings instead of keyboard input and see what you get.


(Adapted from [Kasper Munch](https://github.com/kaspermunch))

### Going bananas

Create a dictionary called ```prices```. Add the following values:
```
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
```

Extract the list of prices and use ```sum()``` on that list to get the total price.



Then create another dictionary called ```stock``` that lists the number of items for each fruit, example
```
"banana": 5,
"apple": 12,
"orange": 6,
"pear": 2
```

Compute the money you would make by selling all the ```stock``` at the given ```price```.
Hint: start by obtaining the list of keys. Then use a list comprehension to multiply the
stock by the price for each fruit.

(adapted from [Erle Robotics](https://erlerobotics.gitbooks.io/erle-robotics-learning-python-gitbook-free/content/lists/exercises_list_and_dictionaries.html))

### Lord of the rings

Lists and dictionaries can be listed in arbitary ways. It is very common to find a dictionary with some keys corresponding to lists. Try to do the following exercise (from [Erle Robotics](https://erlerobotics.gitbooks.io/erle-robotics-learning-python-gitbook-free/content/lists/exercises_list_and_dictionaries.html)):

Given the following dictionary:
```
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
```

* Add a key to inventory called 'pocket'.
* Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.
* ```.sort()``` the items in the list stored under the 'backpack' key.
* Then ```.remove('dagger')``` from the list of items stored under the 'backpack' key.
* Add 50 to the number stored under the 'gold' key.


### Bella Napoli

Create a dictionary called ```toppings```. Add the names of at least three pizzas as keys. Each key should correspond to the list of toppings for that pizza.

* Print the dictionary.
* Use the ```in``` operator to check if the toppings for ```"margherita"``` include ```"pineapple"``` (hint: that should return ```False```).
* Write a list comprehension to list the names of all pizzas that have a specific topping (eg all pizzas that have olives).

---

# Conditional statements

## Conditional statements - Main Content

# Conditional structures

In order to allow coding arbitrary operations, a programming language needs to provide three types of control structures to steer the execution flow:
* sequential execution
    * commands executed in the order in which they are written
    * what we have seen so far
* **conditional execution**
    * branch on conditions
    * different parts of code executed depending on data
* loops
    * repeat a set of actions many times
    

# Conditional statements: if-else

The ```if```-```else``` statement is the basic conditional, present in most programming languages. In detail, it looks like this:
```
if CONDITION:
    Block1
else:
    Block2
    
```
the indentation is important!
Example:

Or, if no alternative action is required:

### Watch your tabs

In the example above, indentation is essential. This won't work:

Indentation marks a **block**. You can think of a block as a group of statements that behaves like a single statement from the point of view of if/else, loops, function definitions, etc. Example: 

# Conditional statements: if-elif-else

We can code more than two alternatives using the ```elif``` keyword

Note that only the first test that's true triggers the execution of the corresponding block. For instance, if ```kettle_temp``` is 96 then it is also larger than 90, but "Brew green tea" is not printed.

# Boolean expressions

The condition in an ```if``` statement is a Boolean expression. That is anything that evaluates to either ```True``` or ```False```, typically the output of **comparison operators**. See [here](http://www.tutorialspoint.com/python/comparison_operators_example.htm) for a list and an example. Here are the main ones:

| Operator | Description   |
|----------|------------|
| ==       | equality   |
| !=  | not equal  |
| >  or  <   | greater/less than |
| >=  or  <= | as above, with equality |

Example:

The same operators can be applied to strings:

You can combine several comparison operators with each other using **relational operators**:

| Operator  | Name        | Description                                             |
|:-----------:|-------------|---------------------------------------------------------|
|  and      | logical AND | True if and only if both operands are true              |
|  or       | logical OR  | True if at least one operand is true                    |
|  not      | logical NOT | True if operand false and vice-versa                    |

Example:

Note that the comparisons return Boolean values that are combined by the relational operators. In another example, we may use relational operators to act directly on Boolean variables: 

Of course, you normally deal with variables of unknown value. So, putting it all together:

# Conditional expressions

The ```if```/```else``` constructs explored above are *statements*, and as such do not return any value. Sometimes we would like a shorthand notation for an expression that changes value according to some condition. For instance:

Another example (note that here we have to have an else in any case, even if when a>=0 we do not want to change anything - the expression still needs to yield some value):

# Reminder: list comprehensions

We already  encountered a conditional of sorts before:

**(C) 2014,2020 Fabrizio Smeraldi** ([f.smeraldi@qmul.ac.uk](mailto:f.smeraldi@qmul.ac.uk) - [web](http://www.eecs.qmul.ac.uk/~fabri/)), all rights reserved. In: "Computer Programming", School of Electronic Engineering and Computer Science, Queen Mary University of London.

---

# Errors and Exceptions

## Errors and Exceptions - Main Content

# Types of errors

There are two types of errors: 
* **syntax errors**: the compiler spots them, you fix them
* **runtime errors**: can be handled via the *exception* mechanism
* **logical errors** (aka **bugs**): here your program may not even crash, but it misbehaves (eg messes up your data) because of a logical flaw in the code. If I knew how to catch these I would be a rich man, so don't let's talk about them any longer. As I said, two types.

Syntax errors are the most common type of error you encounter when you start programming, but are easily spotted and fixed (the interpreter helps you a lot):

Runtime errors are much trickier, as they are conditions that depend on program execution and/or on the data the user may enter:

In the above example, the code is correct and the program normally works; however, errors may arise because of the data (in itself acceptable or otherwise) supplied by the user. These errors trigger *Exceptions*, which (if unhandled) lead to program termination. Notice here that the name of the built-in exception (such as *ZeroDivisonError* or *ValueError*) describes what has happened.

Typical among operations that can cause exceptions are input/output operations (especially involving files). One can try to open a file that does not exist, write to a directory without writing permissions, or encounter unexpected input while reading the file. 

# Exception handling

An exception need not be the end of the program: it can be handled with the following construct:

```
try:
    # anything that can cause errors
    BLOCK
except <EXCEPTION> [as e]: # type of exception and "as" clause are optional
    BLOCK
```

Here ```<EXCEPTION>``` stands for the type of exception we want to handle. Technically it is a class, so that the actual exception is (you guessed it) an object of that class; it gets assigned to whatever variable is specified in the optional ```as``` clause, so that you can inspect it in the following ```BLOCK```. This will become clearer with the examples below.

For instance, we can modify the previous code as follows:

As we see, the problem here is that all errors trigger the "You loser" response, while for instance the program should ask for input again if the user did not enter numbers. It is possible to use more than one ```except``` clause, each restricted to handling only one type of errors:

restricting ```except``` clauses in this way is actually a good idea, because a "wildcard" ```except``` can mask a true programming error.

As said exceptions are actually objects, and carry some information about the error that has occurred. This can be shown to the user by printing the exception, or handled programmatically via the ```args``` attribute of the exception object:

# Exception propagation

In general, an exception will happen in some function or method that has been called by some other function or method, which in turn may have been called by something else. An exception will propagate up the call stack until it is handled. This means that an exception happening in a function can be handled by the caller. If nothing handles it, the exception causes the program to terminate. Consider the following examples:

As we can see, an exception happens in function ```average```, called by the main program, if the list passed to ```average``` is empty. This exception can be handled inside the function as follows:

or it can be handled by the caller:

the exception still happens in the function, but it is propagated back to the caller and handled there.

# Rolling your own

Especially when programming a library, it may be useful to declare your own exceptions. You can do that by extending the ```Exception``` class, as shown below. In a Bioinformatics library, for instance, a ```SeqError``` may be defined to flag errors occurring while dealing with a DNA sequence (in this case, a search for a character that is not a nucleotide). When the condition occurs, your code can use the keyword ```raise``` to throw a ```SeqError``` than then behaves like any other exception, and can be handled in a ```try``` - ```except``` clause.

Note that the ```Exception``` class provides some boilerplate code, so that if you simply define ```SeqError``` as follows:
```
class SeqError(Exception):
    pass
```
you get almost the same behaviour (don't take my word for it, try it!). The point here is to show you that these are *bona-fide* objects and as such they are entirely customisable.

In fact, exception handling can even make use of the inheritance relations among exception classes, as described in the video below.

All [built-in exceptions](https://docs.python.org/3/library/exceptions.html) are listed in the Python documentation; each of them can obviously be extended, should you ever wish to tweak them.

**(C) 2014,2020 Fabrizio Smeraldi** ([f.smeraldi@qmul.ac.uk](mailto:f.smeraldi@qmul.ac.uk) - [web](http://www.eecs.qmul.ac.uk/~fabri/)), all rights reserved. In: "Coding for Scientists", School of Biological and Chemical Sciences, Queen Mary University of London.

---

# Exceptions

## Exceptions - Solutions

### You can handle that

...even if you don't quite know precisely what that function does. Call function ```havoc()``` a few times and see what happens. Then try to handle the resulting exception in the calling code (not inside the function) by printing it. Your can even write code that keeps calling ```havoc()``` until it runs without errors (I wouldn't recommend that as a general debugging strategy, though!)

### Quadratic equation

Consider the function ```quad()``` below that computes the roots of a quadratic equation. Write a program that asks the user for the parameters, calls the function, prints the results and handles all exceptions. In case of error, your program can extract the offending parameters from the ```.params``` attribute of the exception and, for instance, print them (note that since ```a```, ```b```, and ```c``` are not passed to the constructor of ```QuadError``` but stored in an attribute, they do not get printed automatically when the exception object is printed).

# File input/output

A typical situation in which exceptions can occur is when handling files. For instance, the file you want to read may not exist, or you may not have write permissions for the directory to which you are trying to write.

Take some code you have written to read a text file and change the name of the file to something non-existing. See what happens. Modify the code so that the exception is handled correctly (for instance, by asking the user for a new filename or printing a message and quitting cleanly).

### Dictionary lookup

Try the following code as is, then try it removing the ```if``` statement. Looking up a key that does not exist will cause an exception. In place of the ```if```, use exception handling to print the goodbye message and quit.

### More information

Look up the detailed explanations and examples on the [RealPython](https://realpython.com/python-exceptions/#exceptions-versus-syntax-errors) website. Feel free to copy some of their examples and try them here below.


---

# Files

## Files - Main Content

# Reading and writing files

Entering input via the keyboard and reading the output from a console obviously isn't a very convenient way of dealing with large amounts of data. Most of the times, we will want to operate on files (eg TXT, CSV or JSON files to mention a few). Most commonly, files are used to save data entered by the user (think of a .doc file). However, files can be downloaded from some online API or database; they can also be used to store intermediate results of computation for further processing, and to store large amounts of output during batch processing. Dealing with files is luckily straightforward in Python.

Note that since the files we will work with sit in the same directory (and on the same machine) as the notebook, you may need to view and edit them through the Jupyter Notebook interface rather than through your local text editor, according to where you are running.

# Text vs Binary files

There are essentially two types of data files: *text* and *binary*. 

**Text files** can be opened and modified with a plain text editor such as gedit, emacs or notepad. They are not necessarily written in plan English: a Python program, an [HTML](https://en.wikipedia.org/wiki/HTML) page,  a [JSON](https://en.wikipedia.org/wiki/JSON) file, an [XML](https://en.wikipedia.org/wiki/XML) file, a [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) file, a [FASTA](https://en.wikipedia.org/wiki/FASTA_format) file or a [PDB](https://en.wikipedia.org/wiki/Protein_Data_Bank_(file_format)) file are all text files. While not always meant for human consumption, text files are generally somewhat human-readable and are portable across different operating systems and editors, with very minor niggles. The disadvantage is that they take up a lot of space on the disk.

**Binary files** contain data in the internal machine representation. They are less portable and are generally used either to talk directly to the machine, or to store large amounts of data efficiently, or to protect intellectual property. Python bytecode (.pyc) files, compressed (.zip) files, Microsoft Word (.doc) files, executable files (.exe on Windows systems), image files (.jpg, .gif), and music files (.wav, .mp3) are all examples of binary files. An attempt at opening them in a text editor will only show gibberish on the screen.

Happily many of the file types used in web programming, bioinformatics and other fields are text files with open format specifications, so we will not worry about binary files here (specialised libraries exist for the most common file types anyway). It is important however to remember, in your future professional life, that sometimes what you really need is not a bigger disk, but  only a more compact data representation.


# Reading files

Unless they just contain plain text meant for humans (eg a README file), text files normally follow detailed specifications that describe how the information they contain is formatted, and make it possible to retrieve and process it automatically. One of the simplest text file specifications is the [FASTA](https://en.wikipedia.org/wiki/FASTA_format) format, extremely common in Bioinformatics. It is used to store the sequence of proteins (ie, their chemical composition). Essentially, a FASTA file looks like this:
```
> Accession code | Name of protein
THEENTIRESEQUENCEARRANGEDONSEVERALLI
NESWITHOUTSPACESANDBROKENUPWITHNEWLI
NESINARBITRARYPLACESTOMAKEITLOOKTIDY
```
To see an actual example, run the cell below and click on the link it creates. If your browser won't open it, go to File->Open in the Jupyter interface or use a text editor of your choice (note: this example requires the file to exist and to be in the same directory as this notebook).

Note the ```>``` sign that marks the header line and the ```|``` sign that separates the accession code from the name of the protein. The challenge is to read the file retrieving the accession code, the protein name and the entire sequence as one string, discarding the newlines that are just pretty-printing.

Reading this file in Python requires first a call to ```open()```, that returns a *file handle*:

the ```"r"``` indicates we are opening this file for *reading*. The *handle* that's returned is a convenience object used by Python to keep track of all data relative to the file (location, type, position, etc). Just treat it as you would any other Python object and assign it to a variable.

### Using ```readlines()```

An easy way to read all the file is now to use ```readlines()```:

As you can see, ```readlines()``` returns a list of strings, each corresponding to a line in the file. This exhausts the contents of the file. All that remains to do now is to close the file to free the associated system resources:

Note that you cannot run ```readlines()``` on the same file twice without "rewinding" it (for example by closing it and reopening).

### Using ```readline()```

Using ```readlines()``` is less than ideal as it slurps the entire file up in one go, which is somewhat inconvenient as the file may contain different types of data (in this case the header and the protein proper) or may be too large to fit entirely in the memory. In general, it is better to process it one line at a time, using repeated calls to ```readline()```. In this case, this also gives us the chance to assemble the protein into a single string. Here is how it works:

### Using a ```for``` loop:

There is a more "Pythonic" way of doing this that uses the fact that a file is an *iterable* and therefore can be read directly using a ```for``` loop:

Reading other text file formats obviously requires a knowledge of the relevant format specification. Common formats such as JSON and CSV (see below) are supported by Python through the standard library (see for example [here](https://docs.python.org/3/library/json.html)), others are supported through third party libraries (eg [Biopython](https://biopython.org/)). In the other cases, the general strategies described above coupled with some experimentation should hopefully see you through.

# Writing files

Writing files is not much more of a hassle than reading them. In fact, the main steps are the same:
* open a file
* write the content
* close it

The only differences are that the file must be opened in write mode, and that the ```write()``` method must be used to actually write data to it.

Example:

Try running the example above twice, and check the *greetings.txt* file each time. You will see that the content gets overwritten. If you do not like that behaviour, change ```"wt"``` to ```"at"``` in the ```open``` statement to open the file for *appending*. See for yourself what that does. Appending to a non-existing file just creates it.

So for instance, writing your imaginary protein out in FASTA format can be done this way:

# CSV Files

The [CSV (Comma-Separated Values)](https://en.wikipedia.org/wiki/Comma-separated_values) file format is a popular text file format that lists each record on a separate line. Data fields for the same entry are separated by commas (or occasionaly semicolons or tabs). Many popular packages can output data as CSV files, among others Excel. Reading and writing csv files in Python is easy, either directly or via the ```csv``` module.

Example - the file *marksheet.csv* contains the following text:

```
Name, Surname, Mark
John, Smith, 50
Anne, Larsson, 65
Emiliano, Zapata, 95
Donald, Duck, 40
```

When you click on a link to this file, the browser is likely to suggest opening it as a spreadsheet:

We can, however, treat this as a normal text file. Suppose that we want to compute the average mark:

The ```csv``` module offers a slightly more convenient way of accessing the data:

For such a simple file it's hardly worth the trouble; however, the ```csv``` module can handle several types of files (essentially different separators) and automatically guess what software might have generated the file, see the [online help](https://docs.python.org/3/library/csv.html) for details.

The ```csv``` module also provides a ```writer``` object. However, remember that writing a ```csv``` file is essentially only a matter of putting the commas in the right places.

# The ```with``` context manager

Python provides a context management control structure, introduced by the ```with``` keyword. The context manager takes care of initialising and mopping up resources your program is using - in this case, a file. In practice, instead of writing:

you can simply write:

The file is closed automatically for you at the end of the ```with``` block, when the context manager exits. The same happens if the file is opened for writing.

This is a very Pythonic way of doing things, and it is very effective at fixing a common problem - i.e. files being left open when they are no longer needed. Context managers have applications also in other areas, that however are mostly beyond the scope of this module.

**(C) 2014,2020 Fabrizio Smeraldi** ([f.smeraldi@qmul.ac.uk](mailto:f.smeraldi@qmul.ac.uk) - [web](http://www.eecs.qmul.ac.uk/~fabri/)), all rights reserved. In: "Computer Programming", School of Electronic Engineering and Computer Science, Queen Mary University of London.

## Files - Solutions

### Simple notepad

Write a note-taking script that keeps asking the user for text and writes it to a file called ```notes.txt``` one line at a time, until the user writes the word ```exit``` alone on a line. This word should not be saved.

Then write, in a separate cell, a script that prints the contents of ```notes.txt``` to the screen.

Note that each time you run the note-taking script file ```notes.txt``` is cleared. To avoid this, modify the script so that it opens the file for appending instead of for writing - simply change the ```'w'``` into an ```'a'``` in the ```open()``` statement.

### Save your pennies

Write a program that reads a simple ```.csv``` file with the cost of shopping items. Your program should ask the user for the name of the file and print the total cost.

An example input file should look like the one below: 
```
milk,2.00
bananas,1.25
hamburger,4.95
chocolate,25.00
supplements,3.50
```
you can create one using the note-taking program you wrote above, directly using a text editor on your local machine or clicking on ```New > Text File``` on the Jupyter Notebook interface.

*Optional*: Add extra functionality to your program, such it is also prints a line that reads
```
Savings tips: you could cut down on the [...]
```
followed by the name of the *least* expensive item.

### Word count

The Unix ```wc``` command prints the number of lines, words and characters in a text file (type ```man wc``` in a terminal for more details). Write a program that asks the user for the name of a file, reads it and does the same. Process the file line by line; you can assume words are separated by a space.

### Mash them up

The Unix command ```cat``` allows you to concatenate the content of two files by appending the contents of the second file to those of the first file. In this exercise, we are going to create a program that combines the files, so to speak, "side by side", by concatenating corresponding lines.

Your program should ask the user for the names of the first (left-hand) input file, the second (right-hand) file and the output file. It should also ask for a separator string. It should then start reading one line at a time from each of the left- and right-hand files, and combine them to the output file as follows:
```
"line from left-hand file" + "separator string" + "line from right-hand file" + "\n"
```
So for instance if the left-hand file is a CSV file with 3 columns, the right-hand file is a CSV file with two columns and the string separator is ```", 0,"``` the result will be a CSV file with 6 columns: the 3 columns from the left-hand file, a column of zeros inserted by the separator, and the two columns from the right-hand file.

In order to keep the output consistent, your program should terminate when the shortest of the two input files runs out.

### Counting vowels... and more

Retrieve the code you wrote for the "Counting vowels" exercise (Notebook *Collections-Exercises*).

* Modify it so that, instead of processing a string, it reads a text file 
* Process the file line by line. 
* Go ahead, download an entire book from [Project Gutenberg](https://www.gutenberg.org/) and try crunching it.
* Can you use a loop to compute the frequency of all letters of the alphabet, instead of just the five vowels?


Hint No 1: There are two ways of doing this. The first is, loop over each line in the file tallying one character at a time. The second is, for each line in the file, loop over the alphabet and call the ```str.count``` method to see how many times each letter occurs in that line. The first one is maybe more natural.

Hint No 2: the command
```
from string import ascii_uppercase
```
will import variable ```ascii_uppercase``` with the entire uppercase alphabet from module ```string``` in the standard library. You can substitute ```ascii_lowercase``` for that if you prefer.

---

# First Steps

## First Steps - Main Content

# How to run Python

* You can run python in interactive mode from the command line (watch the video below for details): if you have Python installed, just type
<pre><code> python </code></pre>
* Python can answer many interesting questions in this modality (see the video)
* When you are done, type 
<pre><code> quit() </code></pre>
to exit
* However, in general, you will want to write a **program**
    * the difference between a calculator and a computer is that the latter can sequence operations
    * a program is just such a sequence

# Hello World! (Your first Python program)

* This is a programmer's [meme](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program), I'm sorry
* Your first program looks like this:
<pre><code> print ("Hello World!") </code></pre>
* Normally it would need to be typed in an editor (eg gedit, notepad, idle).
If you do not have Python on your machine or are unfamiliar with editors, follow the instructions in the video below
* You have to save it in a suitably named file (say hello.py)
* You run it by typing 
<pre><code> python hello.py </code></pre>
* You may find a file with extension .pyc has been created - that would contain the bytecode for your program (for very short programs, this is often cached).
* The program does what it says on the tin

### So why aren't we learning Java?

* In Java, it would look like this:
<pre><code>
public class Hello {

    public static void main(String[] args) {
        System.out.println("Hello, World");
    }
}
</code></pre>
* You would compile it this way:
<pre><code>
javac Hello.java
</code></pre>
* And run it this way:
<pre><code>
java Hello
</code></pre>
* There are reasons for that, but as far as you are concerned, that's overkill

# What are these lousy web pages anyway?

* This is actually a [Jupyter Notebook](https://jupyter.org/)
* It's pretty cool:

* You can mix notes and code
* It's available in the lab
* I recommend you install this on your computer: https://jupyter.org/install
(Linux not required), or install some Python distribution that includes it, such as Anaconda
* You can modify or experiments with these notes live during tutorials and labs
* You can insert your own examples and annotations
* Lab exercises will be Jupyter Notebooks
* Helps you document your work
* Great for working with colleagues afterwards
* Not practical for larger chunks of code...
* ...but you can mix and match as you like:

...there's more to life than PowerPoint!

# Arithmetic operations

As we have seen, we can use Python to perform standard arithmetic operations:

| **Operator** | **Description**   |
|--------------|-------------------|
|      +       | Addition          |
|      -       | Subtraction       |
|      *       | Multiplication    |
|      /       | Division          |
|      //      | Integer division  |
|      \*\*    | Exponentiation    |
|      %       | Modulo (remainder) |

* Note the difference between integer operations and floating point operations:
    * try 3/2
    * now try 3//2
* Precedence follows the standard arithmetic conventions:
    * try 1+3\*2
* Exponentiation has highest precedence, followed by multiplication and division, and then addition and subtraction
* Parentheses can be used as needed:
    * try (1+3)\*2
* A handy reference can be found [here](http://www.tutorialspoint.com/python/python_basic_operators.htm)

# Variables

We can assign values to symbols using the assignment operator '=':

*a* and *b* in the example above are **variables**.
Note that **=** is an **assignment**, so that the following makes perfect sense:

*a=a+1* is called an **increment** operation. It is so common that a special notation exists for it:

(just guess what *a-=1* does).

It makes a lot of sense to use meaningful variable names:

Note that the two strings
``` 
# in Kg 
```
and 
``` 
# in metres
```
above are there for your benefit, not for the interpreter. They are **comments**. Python ignores them. 
They can come after instructions or on a line of their own. Use liberally.

# Data types

* Integers such as 2 and decimal numbers such as 3.5, that are called *floats*, represent two different **data types**. That means that the bit patterns involved at the level of the memory are interpreted in different ways, and that in general they support different operations (rather more detail than necessary on the term *float* can be found [here](https://en.wikipedia.org/wiki/Floating-point_arithmetic), if you are interested).
* Another basic data type is a **character string**:
    * ```"Hello World!"``` was a string
    * ```'This is another Python string'```
    * When three delimiters are used, strings can span multiple lines:
        ```
        """This is a Python string
        on multiple lines"""
        ```
    * Strings spanning multiple lines can be used anywhere as a comment
* Strings can be assigned to variables:

Operators work in different ways on different types of data (obviously, not all operators apply to all data types):

There is more to this than meets the eye:

So how does the interpreter know what operator should be applied in each case?
* Python is implicilty typed, but strongly typed
* Implicitly typed means you do not have to write
```
int num=3;
String name="John";
```
as you would in Java
* however, each variable knows its type:

You can generally trust Python to do the right thing with your data. There are a few pitfalls, that will become apparent later on.

Strings are not, with a few exceptions, processed by Python - and the interpreter does not care if a string actually contains a number. If you declare it as a string, it means that you want it processed as a string! After all, you may have good reasons for that:

# Obtaining user input

A string of data from the user can be obtained via the ```input()``` function:

Note that ```input``` returns a string: 

### The Body Mass Index example revisited:

See the video below for help if you get stuck:

# Advanced operations on strings

Here are a few useful string manipulation operations. The syntax of some of these may look funny - these are actually **methods**. They are appended to the string variable name (or to the string itself) using a dot. Wait until we learn about Objects for this to make sense completely, but use them freely in the meanwhile

##### Length of a string

It's worth remembering the ```len``` function, it is very common and is also used to find the length of lists, tuples, dictionaries and sets (all things we will learn in the future)

##### To uppercase/lowercase

##### Replacing a substring

Use the method **replace**:

##### Other operations:

Here are a few more useful methods that I encourage you to experiment with:

For the low-down on strings, including more methods you can play with, check out the [documentation](https://docs.python.org/3/library/stdtypes.html#textseq).

**(C) 2014,2020 Fabrizio Smeraldi** ([f.smeraldi@qmul.ac.uk](mailto:f.smeraldi@qmul.ac.uk) - [web](http://www.eecs.qmul.ac.uk/~fabri/)), all rights reserved. In: "Computer Programming", School of Electronic Engineering and Computer Science, Queen Mary University of London.

## First Steps - Solutions

###  1- Hello World

Write a program that prints "Hello World". 

Your program should read:
```
print("Hello World")
```

### 2 - Proof of residence

Modify your program so that it prints your name and address as you would on an envelope

### 3 - Bugger off

Write a program that asks for your name and insults you.

### 4 - Star Trek

Write a program that asks you for a speed in km/h and converts it to furlongs/fortnight (ask Google for help with the conversion factor). Use it to convert the speed of light to furlongs/fortnight.

### 5 - The real deal

Write a program that asks for the length and width of your average studio shoebox in meters. Multiply the area by 19500 to obtain its price in Kensington, in pounds. Store in a variable and print the result including units. 

Multiply the average UK salary of £26500 by 0.75 to deduce taxes. Divide the price by the net salary to obtain the number of man-years it takes the average bloke to pay for the average shoebox.  

Print all results including units. Use meaningful variable names for all the parameters (salary, cost per square meters). Include comments.

### 6 - Happy birthday

Now for something a bit more cheerful: write a program that asks you for your age and prints "Happy Birthday" once for each year. Use the * operator on a string to do that.

### 7 - Operator madness

Look up Python operators [here](http://www.tutorialspoint.com/python/python_basic_operators.htm).

Try out all Arithmetic, Comparison, and Assignment operators in the box below. Feel free to define variables, create more boxes, write down notes and ask questions. Remember to save this notebook when you are done.

### 8 - Tea for You

Write a program that replaces 'U' with 'T' in RNA sequences, making sure that it works whether the string is uppercase or lowercase and always outputs an uppercase string. Hint: to obtain help on, for instance, the *str.replace()* method type *help(str.replace)* in the box below. Typing *dir(str)* will list all methods.

### 9 - With complements

This is stretching it a bit, but there is a way to use *str.replace()* to transform a DNA sequence into its complement. Can you do that? Write a program that asks you for a sequence and outputs the complement.

---

# Flow Control

## Flow Control - Solutions

### Good morning Vietnam

Write a program that asks the user "Is it morning?". If the answer is "yes", print "Good morning Vietnam". Otherwise, print "Good night Basildon".

### Making ends meet

Write a program that asks for the name of a month, and output the number of days in that month.

### Leap year proposal

Write a program that asks the user for the current year. Check to see if it is a leap year (leap years are divisible by 4 but not by 100). If so, print "Will you marry me?". Try it with your neighbour. Or not.

### No ifs or buts

Go over all the Comparison operators and Logical operators listed in
http://www.tutorialspoint.com/python/python_basic_operators.htm

Play with them and make sure you understand what they do

### Think positive

Write a list comprehension that creates a copy of a list of numbers, including only the positive ones.

For instance ```[-3, 2.5 ,-1, 2]``` should yield ```[2.5, 2]```

Modify it using conditional expressions so that the negative numbers in the input list get their sign changed.

Example: ```[-3, 2.5 ,-1, 2]``` -> ```[3, 2.5, 1, 2]```

### The Maths

Write a program that uses a ```for``` loop to print the multiplication  table for a number entered by the user. 

### Advanced Maths

Use two nested ```for``` loops to print the complete multiplication table for all numbers from 1 till 10. Try to print it out as a nicely formatted table.

### Very advanced Maths

You may want to attempt this later, if you have time. Try computing the first *n* lines of Pascal's triangle: http://en.wikipedia.org/wiki/Pascal%27s_triangle

Apart for the initial and final 1 of each line, each number is the sum of those above it to the left and to the right. So you can

* make a copy of the last line you printed (use ```[:]``` to copy all elements, simply creating references to the same list won't work)
* chop the leading "1" off one copy and the trailing "1" off the other
* sum them element by element
* add a leading "1" and a trailing "1" to form the next line
* print it and never mind the formatting

### A guessing game

Use the code below to generate a random number between 1 and 10 included and store it in the variable ```secret```. 

Use a ```while``` loop to keep asking the user for a guess until he finds the secret. Print the number of attempts.

### Caesar cypher

In cryptography, a Caesar cipher is a very simple encryption techniques in which each letter in the plain text is replaced by a letter some fixed number of positions down the alphabet. For example, with a shift of 3, A would be replaced by D, B would become E, and so on. The method is named after Julius Caesar, who used it to communicate with his generals. ROT-13 ("rotate by 13 places") is a widely used example of a Caesar cipher where the shift is 13. In Python, the key for ROT-13 may be represented by means of the following dictionary:

```
key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
```

Your task in this exercise is to implement an encoder/decoder of ROT-13. Once you're done, you will be able to read the following secret message:

   ```Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!```
   
Note that since English has 26 characters, your ROT-13 program will be able to both encode and decode texts written in English.

(By [Thorbjoern Lager](https://www.gu.se/english/about_the_university/staff/?languageId=100001&userId=xlagto)).

### 99 bottles of beer

"99 Bottles of Beer" is a traditional song in the United States and Canada. It is popular to sing on long trips, as it has a very repetitive format which is easy to memorize, and can take a long time to sing. The song's simple lyrics are as follows:

99 bottles of beer on the wall, 99 bottles of beer.
Take one down, pass it around, 98 bottles of beer on the wall.

The same verse is repeated, each time with one less bottle. The song is completed when the singer or singers reach zero.

Your task here is to write a Python program capable of generating all the verses of the song.

(By [Thorbjoern Lager](https://www.gu.se/english/about_the_university/staff/?languageId=100001&userId=xlagto). Optional: modify your program so that the numbers are printed out in words instead than in digits)

### Lost in translation

Here's a simple real-world application from the ever-growing field of Bioinformatics. Genetic information is stored in DNA, which is a sequence of 4 bases (the nucleotides, conventionally indicated by the uppercase letters A, C, T, G). Thus a part of a gene might look like the string ["GATTACA"](https://en.wikipedia.org/wiki/Gattaca). During [translation](https://en.wikipedia.org/wiki/Translation_(biology)), molecular machinery converts the genetic sequence to a string of aminoacids constituting a protein (proteins are the building blocks of our bodies). In particular, DNA is read as a sequence of three-letter long "words" (the *codons*), each of which identifies an aminoacid. Aminoacids are also written as uppercase alphabet letters. So a sequence like "ATACAACCTGGTTCA" would be segmented as "(ATA)(CAA)(CCT)(GGT)(TCA)" and translated to "IQPGS", according to the [standard genetic code](https://en.wikipedia.org/wiki/DNA_codon_table) (see also the dictionary below). In reality, these sequences are a few thousand characters long, hence the need for Bioinformaticians to crunch them. Happily, if we discard all the chemistry, this is just straightforward string processing. 

Write a program that asks the user for a nucleotide sequence and translates it into aminoacids. Use the genetic code table given below as a dictionary to look up the codons and perform the translation.

**(C) 2014,2020 Fabrizio Smeraldi** ([f.smeraldi@qmul.ac.uk](mailto:f.smeraldi@qmul.ac.uk) - [web](http://www.eecs.qmul.ac.uk/~fabri/)), all rights reserved. In: "Computer Programming", School of Electronic Engineering and Computer Science, Queen Mary University of London.

---

# Functions

## Functions - Main Content

# Functions

The scripts we have seen so fare were mainly very short. However, when programs become longer (above, say, 100 lines of code) it becomes important to split them into separate units. This improves readability, makes it easier to debug code and also allows reusing code within the same script or across different applications.

Functions are a standard mechanism provided by most programming languages to support modularisation of the code.

Functions normally take parameters passed as *arguments*, and may accomplish some action or return some value. We have already seen several examples:

We can define functions to perform tasks in our code. The way to do that is using the ```def``` statement:

```
def functionName (argument1, argument2, ...):
    """ Optional description (DocString) """
    ...BLOCK of code...
    return DATA # optional return statement
```
    

Example:

The above function does not return any value. We can modify it so that it returns the multiplication table instead of printing it:

Note that when the interpreter reaches the ```def``` statement it defines the function, but does not run it. Control starts from the first line of code outside a ```def``` statement. Note that we have to define a function before we can use it, so we could not put the definition below the rest of the code.

Also note that the docstring comment has a special function:

Algorithms are of course much, much older than computers. A good example is the [Euclidean Algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm) for finding the Greatest Common Divisor (GCD) of two numbers, that dates back to 300BC. It is based on the fact that if a number divides other two numbers, it also divides their difference (this is obvious: if, say, 3 divides both A and B, then A is this many times 3, B is that many times 3 - and the difference is also a certain number of times 3). So we can take the smaller number away from the larger without changing the GCD; this leaves us with smaller numbers. If we continue until the numbers eventually become equal, what we are left with is their GCD. Euclid would certainly have loved to see the code for this:

A function can take more than one parameter, and return any type of result:

In particular, we can use tuples or lists to have a function return more than one value. For instance, once we have the GCD of two numbers, we can obtain their [Least Common Multiple](https://en.wikipedia.org/wiki/Least_common_multiple) by taking the product of the two numbers and dividing it by the GCD:

### Function scope

Be aware that a function defines a *scope* for variables. In general, this means that variables that you use within a function are local to that function. You cannot access a variable that's local to a function from outside the function.

Any variable of the same name outside the function will be overshadowed by new variables defined within the function and will not be affected by operations done within the function. 

Modifying a global variable within a function is potentially messy, so Python generally prevents you from doing it. If you do want to access a global variable within a function *for writing*, you have to declare it explicitly using the ```global``` keyword:

### One last example:

As a last example, let us package the code below, that reads a protein from a FASTA file, into a function: (guided exercise)

**UPDATE:** Since version 3.6 dictionary keys are stored in insertion order, so you may in fact want to pay some attention to the order in which you list them

**(C) 2014,2020 Fabrizio Smeraldi** ([f.smeraldi@qmul.ac.uk](mailto:f.smeraldi@qmul.ac.uk) - [web](http://www.eecs.qmul.ac.uk/~fabri/)), all rights reserved. In: "Computer Programming", School of Electronic Engineering and Computer Science, Queen Mary University of London.

---

# Functions and Modules

## Functions and Modules - Solutions

### Maximum of two

Define a function ```max_of_two()``` that takes two numbers as arguments and returns the largest of them. Use the if-then-else construct available in Python. (It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)

(Credits:  [Thorbjoern Lager](https://www.gu.se/english/about_the_university/staff/?languageId=100001&userId=xlagto))

### Maximum of three

Define a function ```max_of_three()``` that takes three numbers as arguments and returns the largest of them. Use if-then-else.

(Credits:  [Thorbjoern Lager](https://www.gu.se/english/about_the_university/staff/?languageId=100001&userId=xlagto))

### Maximum of many

Define a function ```listMax()``` that takes a list as argument and returns a tuple with the maximum and its index in the list.

(Credits:  [Thorbjoern Lager](https://www.gu.se/english/about_the_university/staff/?languageId=100001&userId=xlagto), adapted)

### Roll your own

Take the three functions you coded above and put them in a file called ```mymax.py``` to make a module. Then try writing a simple program that starts with 
```
import mymax
```
and calls the functions you wrote as ```mymax.max_of_three()```, etc

### Histogram

Define a procedure ```histogram()``` that takes a list of integers and prints a histogram to the screen. For example, ```histogram([4, 9, 7])``` should print the following:
```
****
*********
*******
```
Note: a procedure is a function that does not return any value, it simply *does* something.

(Credits:  [Thorbjoern Lager](https://www.gu.se/english/about_the_university/staff/?languageId=100001&userId=xlagto))

### Got it all backwards

Define a function ```reverse()``` that takes a string as an argument and returns it reversed. For instance,   ```reverse("I am testing")``` should return the string "gnitset ma I".


(Credits:  [Thorbjoern Lager](https://www.gu.se/english/about_the_university/staff/?languageId=100001&userId=xlagto))

### Palindromes

A palindrome is a word or sentence that is unaltered when read backwards.

Write a palindrome recognizer ```isPalindrome()``` that accepts phrase palindromes such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored. 

Your function should return ```True``` for palindromes and ```False``` otherwise. Your function should use the ```reverse()``` function you just programmed to do its job.

(Credits:  [Thorbjoern Lager](https://www.gu.se/english/about_the_university/staff/?languageId=100001&userId=xlagto))

### Default arguments and calling styles

Try calling the procedure below in the following ways, that are all legal, and see what happens:
```
aProc("eggs", "bacon") # specify both arguments (the usual way)
aProc() # use default values
aProc("goo") # only specifies first argument
aProc(second="more spam") # only specifies second argument
pet=["Humpty", "Dumpty"]
aProc(*pet) # both arguments as a list 
meg_and_mog={'first': 'Meg', 'second': 'Mog'} 
aProc(**meg_and_mog) # both arguments as a dictionary
```

### Lingo



In a game of Lingo, there is a hidden word, five characters long. The object of the game is to find this word by guessing, and in return receive two kinds of clues: 1) the characters that are fully correct, with respect to identity as well as to position, and 2) the characters that are indeed present in the word, but which are placed in the wrong position. Write a program with which one can play Lingo. Use square brackets to mark characters correct in the sense of 1), and ordinary parentheses to mark characters correct in the sense of 2). For the sake of the exercise, your program should pass each character in the user input to a function that "packages" it in brackets (or not). In turn, this should use two separate functions to check if either 1) or 2) apply.

Assuming, for example, that the program conceals the word "tiger", you should be able to interact with it in the following way:

```
snake
Clue: snak(e)
least
Clue: l(e)as(t)
times
Clue: [t][i]m[e]s
tiger
Clue: [t][i][g][e][r]
```

(Credits:  [Thorbjoern Lager](https://www.gu.se/english/about_the_university/staff/?languageId=100001&userId=xlagto))

### Born on the Fourth of July

You now have all the tools and the knowledge to do fairly complex stuff. Let's try some data analysis -
read [this story](https://fivethirtyeight.com/features/some-people-are-too-superstitious-to-have-a-baby-on-friday-the-13th/) online, and download the underlying data - it's available in a [github repository](https://github.com/fivethirtyeight/data/tree/master/births). Read the ```README.md``` file carefully and make a note of file format, then click on ```US_births_2000-2014_SSA.csv```, click on *Raw* and use the *File>Save Page As* (or equivalent) function of your browser to save the file in  your working directory (if this does not work for you, you can download the entire repository from GitHub as you would one of our lectures, and then copy the file over).

* Write a function that reads all the data into a list of *(year, month, date_of_month, day_of_week, births)* tuples. Remember to convert all data to type ```int```
* Warm-up exercise: for the sake of the title, compute the average number of people born yearly on July 4th (hint: that should be around 8815.27). If you are curious, do the same for people born on Friday 13th, and people born on a Friday that's not the 13th.

Data aggregation is a basic stepstone of data analysis. We can aggregate birth data with respect to each of the first  four columns to find how many people were born in each year, on each day of the week or on each date of the month.

* Write a function called ```aggregate``` that takes as its arguments the data and the number of a "key" column for aggregation. The function should return a dictionary. The keys of the dictionary should be all values of the "key" column; the corresponding values should be the total of all births listed against each value of the "key" column. So for instance if the "key" column is number 3 (*day_of_week*), the dictionary should have keys 1 to 7 and the value for, say, key 1 should be the sum of all births for which *day_of_week* is listed as being 1.

Hint: this is somewhat similar to the "Counting Vowels" exercise (in both "Collections" and "Files" lectures), except the key values now are taken from the data table itself, and increments are given by the number of births. If you get stuck, try hard-coding it for the *day_of_week* column only, move on to the following part, test the two functions together, and then come back to this.

* Write a function called ```print_stats``` that takes as its argument an aggregated data dictionary as returned by ```aggregate``` and prints it out as a nice table of key-value pairs, sorted by key.

* Use the above two functions to compute and tabulate the total number of births in each year, on each day of the week, in each month and on each date of the month. Can you spot any interesting trends?

**NOTE:** This is a slightly more complex exercise - you may not have the time to go beyond the warm-up part in class, but we recommend you attempt the rest in your own time. Be prepared for the second part to require some thinking. This exercise is also, like all exploratory data analysis tasks, very open-ended - if you want to do more, you can modify the ```histogram``` function to take a dictionary as its input, and use it to plot the percentage of people born on each day of the week, month or date of the month. You can also try analysing the data in the other birth data file, ```US_births_1994-2003_CDC_NCHS.csv```, that is formatted in the same way, and see if any trends you identified are confirmed in the longer term.

---

# Introduction

## Introduction - Main Content

*It is said that despite its many glaring (and occasionally fatal) inaccuracies, the Hitchhiker's Guide to the Galaxy itself has outsold the Encyclopedia Galactica because it is slightly cheaper, and because it has the words **'DON'T PANIC'** in large, friendly letters on the cover (D. Adams, the Hitchhiker's Guide to the Galaxy)*

# 1- Why Python?


Here is a quote from a [blog](https://dzone.com/articles/why-python-important-you) that expresses how your lecturer (and many others) feel about Python:

"I believe that Python is important for software development. While there are more powerful languages (e.g. Lisp), faster languages (e.g. C), more used languages (e.g. Java), and weirder languages (e.g. Haskell), Python gets a lot of different things right, and right in a combination that no other language I know of has done so far."

Python has evolved from a "scripting language" (more on this below) to a language in which you can write entire applications. Among other advantages, we have that:
* Python makes writing good code easy.
* Python keeps development time low - it's basically executable pseudocode.
* Python has bindings for most libraries (including scientific computing ones).
* Python code is easy to read, debug and maintain.
* Python is *fun* (I cannot explain this one, but I'm not the only person who thinks that).
* You can basically do anything in Python.

# 2 - So should I learn Python as my 1st programming language?

There are plenty of discussions online on this topic. Many top universities, including MIT, have switched their introductory modules from Java to Python, so that's a good indication. Having years of experience teaching both languages, your teacher thinks Python is the better choice. Here are some of the reasons for that:

* Python syntax is clean and easy to read
* It allows you to start simple - what you don't know (mostly) won't harm
* In spite of that, it supports very advanced programmed techniques and styles
* It offers plenty of interactive tools (including these notebooks) that make learning easy
* There are plenty of online resources to support you
* It is a real-world, general purpose programming language.

It is worth emphasizing the last point: there are plenty of Python programming jobs out there that range from web development to full-stack engineering (a [chimeric professional figure](https://stackoverflow.blog/2019/10/17/imho-the-mythical-fullstack-engineer/)  much loved by recruiters) to much more trendy and esoteric stuff. Namely, Python has become a de-facto standard for, among others, 
* Data science and visualisation, thanks to libraries such as [pandas](https://pandas.pydata.org/) and [seaborn](https://seaborn.pydata.org/)
* Machine Learning, thanks to [keras](https://keras.io/), [tensorflow](https://www.tensorflow.org/), [pytorch](https://pytorch.org/) and [scikit-learn](https://scikit-learn.org/stable/)
* Web scraping, thanks to the [scrapy](https://scrapy.org/) framework

You will find plenty of videos online discussing the choice of your first programming language. Mercifully, that choice has been made for you by your lecturer. If you are still concerned, the video below is far too centred on web development, but it does make some good points 


# 3 - What is Python anyway?

Python is a *high-level*, *interpreted*, *object-oriented* language with some *functional programming* constructs. It is also sometimes described, like PERL or TCL, as a "scripting language", which generally means "interpreted and suitable for solving small tasks", though indeed Python can be used for large projects too.

### High-level (*versus* low-level)

Low-level languages such as ASSEMBLY, C and C++ are closer to machine code (i.e. the binary code that computers can actually run). They allow full control of the memory and the hardware, they are extremely fast, but tedious to write and difficult to debug.

High-level languages such as Java, C#, Python and PERL are further removed from the machine code and closer to English. They are easy to write and more concise, but generally slower. Some languages such as Matlab, R, and Julia are specialised for particular task (e.g. scientific computation) and have a specific syntax (e.g. algebraic-style) to support those tasks.

Python is high-level; it has a general purpose (particularly clean) syntax that makes code easy to read and maintain. Python programs are remarkably concise as compared to, for instance, Java (PERL programs are concise but can be [unreadable](https://en.wikipedia.org/wiki/Just_another_Perl_hacker)).

### Interpreted (*versus* compiled)

Program code is understandable by the programmer, but not by the machine. Therefore, there needs to be something (which is actually another program!) that translates the code to machine language before it can be executed. This translator software can be either:
* an interpreter, or
* a compiler.

An **interpreter** translates code line-by-line as it is executed. This process is slower than compilation, as the same line may have to be translated many times; on the other hand it generates great flexibility, as a program can for instance modify itself on the fly or evaluate user input as an instruction.

The development cycle is also faster with an interpreter, as code can be tested as soon as it is written. Indeed, it is possible to embed interpreted code in other environments:

High-level languages such as Matlab, PERL and indeed Python are generally interpreted.

A **compiler** translates all your program at once, before execution. The advantage is that the translation is performed "once and for all"; also, the compiler can perform more checks and optimisations. Once the program is compiled, it runs at machine-code speed. The disadvantage of compilation is that the development cycle becomes slower: each time you modify the code, you need to compile it. Also, when an error occurs while the program (i.e. its machine code) is running, you need to trace this back to the source code, which generally requires the use of a debugger. Low-level languages such as C/C++, Fortran and also Java are compiled.


### Bytecode

Well actually... a third way has emerged in recent years, and Python and Java actually sit in this "grey area" (though PERL does not). Program code can be translated (i.e. compiled) to an intermediate low-level pseudo-code called *bytecode*. This is the choice made in Java and Python (as well as languages of the Microsoft .NET framework, e.g. C#). The interpreter then only needs to convert bytecode to machine code on the fly, but this is a much simpler task. Thus the first advantage of this approach is *increased speed* relative to interpreted languages (though of course bytecode is still slow compared to native code).

A second advantage is *portability*: because bytecode is an abstraction of machine code, it can be made independent of the machine. This has allowed the development of huge standard libraries for languages that use it, a feature that you will find most beneficial.

Java bytecode is lower-level (and thus faster) and requires separate programs for generating and running it (the "compiler" and a "virtual machine" known as JVM), so we commonly think of Java as a "compiled" language. Python bytecode (that hides in *.pyc* files) is higher level and is generated and run by the Python interpreter, so we tend to think of Python as an "interpreted" language.

Finally, it is possible to:
* generate Java bytecode from a Python program by using Jython (http://www.jython.org/)
* generate CIL code (i.e. the .NET bytecode) using IronPython (http://ironpython.net/), and
* compile a subset of Python instructions to C code (and hence native machine code) using Cython (http://cython.org/).

None of these is possible in, for instance, PERL.



### Object-Oriented (with benefits)

Object-oriented programming is a technique for facilitating code reuse. It is very popular in industry, though there are arguments against it, as well as in favour. It is essentially an effective way of encapsulating data and code in independent units (known as *objects*) that can be handled without any knowledge of their internal working and modified according to your needs. **Objects** are a more advanced concept than *modules* or *functions* (both of which we will cover), and offer exciting capabilities such as inheritance (in fact, object-oriented libraries are organised in taxonomies of sorts). This obviously imposes some overhead, especially evident in languages like Java (where object-oriented programming is mandatory). 

The good news is: Python is object-oriented, but you can safely ignore objects if they are not useful for your task (e.g. short scripts). When you do want to use them, the overhead is minimal and the mechanism is rather elegant. By contrast, objects come as an afterthought to PERL and are not very convenient to use.

Besides, Python incorporates some interesting constructs from *functional programming* (an entirely different programming paradigm exemplified by Haskell and Lisp). Notable among these are *list comprehensions*, that we will cover in this module.

**(C) 2014,2021 Fabrizio Smeraldi** ([f.smeraldi@qmul.ac.uk](mailto:f.smeraldi@qmul.ac.uk) - [web](http://www.eecs.qmul.ac.uk/~fabri/)), all rights reserved. In: "Computer Programming", School of Electronic Engineering and Computer Science, Queen Mary University of London.

---

# Iterative constructs

## Iterative constructs - Main Content

One of the few things computers are really good at is repeating the same actions over and over again (possibly on different data). This is achieved with iterative constructs (**loops**). This notebook introduces loops; combining these instructions with conditional statements and the advanced data structures we covered in the first few lessons, you will be able to write  useful code.

# For loop

This is a control structure that allows you to repeat a block, while an index variable takes on a predefined set of values. Formally we write this as:
```
for VAR in ITERABLE:
    BLOCK
```

An ITERABLE is essentially an ordered collection of items (think a list, a tuple or a file). Example:

Again, note the indentation of the block which is mandatory.

In other languages ```for``` loops use an index variable that iterates over a range of values. This can be done in Python by iterating over a list of numbers:

We can use the convenient function ``range``: this is an immutable sequence of numbers that's computed lazily as needed. This means that elements of the sequence are computed one at a time as they are used; the advantage is that all ranges take up the same space in memory regardless of their length - only the starting point, end point and optional step are stored (see the [documentation](https://docs.python.org/3/library/stdtypes.html#range) for more info). We won't worry about the details here:

so, no need to write down the list ```a``` explicitly:

or even more simply:

As we have seen, we can iterate over the content of a list directly. However, sometimes we may want to iterate over a list explicitly using the index, maybe because we have more than one list at the same time. This is a very typical use of the loop variable:

However, Python also gives us an option to create a "composite" list and iterate over that one:

In another example, you can step through a string:

Another classic example is the multiplication table:

### Nested loops

Note that loops can be **nested** by placing one loop inside the other. Then the inner loop runs its entire course over and over again as specified by the outer loop:

I strongly recommend that you paste the code above into the [Pythontutor](http://pythontutor.com/visualize.html#mode=edit) online intepreter and run through it step by step in order to understand how the values of ```i``` and ```j``` change throughout the execution.

# While loop

This other type of loop does not iterate over an object such as a list, but keeps looping until a certain condition becomes false. The syntax is:
```
while EXPRESSION:
    BLOCK
```
where *EXPRESSION* is a Boolean expression of the type we saw previously in conjunction with *if/else*.

Since there is no predefined object to iterate on, this type of loop comes in handy when we do not know in advance how many objects we need to process - say when reading a file, or asking the user for input.


Another example (note the "accumulator" technique):

In other situations, we might genuinely not know where we should stop:

# The "break" statement

Sometimes, it is convenient to break out of a ```for``` loop when a condition is met. For example, during a search, we may be happy with the first match and economise on computer resources by not looking any further. The ```break``` statement allows us to exit a loop there and then (and as such, is normally found inside an ```if``` clause):

We may also want to break out of a ```while``` loop, which sometimes leads to elegant solutions:

# The "continue" statement

The ```continue``` statement takes us to the next iteration of a loop. It is typically used to skip input that is invalid or irrelevant, for instance commented lines in a file, or erroneous values. Here are two simple examples.

The number 4 is considered [unlucky](https://en.wikipedia.org/wiki/Tetraphobia) in many East Asian countries because it sounds similar to the word "death". Therefore, you may want to skip it while printing:

In another application involving a ```while``` loop, we may want to handle invalid input to our accumulator. The conversion to ```float``` fails and crashes the program if the user input is not a number (apart for the word "sum" that's handled separately - try it on the previous version of this program). Using a ```continue``` statement allows us to prevent the crash and go around to ask for more input.

**(C) 2014,2020 Fabrizio Smeraldi** ([f.smeraldi@qmul.ac.uk](mailto:f.smeraldi@qmul.ac.uk) - [web](http://www.eecs.qmul.ac.uk/~fabri/)), all rights reserved. In: "Computer Programming", School of Electronic Engineering and Computer Science, Queen Mary University of London.

---

# MockAnswers22

## MockAnswers22 - Main Content

**NOTE**: The exam questions will come in a pdf file. This will be released together with the a Jupyter Notebook answerbook, in which you will have to fill in your answers. Submissions not using the answerbook will not be marked. The answerbook will contain test code to help you check your answers, as per examples below. The text of the questions will not appear in the answerbook, though for convenience some code may be already copied into the answerbook for you.

The questions below are not meant to be representative of the level of difficulty or of the exact tests, and are only simple examples given to clarify what form of answer is expected and what are the rough limitations of the tests provided.

### Mock question 1

*The text of the question will be in the pdf file*

--------------------------------

Consider the following list:

```message=['blah', '/start/', 'this', 'is', 'boring', '/stop/', 'whatever']```

Write a comprehension to list all the strings appearing  between the words ```'/start/'``` and ```'/stop/'```, with the two extremes excluded. Your code should be independent of the precised contents of ```message```, provided it contains ```'/start/'``` and ```'/stop/'``` (that are guaranteed to appear only once, in the right order).


### Mock question 2

Code a function called ```compute``` that takes three parameters. In order, these are a number ```a```, a string ```op```, and a number ```b```. Assume argument ```op``` is one of ```"+"```, ```"-"```, ```"*"```, ```"/"```; the function should return the result of the corresponding operation performed on ```a``` and ```b```. So for instance ```compute(1, '+', 2)``` should return ```3```.


### Mock question 3

Code a class called ```EggTimer``` that models a simple egg timer. The constructor of the class should take as a parameter the length of time you want to boil the egg for (given in seconds); this should be stored in attribute ```_duration```. Code a method ```time``` that prints the message ```'Start boiling the egg'```, waits for the correct number of seconds, and then prints the message ```'Your egg is cooked'```. Hint: use the function ```sleep``` provided by the ```time``` module of the standard library to wait for the required number of seconds. 

---

# MockQuestions22

## MockQuestions22 - Main Content

**NOTE**: The exam questions will come in a pdf file. This will be released together with the a Jupyter Notebook answerbook, in which you will have to fill in your answers. Submissions not using the answerbook will not be marked. The answerbook will contain test code to help you check your answers, as per examples below. The text of the questions will not appear in the answerbook, though for convenience some code may be already copied into the answerbook for you.

The questions below are not meant to be representative of the level of difficulty or of the exact tests, and are only simple examples given to clarify what form of answer is expected and what are the rough limitations of the tests provided.

### Mock question 1

*The text of the question will be in the pdf file*

--------------------------------

Consider the following list:

```message=['blah', '/start/', 'this', 'is', 'boring', '/stop/', 'whatever']```

Write a comprehension to list all the strings appearing  between the words ```'/start/'``` and ```'/stop/'```, with the two extremes excluded. Your code should be independent of the precised contents of ```message```, provided it contains ```'/start/'``` and ```'/stop/'``` (that are guaranteed to appear only once, in the right order).


### Mock question 2

Code a function called ```compute``` that takes three parameters. In order, these are a number ```a```, a string ```op```, and a number ```b```. Assume argument ```op``` is one of ```"+"```, ```"-"```, ```"*"```, ```"/"```; the function should return the result of the corresponding operation performed on ```a``` and ```b```. So for instance ```compute(1, '+', 2)``` should return ```3```.


### Mock question 3

Code a class called ```EggTimer``` that models a simple egg timer. The constructor of the class should take as a parameter the length of time you want to boil the egg for (given in seconds); this should be stored in attribute ```_duration```. Code a method ```time``` that prints the message ```'Start boiling the egg'```, waits for the correct number of seconds, and then prints the message ```'Your egg is cooked'```. Hint: use the function ```sleep``` provided by the ```time``` module of the standard library to wait for the required number of seconds. 

---

# Modules

## Modules - Main Content

Functions are a convenient way of packaging parts of the code that carry out a particular operation. Sometimes, we want to package a series of functions and constants that help accomplish related tasks (for instance, read and write common bioinformatics file formats) into a separate file for convenience of reuse. In python, such a file is called a *module* and we can think of it as a library of functions. 

**NOTE:** This notebook assumes that you are familiar with the contents of the *Functions* notebook

# Importing modules

Modules need to be imported before they can be used. This is done with the ```import``` keyword. For instance, the [os](https://docs.python.org/3/library/os.html) (for Operating System) module is part of the Python Standard Library, so it is included in every Python distribution. It provides an interface to low-level functions provided by the operating system. In order to use it, we have to ```import``` it:

Note that all references to constants, functions and variables defined by the module include the name of the module. We say that the module defines a *namespace*. This is to avoid variables and functions within the module to conflict with those you may have defined in your program, using the same name.



We can just import a few functions or constants into the main namespace and use them directly without the module name:

Or we can import everything into the main namespace, but that is risky as it can override other definitions:

In general, it is better to import a module into a separate namespace, using maybe an alias if the name is too long. This example uses the [time](https://docs.python.org/3/library/time.html) module, also from the Standard Library, that gives access to system time and time conversion functions.

# Installing modules

The [Python Standard Library](https://docs.python.org/3/library/) provides a rich selection of modules that you can use to perform all sorts of operations, from formatting text to accessing web sites programmatically and even processing multimedia files. These should be included with every Python installation; specific distributions may include more modules as a default.

Most other Python libraries are in fact organised into packages and available online from the [PyPI](https://pypi.python.org/pypi) website. A description of what a package is can be found in the online
[documentation](https://docs.python.org/3/tutorial/modules.html#packages), but for the time being don't worry about it - they are sets of modules organised hierarchically in a directory tree, and by and large they
work just like modules.

Your machine should have *pip* installed, or you can install it as explained [here](https://pypi.org/project/pip/) (for Linux distributions, this may be as easy as installing a .rpm or .deb file).

Once that is done, installing any Python packages you require from the repository is straightforward: just type
```
pip install PACKAGE_NAME
```
that's all that there is to it; *pip* will find the most recent version, download it and install it for you. It will also fetch and install any modules required by the one you want installed.

**NOTE**: if you are working on the EECS JHUB, packages you install as indicated above won't be persistent - they will be removed when your instance is restarted.  If you have installed the [Anaconda](https://www.anaconda.com/products/individual) Python distribution on your machine, you will have *conda* instead of *pip*. That's just as good, refer to the [conda documentation](https://docs.conda.io/projects/conda/en/latest/) instead.

# Writing modules

Writing modules isn't more difficult than writing any other Python program. You can, in fact, put some code into a separate file and import it. For instance, we may want to package the function that reads a FASTA file into a function and put it into a module for easy reuse. We'll call this module *fastaio.py*. This will be done as a guided example, see the video.

Once we have added the ```readFasta``` function to the module file, we should be able to run the following code:

# Testing modules

A module is, after all, only a piece of Python code. So there is nothing preventing you from running the *fastaio.py* module stand-alone by typing
```
python fastaio.py
```
on the command line. If this module only defines some functions and does not actually contain any instruction to call them, nothing will happen. However, instructions can be added, outside functions, within a module; these are typically used to define constants and perform the necessary initialisations within your module; they are run only once when the module is imported. 

Within a module, the name of the module is made available through the global variable ```__name__```. When the module is run stand-alone rather than imported, this variable is set to ```"__main__"```. This can be used to code some tests that shall only run when the module is invoked directly from the command line. Typically, one would write
```
if __name__== "__main__": # we have been launched stand-alone
    # Do some tests here
```
This feature is demonstrated in the video below.

**(C) 2014,2020 Fabrizio Smeraldi** ([f.smeraldi@qmul.ac.uk](mailto:f.smeraldi@qmul.ac.uk) - [web](http://www.eecs.qmul.ac.uk/~fabri/)), all rights reserved. In: "Computer Programming", School of Electronic Enigneering and Computer Science, Queen Mary University of London.

---

# OOP

## OOP - Solutions

### Counting sheep (or anything else)

Write a class called ```Counter``` that represents a simple counter. It should have a ```self.count``` attribute that starts from 0. Also it should have a ```self.max``` attribute that represents a limit for the count. Code the following methods:
* ```.__init__(self, m)``` constructor. Set ```self.max``` to ```m``` and ```self.count``` to 0
* ```.increment(self)``` increase the count if it is smaller than the max, otherwise complain
* ```.decrement(self)``` decrease the count if it is larger than zero, otherwise complain
* ```.reset(self)``` reset counter to 0
* ```.__str__(self)``` return a string such as "5 out of 10 and counting", assuming 5 is the count and 10 the max (this message will be displayed when the object is printed)

Write a test program for your counter class. Allocate two objects of type ```Counter```: one called ```sheep``` with a maximum of 4 and one called ```chicks``` with a maximum of 6. Program a while loop to keep asking the user for input. Process input as following:
* "baaa" increment sheep counter
* "egg" increment chicken counter
* "wolf" decrement sheep counter
* "fox" decrement chicken counter
* "market" reset both counters
* "quit" exit

Print the two counter objects after each iteration (this will actually call the ```__str__``` method you coded and print the string it returns).

### Subsidised computing

Derive a ```CounterPlus``` class from ```Counter```. Within it, define a ```.add(self, n)``` method that adds ```n``` to the count (capping the count to the maximum if needed).

Modify the previous program so that it uses a ```Counter``` for sheep and ```CounterPlus``` for chickens. When the user enters "subsidy", add 5 to the number of chickens.

### Pizza and no beer

A pizzaiolo traditionally manages his orders using a metal pin or skewer. New orders are written on a piece of paper by the waiters and skewered on top of the heap. The pizzaiolo always tears off the lowest paper and bakes that. This is a practical implementation of a first-in-first-out (FIFO) queue.

Write a class called ```Skewer``` that has two methods: ```.order(self, pizza)``` that adds an order to the top of the skewer and ```.bake(self)``` that returns and removes the oldest order from the bottom of the skewer  (these are often unimaginatively called *push()* and *pop()* in CS jargon; *push* adds to the tail of the queue, and *pop* removes from its head). Design the internal workings of the class so that it functions as it should, in a first-come-first-served fashion (hint: you will need a list attribute to store the orders, this should be created by the constructor).

Test by allocating an object of type Skewer and using it to order a "margherita", a "capricciosa" and a "quattro stagioni". Remember to ```.bake()``` them. Enjoy!

### Animal farm

Create a hierarchy of classes for storing data about animals. This should be structured as follows:
* Class ```Animal``` is the base class for the entire hierarchy. Its constructor takes the name of an animal and its age and assigns them to attributes. It defines a method ```basic_info``` that returns a tuple with the name and age of the animal.
* Class ```FarmAnimal``` extends ```Animal```. It adds a method ```to_stable``` that prints the message "Taking NAME to the stables", as appropriate.
* Class ```Pet``` extends ```Animal```. It adds an attribute ```is_sociable``` that is either ```True``` or ```False```; this attribute must be set by the constructor. It also adds a ```pet``` method that prints the message "I'm petting NAME" or "NAME does not like to be petted" according to the value of ```is_sociable```. 
* Classes ```Cow``` and ```Goat``` extend ```FarmAnimal```; classes ```Cat```, ```Dog``` and ```Python``` extend ```Pet```. Each of them defines a method ```make_sound``` that takes an integer as its argument and prints the sound that animal makes the corresponding number of times. 

Once your classes are defined, create one instance for each of ```Cow```, ```Goat```, ```Cat```, ```Dog``` and ```Python```. Then try the following:
* Create a list of all your farm animals. Write a loop that takes them all to the stables.
* Create a list of all your pets. Write a loop that pets them.
* Merge the two lists. Write a loop that, for each animal, calls ```basic_info``` to get the name and age of the animal, prints the message "NAME just turned AGE and says:" and then calls ```make_sound``` with the value of the age. So for instance if the cat is 4, it should go "meow" four times.
* Optional: Add an attribute ```sound``` to ```Animal```, and have it set by the constructor. Move the ```make_sound``` code to the class ```Animal```, and modify it so that it uses the ```sound``` attribute to print the correct sound. Remove ```make_sound``` from the derived classes. You will need to change the constructor of the derived classes and the lines that create your animals accordingly, but in the end your code will be much shorter.

Tips: Constructors in Python are inherited, unless you override them in the child class. If you do, remember to call the constructor of the parent class - use the ```super``` keyword. All methods take ```self``` as their first argument!

---

# Object Oriented Programming

## Object Oriented Programming - Main Content

# Why objects

The programming paradigm we have been working with so far is called *procedural programming*. Essentially, this views a program as composed of two entities:
* Data structures (variables, lists, etc) that hold the data
* Functions that operate on the data

This is adequate for many purposes, and indeed you will find yourself writing procedural code in Python time and again. However, sometimes we would like the data to be more closely tied to the functions that handle them. For instance, we might want image data to know how to save itself to the disk in a JPG format, while music data should write itself in the MP3 format. We can, it's true, write something like
```
picture= # image data
song= # music data
writeJPG(picture, "mypicture") 
writeMP3(song, "mysong")
```
but we'd rather write
```
picture.write("mypicture")
song.write("mysong")
```
so we don't have to remember two function names. In fact, we are almost sure that one day we will write:
```
multimedia_data= # some image
writeMP3(multimedia_data, "somefile") # Oops! .mp3 image?
```
so that we'd rather do:
```
multimedia_data= # some image
multimedia_data.write("somefile")
```
and trust it will do the right thing.

Indeed, the best would be this:
```
media_collection=[a_picture, a_song, a_movie]
for mm in media_collection:
    mm.write("somefile") # you know what's the right format for you, don't you?
```
Objects allow us to do just that.

# Classes and Instances

A **class** is, so to speak, the template of an object: it specifies the operations that can be done on it. The syntax for defining a class in Python is straightforward:
```
class NAME:
    BODY
```
where *BODY* contains the definition of functions, called *methods*, that operate on the data of the class. 

Here is a simple class that models a square:

The class definition itself does not do anything. We need to create an **instance** of the object, that is a specific square. The ```self``` parameter tells Python to which particular instance of ```Square``` that ```side``` belongs: this is where the link between the generic template of the class and the individual instance is made.  

This is convenient, but still somewhat unrefined. For instance, we can do the following:

To avoid this kind of errors, we need a special type of function to initialize all the attributes of our object. This is called a Constructor.

### Constructors

A **constructor** is special methods that is called when an instance is created and initialises all the variables needed by the instance. A constructor in Python is just a special method called ```__init__``` that can take any parameters besides ```self``` but does not return any value: 
```
def __init__(self, PARAMS):
   BODY
```
Once again, you do not call this method directly, but Python calls it for you when the instance is created.

We can rewrite our *Square* class as follows:

There are several things we can learn from this snippet of code. First of all, the problem of having a ```Square``` with an undefined ```side``` is solved: we have to provide that when we create the ```Square```, the interpreter won't let us do otherwise (unless we provide a default value).

Second, note the difference between ```self.side``` and ```s```. The parameter ```s``` is local to the constructor (like all function parameters), and it ceases to exist when the constructor returns. Attribute ```self.side```, instead, is attached to the instance and lives on with the particular instance of ```Square```.

### An example

Here is an example:

So we can do the following:

Notice that students have their individual names and print accounts. Something like this makes no sense:

An exception to this is the "class variable" *university* declared together with the class. This is shared among all students, so that I can do this:

The second line hides the fact that this variable is shared among all objects, so that assigning to it affects all instances:

Once again, notice that ```Student``` instances have their own individual ```name``` attribute, so compare with this:

Most of the times what you need is an attribute. Class variables are rather rare and have specific uses, so as a first approximation it's safe to ignore them. You will generally find class variables used, for instance, as a class-specific type of constant in libraries.

# Inheritance

A key features of Objects Oriented languages is **inheritance**. Inheritance is the key feature of these languages that facilitates code reuse; as such most libraries you will sooner or later use rely heavily on it. In essence you can think of objects as forming a taxonomy, the root of which is (you guessed it) the type ```object```. This type is rather boring, in fact it is essentially a placeholder  

Going down the branches of the "taxonomy", every object specialises its parent in the sense that it adds more features, or modifies existing behaviour. Any class you define is automatically a "child" (a *subclass*) of ```object```, so that an instance of any class will be an instance of ```object```, in the same way that Barker (an instance of *Canis familiaris*) is also an instance of a Mammal and of an Animal:

However, what makes this interesting is the possibility of inheriting from more meaningful classes than ```object```. For instance, let us consider different types of students in a university:

Of course you would expect these to work:

But the neat thing is that we can also do this:

These methods are inherited from the parent class ```Student```. So a ```BScStudent``` is all that a ```Student``` is, plus something - and the same applies to ```PhDStudent```. In fact, both ```fresher``` and ```nerd``` are instances of ```Student```:

Note that the converse is not true (the parent is not an instance of the child):

# Polymorphism

In the previous section we have seen how an object
* inherits methods, attributes and class variables from the parent class
* can add its own methods, attributes and class variables as required to perform more operations

However, a child class can also perform one of the functions the parent can do in a different way. This is achieved by redefining (*overriding*) methods of the parent class in the child class. This results in object hierarchies with the
following properties:
* each is derived from a common class
* each can perform a certain operation
* each one does it its own way, without the programmer having to worry about it.

This is called **polymorphism**.

As an example, we will define a 
```
__str__()
```method for ```Student``` and each of its derived classes. This method is used to return a human-readable representation of an object as a string; this is the string that is printed when one calls ```print``` on the object. The default version of this method inherited from ```object``` is not very informative:

the above is actually equivalent to:

so ```print``` does call ```__str__()``` for you.

In the following example we will override ```__str__()``` for Student and its children with a more meaningful version. Since this involves a bit of code, the class definitions are written in the module *students.py*:

In the cell below, we import the student module, create an instance of each class and print it, which will show the output of the ```___str___()``` module we defined for each of them.

In fact, there's no need to refer to the original variable names - each instance knows its type and will do the right thing regardless - and this is exactly what we said in the "Why Objects" section at the top!

###  Further reading

Other interesting examples of inheritance, polymorphism and the use of the ```super``` keyword can be found [here](https://www.python-course.eu/python3_inheritance.php) and [here](https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3).

**(C) 2014,2020 Fabrizio Smeraldi** ([f.smeraldi@qmul.ac.uk](mailto:f.smeraldi@qmul.ac.uk) - [web](http://www.eecs.qmul.ac.uk/~fabri/)), all rights reserved. In: "Computer Programming", School of Electronic Engineering and Computer Science, Queen Mary University of London.

---

# Regular expressions

## Regular expressions - Main Content

Regular expressions (or REGEX) are compact ways of summarising a text pattern. The need to handle text patterns is very common indeed: for instance typing
```
ls *.py
```
in a Linux shell will list all files that end in ```.py```. The character ```*``` is known as a *wildchar*. The above is known as *glob* syntax, and is not technically a REGEX; rather, regular expressions are major refinement of this concept.

Regular expressions help with extracting information from text (eg BLAST output or FASTA files) by locating particular patters. For instance, in a [FASTA](https://en.wikipedia.org/wiki/FASTA_format) file, the accession number may come between a ">" and a  "|": such a pattern can be easily described by a regular expression.
```
>P04637|P53_HUMAN Cellular tumor antigen p53 - Homo sapiens (Human).
```

Also, databases such as [PROSITE](http://prosite.expasy.org/) list *patterns* that identify particular families of proteins or domains; as we will see, from a computational point of view, these are really regular expressions in disguise.

Regular expression syntax in Python is very similar to PERL syntax, so migrating between the two languages should not be difficult.

## The ```re``` Module

In Python, REGEX support is provided in the ```re``` module. Simple usage is indeed straightforward: 

This is not too different from the ```.index()``` method of a string:


But it is a lot more flexible:

here the square brackets express an alternative within a set of characters.

If a match is not found, the search returns None:

## Performing matches

We have already seen ```.search()```, that finds the first match only, and ```.findall()```. 
The ```re``` module offers four matching operators:


| Function/Method   | Use                                                                          |
|-------------------|------------------------------------------------------------------------------|
| match()           | Determine if the RE matches at the beginning of the string.                  |
| search() 	        | Scan through a string, looking for any location where the RE matches.       |
| findall() 	    | Find all substrings where the RE matches, and returns them as a list.        |
| finditer() 	    | Find all substrings where the RE matches; returns match objects as an iterator(*).|

(*) an iterator works very much like a list in that for instance you can loop over it, but its items are computed on the fly as they are needed, so it is more memory-efficient. 


## Compiling a pattern

For reasons of efficiency, if a pattern is going to be used repeatedly, it is best to compile it. This is done as follows:

the same search functions listed above are available as methods of the *compiled expression* object ```rgx```.

## Beware of the backslash

Regular expressions are a powerful tool, though a bit tedious to learn. Besides matching very complex patterns indeed, other operations that are possible are splitting a string where a pattern matches and substitution. I invite you to have a look at the official [howto](https://docs.python.org/3/howto/regex.html) to get a feeling for what can be done.

As you will see, REGEX syntax makes heavy use of backslashes. This is a problem in Python, because a backslash is interpreted as an *escape character*. That is, a combination of a backslash and a standard character is normally translated to a non-printable character (for example a newline), according to this [table](http://www.python-ds.com/python-3-escape-sequences).

The solution is to use the Python "raw string" syntax by prepending an "r" (for "raw") to the string in question. This saves the backslash from being crunched as an escape sequence:

to be on the safe side, you may want to put an "r" before all of the regular expressions you write. Example:

If you would like more information about your matches, the ```finditer``` method may be a better option, since it returns the individual match objects for you to process.

## Text substitution

There are times when you may want to edit text automatically - for instance, you may want to remove all *http* links from a text you have scraped, remove [stop-words](https://en.wikipedia.org/wiki/Stop_word) from a document in preparation for some natural language processing, re-format telephone numbers or hide credit card numbers. The ```re``` module supports this through the ```re.sub``` function, that you can think of as a powerful programmatic *Find-and-Replace* tool. The documentation is [here](https://docs.python.org/3/library/re.html#re.sub), and usage is straightforward:  

The ```sub``` function is very flexible. You may be a bit disappointed that "Hallo" is uppercase, "hello" is lowercase, but it seems that we have to choose whether we want an uppercase "Bye" or a lowercase "bye". Of course we could use two separate expressions, but isn't there a way to match the case in one go? It turns out there is - we can pass a function as the ```repl``` argument, in which case that function is passed the match object and can use it to compute the appropriate replacement. In our case:

This gives you a lot of flexibility. For instance, you might need to update all hyperlinks in a website to reflect the new structure of the site: just code a REGEX that matches hyperlinks and a function that maps the old URLs to the new URLs (maybe simply using a dictionary), and hey presto.

## Matching PROSITE patterns


The [Thioredoxin](https://en.wikipedia.org/wiki/Thioredoxin) pattern listed on PROSITE under accession number [PS00194](http://prosite.expasy.org/PS00194) is the following:
```
[LIVMF]-[LIVMSTA]-x-[LIVMFYC]-[FYWSTHE]-x(2)-[FYWGTN]-C-[GATPLVE]-
[PHYWSTA]-C-{I}-x-{A}-x(3)-[LIVMFYWT].
```
Though the [syntax](https://prosite.expasy.org/prosuser.html#conv_pa) is different, this is really a regular expression, and we can easily translate it to a Python REGEX:
```
r'[LIVMF][LIVMSTA]\w[LIVMFYC][FYWSTHE]\w{2}[FYWGTN]C[GATPLVE][PHYWSTA]C[^I]\w[^A]\w{3}[LIVMFYWT]'
```
where ```\w``` matches any character, ```\w{3}``` matches exactly three characters and for example ```[^I]``` will match anything except an ```I```. The following code scans the chicken proteome for matches and prints out the accession number of the proteins that match. 

NOTE: the chicken proteome can be retrieved from the list of Uniprot reference proteomes for [Eukaryotes](https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Eukaryota/);
*Gallus gallus* is entry ```U000000539_*.fasta.gz```, where ```*``` stands for the current revision number.
Download the file, unzip it and rename it ```CHICK.fasta``` for convenience. I have included here a file named ```CHICK.fasta``` with a more or less outdated revision, I encourage you to fetch the current data; you may also download data for other organisms of your interest (the key to the file names is in the [README](https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/README) file in the parent directory on the Uniprot server). If you are running as a binder or on the QM JupyterHub instance, you may need to dowload the file locally to your machine and then upload it.

#### Warning! Real data - handle with care

```CHICK.fasta``` contains around 10Mb of data (almost 16,000 proteins, filling about 170K lines of text). This is by no means big data, but it is too large for you to open in an editor. The following code prints the first few lines of it:

**(C) 2014,2020 Fabrizio Smeraldi** ([f.smeraldi@qmul.ac.uk](mailto:f.smeraldi@qmul.ac.uk) - [web](http://www.eecs.qmul.ac.uk/~fabri/)), all rights reserved. In: "Computer Programming", School of Electronic Engineering and Computer Science, Queen Mary University of London.

## Regular expressions - Solutions

### Mistery pattern

What does the following regular expression match? Try to find out!
```
r"([A-Za-z0-9\.]+)@[A-Za-z0-9\.]*qmul\.ac\.uk"
```

When you have got it, try using the ```.search()``` function to return a matching object and  print ```.group(1)``` of the matching object. This corresponds to whatever matches the content of the first (and only) pair of brackets () in the pattern. What is it?

### Call me back

Write a function ```parseNumber``` that takes a string with a phone number as an argument, and returns a dictionary with the country code, area code (starting with zero) and number as separate strings.
So for instance the call
```
parseNumber("+44 (207) 882 5555")
```
should return the dictionary
```
{
    "country": "44",
    "area": "0207",
    "number": "8825555" # remove the spaces
}

```
Use grouping as in the example above; search for "Grouping" in the official [tutorial](https://docs.python.org/3/howto/regex.html) for more information. You can stick with this format, or try to cater for a few variants - for instance ```"(0207) 8825555"``` might return ```None``` for the country, and the rest as above. 
Simply return ```None``` if the number cannot be parsed. You may need a combination of regular expressions, string methods and ```if``` statements to get the job done.

In the solution below:
* we first remove spaces - this can be done using the ```str.replace``` method or ```re.sub``` (see [here](https://docs.python.org/3/library/re.html#sub))
* groups followed by a ```?``` are optional, if they are not matched they are set to ```None```
* nested groups are numbered in the order of the first bracket
* ```\(``` and  ```\)``` are literal brackets

### Books to scrape

The few lines of code below download the html source code of the home page of a simulated [bookstore](http://books.toscrape.com/) meant for web scraping practice. Write code that uses regular expressions to extract the title and price of the books listed on the page, and prints them out as comma-separated values:

```
A Light in the Attic,£51.77
Tipping the Velvet,£53.74
...
```
Hint: have a look at the web page first. Then print the ```html``` variable, and use the search function of your browser (generally CTRL-F) on the notebook to find occurrences of title words or prices in the source code of the page. Is there any regularity you can exploit? 


### An interactive tutorial

There are a number of interactive tutorials and puzzles on regular expressions online. Try this is one:
    
http://regexone.com/

**(C) 2014,2020 Fabrizio Smeraldi** ([f.smeraldi@qmul.ac.uk](mailto:f.smeraldi@qmul.ac.uk) - [web](http://www.eecs.qmul.ac.uk/~fabri/)), all rights reserved. In: "Computer Programming", School of Electronic Engineering and Computer Science, Queen Mary University of London.

---


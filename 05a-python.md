# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Python lists are a list of values that are mutable (values can be changed). Tuples are immutable lists (consisting values can not be changed). Dictionary keys are required to be immutable thus only tuples will be able to be used for dictionary keys.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> List and sets are both data structures of the Python and is a sequence of values. Biggest difference is that sets are unordered collections of unique values. Lists are ordered and can be iterated through. When looking for an element, sets are faster because set uses hash functions. In lists, each value has to be checked for equality. 

Example of List: list = [1,2,3,4]
Example of Set: set ={1,2,3,4}

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda functions are anonymous functions(functions without a name) that is executed immediately. Lambda functions are especially useful when passing functions to other functions. 

Example:
a = [(1, 2), (3, 1), (5, 10), (11, -3)]
a.sort(key=lambda x: x[1])

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension is a way to define and create python lists. Map function applies a passed in function to each item in the iterable and returns a list containing the results. Filter function extracts certain values in the iterable that will evaluates to true when passed through the function. 

Example of list comprehension: 
new_list = []
for i in old_list:
    if filter(i):
        new_list.append(expressions(i))

Filter equivalent of list comprehension: 
new_list = [expression(i) for i in old_list if filter(i)]

Use of map and lambda:
list(map((lambda x: x **2), items)
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)






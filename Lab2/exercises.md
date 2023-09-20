# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

*It is very important that to use a descriptive and meaningful name to describe the accurate purpose and behavior of the function to have more readable and clear code.
 After read the SL for dictionary and List's functions. A good example will be get(), which return the value for key if key is in the dictionary and that reflect the name of this function. *

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

*Lists are ordered, indexed by position, and suitable for sequences of values.
 Dictionaries are unordered, indexed by unique keys, and ideal for associating values with specific labels or identifiers.*

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

*Yes, list allows for random access. You can access any element in the list by using its index number. *

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

*Pros: Flexibility is the first reason. Containers that can store any data type, so you can work with different types of data within a single data structure.
 The second one will be easy to use and write code. When you use containers that don't need to worried about data types, you can reuse the same container and code for various purposes. You also can switch between data types without declaring them separately.
 Cons: The first one is the performance related. This type of containers need dynamic type checking and that may cause can slower execution and more memory usage.
 The second one is the difficulty of debugging. It is more harder to check bugs with generic data type rather than specific data type.*

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

*Functions in request are well named in the Request module. For example, the requests.get(url, params=None, **kwargs) function. It is clearly indicates the action of making a GET request to a specified URL.
 The second example will be requests.delete(url, **kwargs) function. This is clearly represent that send a delete request to the listed url. *

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

*Yes, there is a API have more than 5 arguments. For example, class requests.Request(method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None)*

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

*'**kwargs' is a special syntax in Python that allows you to pass a variable number of keyword arguments to a function or method. It collects these keyword arguments into a dictionary where the keys are the argument names, and the values are the corresponding values.
The good part of '**kwargs' is the flexibility in function. '**kwargs' allows you to add new keyword arguments without changing the function signature, and it is easier to extend and modify the function in the future.
When using '**kwargs' may case some issue that Users may not be aware of all the possible keyword arguments. Also, '**kwargs' may cause some debugging issue that it may not be clear which keyword arguments are commonly used and which are more specialized.*

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?


*When we setting the arguments to None as default values, it allows users to ignore those arguments when calling the method. Setting to None provide more flexible to users. Users can provide values for the arguments they care about and leave the rest as None to use default behavior.
 On the other hand, we can use other values as defaults as well, such as integers, strings, dictionaries to set the arguments. To use a meaningful and intuitive default values helps API more user-friendly and reduces potential errors.*
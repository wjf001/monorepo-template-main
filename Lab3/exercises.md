# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	- *The MObject class is a concrete class because it can be instantiated, but it didn't define any attributes or methods.*
1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- *when the instance is about to be destroyed will call '__del__'. This is also called a finalizer or (improperly) a destructor. If a base class has a __del__() method, the derived class’s __del__() method, if any, must explicitly call it to ensure proper deletion of the base class part of the instance.*
1. What class does Texture inherit from?
	- *The Texture class inherits from the Image class.*
1. What methods and attributes does the Texture class inherit from 'Image'? 
	- *The Texture class inherits all the methods and attributes from the Image class. Although there is nothing in the 'Texture' class, but we can can create a Texture object and use all of these methods and attributes.*
1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- *I think a texture should have a 'has-a' (composition) relationship. Composition means that changes to the component class rarely affect the composite class, and changes to the composite class never affect the component class. This provides better adaptability to change and allows applications to introduce new requirements without affecting existing code.*
    -     class Texture:
              def __init__(self, image):
                 self.image = image
1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- *Yes,if you didn't define a constructor for a class, then the Python will provide a default constructor.*

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?\
   *Singleton is not thread-safe, you will have to add a lock, which may slow down application. It is also hard to tell which thread last modified singleton*

*edit the code directly*  
  

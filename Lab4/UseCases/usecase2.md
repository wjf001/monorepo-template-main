**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 2

<hr>

**Use Case**: *Change drawing color using number keys*

**Primary Actor**: *User*

**Goal in Context**: *To change the drawing color by pressing number keys 1 through 8, with each key corresponding to a specific color.*

**Preconditions**: *The program must be running and in a responsive state. The Canvas must be setted up.*

**Trigger**: *The User presses a number key from 1 to 8.*
  
**Scenario**: *The User presses one of the number keys from 1 to 8. \
The application maps the number key to a specific color as follows:\
1 = Black\
2 = White\
3 = Red\
4 = Green\
5 = Blue\
6 = Yellow\
7 = Magenta\
8 = Cyan\
Color changed after press the key.\*
 
**Exceptions**: *If the User presses a number key that is not in the range 1 to 8, the application ignores this press input, and use the current color without change.
If an unexpected error happen, the app provides an error message and ask user to save and restart the app.*

**Priority**: *High-priority.*

**When available**: *First release*

**Channel to actor**: *The primary actor communicates through I/O devices. This includes the keyboard and the mouse. The system is responsible for maintaining focus of the window when the user clicks, and should respond within 1 second of any keyboard event. The user is responsible for all other input.*

**Secondary Actor**: *N/A*

**Channels to Secondary Actors**: *N/A*

**Open Issues**: *We may need to provide more color choice to users in the future.*

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)

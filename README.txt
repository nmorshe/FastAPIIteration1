Version 1 - 6/25/25

This project's purpose is meant to serve as practice with Python APIs as well as a serviceable skeleton 
for developing the backend of future full stack applications. 

This is meant to be an improvement over the previously built Flask API due to using more up to date
libraries and capabilities.

Currently capable of managing simple JSON data - next step later on is to get delete and put methods working
and connect to Firebase cloud services for storing/retrieving data. 


CHANGELOG - 6/26/25

Developed DELETE method and did extensive refactoring and error checking for previous methods. Next plans are to 
implement the PUT method and check for more possible refactoring possibilities.

CHANGELOG - 6/26/25 - 9:33 PM

Implemented PUT method and added more error checking elements - next focus is implementing more error checking and
trying to ensure better time complexity with functions and operations. Eventually planning on developing main.py to 
be a function that calls the api via uvicorn. As for Firebase integration - may implement that in a separate clone 
of this API.

CHANGELOG - 6/27/25 - 10:53 PM

Implemented bulk data posting as well as more refactoring of helper functions and REST functions to allow for less
repetitive function calls to be made to improve performance. Later goal is to develop main.py to activate api directly
via uvicorn.

CHANGELOG - 6/28/25 - 11:31 PM

Implemented main.py to be able to call the API via uvicorn, allowing for api.py to be called from the top-level file.
Also altered Firebase credentials to exist in api.py to handle build correctly. Overall the API appears to be finished, 
but more changes may occur in the future.

Am planning on using the design of this API to create multiple other APIs - next iteration will manage data through
a connection to Firestore, while later iterations I may try to experiment with nhost.
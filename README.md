# GUI DATABASE APP
### A SIMPLE (YET HARD TO MAKE) mood barometer database 
Ok, so i went for it. The biggest project so far and totally unprepared for this one. It has forced to me to google quite a few things.  But! I am almost done with my first actual database app. This project has taken me around a week or so so far, mostly a lot of it was wasted trying to make heads or tail of the frigging Google sheets API. Anyway eventually i decided to check out the section on Python and SQLite3 by Colt Steele's course on udemy. 

That got me started on this project, and hopefully allows me to prevent sql injections. (Not that i fully understand the repercussions)

i went with tkinter again given that the ttk version of the framework looks decent enough and i am knowledgeable on this framework. 

## SOME THINGS DIDN'T GO ACCORDING TO PLAN
#### Like how can i project  a raw sqlite object in a Tkinter Text widget????
After jumping from Google sheets, i landed on SQLite3 and decided to work with that to develop my database app. Except i am struggling with my inexperience in this project and i ended up unable to display the sqlite data from my table into tkinter for review. While as i understand it, studying the data and such is something normally reserved for the command line tools. I was hoping that i could access the data in house so that i did not had to dig through the files or open VSCode to view the data. 

#### Writing and formatting a txt file. 
So i decided to write the app in such a way that i took an individual data row and fed the raw input to a txt file. My hope is to be able to create a function that allows me to iterate over either itself or some range and create separate txt files. 
Yet while the function can take the values that i hard coded to the tkinter text widget anything else i add gets dropped. 

### GLITCHES I KNOW OF...
##### ONLY ONE I CAN THINK, AND IT IS:
When i press the command button to add values to the database and when i press the button to open the tkinter text widget window. It does not seem to put the data together with text.  
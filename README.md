# SP-Homework03

In order to successfully complete this homework you will need to
make your own **CSV** (*Comma-separated values*) **parser**. Records
inside the CSV file will be comma delimited `,` without enclosing
double quotes `”`. 

Your task will be to make a function that will read CSV file into
a list of dictionaries where each dictionary represents a single 
record (line) inside a file.

First row of the file will be used as header which will contain
column names which will become dictionary keys.

Please check the example below.

The following file:
```
name,surname,dob
John,Doe,1969-09-01
Clark,Kent,1988-01-01
```
Should look in Python like this:
```
file_records = [{“name”:”John”, “surname”:”Doe”,”dob”:”1969-09-01”},
            {“name”:”Clark”, “surname”:”Kent”,”dob”:”1988-01-01”}]
```

In order to have your homework reviewed please fork this project.
Deadline for homework submission is 11th October 2018 till midnight.


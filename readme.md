# Faker, Generating test data, and adding your package to command line app.

For this homework. what you need to do is add the following features to **your own** calculator project:

1. Add the "faker" libary with the command "pip install faker" and then do a pip freeze > requirements.txt.  **Tip:  First Deactivate the virtual environment with the command "deactivate" and then activate it again** This is so that you will only add faker to the requirements and that your virtual environent is the current one that your working on when faker is installed.  Review the faker website [here](https://faker.readthedocs.io/en/master/#).  Once you add the library you need to update your tests to use the fake data.  Do a basic implementation first and understand how it works.  Review the faker library documentation, its important that you learn how faker works because it's an invaluable tool for development.

2. Add a new command to pytest to generate  N number of records, so that you can run the following command: **pytest --num_records=100** to generate 100 records.  **The code to do this is in the tests/conftest.py file** and is a little complicated but ask ChatGPT, or me and study it a bit.  Basically what happens is that records are generated and in the background the parameters for a,b,operation, expected result are created and there is a special method to generate test data that is automaticly called when these variables are passed in, so it just keeps calling the test function to test it.  You kinda just need to have a leap of faith that its going to work, since the pytest library is doing all the work in the background.

3. Add a main.py file to serve as an entry point to your program and add the code from my main.py, so that you can have some exception handling to your program.  Review the code in main.py to see how exceptions are caught when bad input is submitted by the user of your program.  

### The command you add will be able to handle the following test cases (see my test_main.py test file):
* a, b, operation, expected result
* "5", "3", 'add', "The result of 5 add 3 is equal to 8"
* "10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"
* "4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"
* "20", "4", 'divide', "The result of 20 divide 4 is equal to 5"
* "1", "0", 'divide', "An error occurred: Cannot divide by zero"  
* "9", "3", 'unknown', "Unknown operation: unknown"  # Test for unknown operation
* "a", "3", 'add', "Invalid number input: a or 3 is not a valid number."  # Testing invalid number input
* "5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number." # Testing another invalid number input


## Submission Instructions
1.  Use the repo from your previous assignment and update it with the features above.  Use a branch for each feature and get each feature to work and then merge it.  Branch -> complete feature -> merge -> repeat for each feature

2.  Submit a link to your repository to Canvas when your finished.

## Grading:

1.  30 Points - Faker 
2.  30 Points - Test Data Generation
3.  40 Points - User Input

## To get my code to run / Install Instructions

1.  Clone the repo
2.  CD into the repo directory
3.  Create the virtual environment
4.  Activate the virtual environment
5.  Install the requirements with pip or pip3 install requirements.
6.  Try out the test data functionality "pytest --num_records=100"
7.  Try out the user input functionality on the command line: "python main.py 1 2 add"

### Testing Instructions
* pytest --num_records=10
* pytest --pylint --cov 


Basic tips:
* Don't repeat yourslf #1 rule
* Separate each thing the program needs to do, so its organized and your functions only do one thing


You should create new branches for each version of your progarm and work from the most simple, which is the first branch (main) and then keep upgrading your program until you have all of the requirements met.  Please don't just copy and paste my final program, or you will not learn anything.  Soon you will have to design your own program without any examples, which will be your mid-term.  I have commented the code with explanations, so you can understand it better.   


## Instructor Video and Required Readings

1.  Instructor Video 1 Faker and Test Data Generation - [here](https://youtu.be/4x6JP0eUVzo)
2.  [Python Try Accept](https://www.geeksforgeeks.org/python-try-except/)
3.  [Python Command Line Arg Parsing](https://realpython.com/command-line-interfaces-python-argparse/)
4.  [Python Faker Library Standard Fake Data Available](https://faker.readthedocs.io/en/stable/providers.html)
5.  [Using Python Fake and Synthetic Data](https://www.udacity.com/blog/2023/03/creating-fake-data-in-python-using-faker.html)
6.  [Pytest and Generating Data GOod explanation](https://pytest-with-eric.com/introduction/pytest-generate-tests/)

# Worlder TASK 2
This repository is created for Task 2: Knowledge of Security Vulnerabilities.
For this task, I chose to demonstrate the following three common security vulnerabilities:

1. SQL injection–prone input handling
2. Insecure file handling
3. Missing input validation

To demonstrate these issues clearly, I created two Python scripts:
vulnerable.py – insecure version
secure.py – secure version
Since SQL injection is one of the selected vulnerabilities, I also created a separate script called database.py, which creates a SQLite database containing sample user records.

In vulnerable.py, the get_user() function takes a user ID as an argument and returns the corresponding record of the user from the database. However, the SQL query is built using the provided user input without any validation. This leads to a SQL injection vulnerability in the function. For example, if the user enters a string ' OR '1'='1 to the function instead of a valid ID, it impacts the query logic, returning data from all records in the database. This indicates a lack of validation of the input provided to the function.
The same script also comprises the readfile() function, which is responsible for the reading of files on the filesystem based on user input. The function is prone to the path traversal attack because the user’s input for the filepath is neither validated nor restricted. This also shows the file input is not handled properly. The user can gain access to the sensitive files, including the admin.txt file, which is the administrative file. This can be achieved through the use of the directory traversal character sequence like ../admin_access/admin.txt.

These security flaws are addressed in the secure.py script. In this script the user input is first cleaned by removing unnecessary whitespace and special characters. The input is then passed to a validation function that ensures only numeric user IDs are accepted. If the user ID corresponds to the administrator account (ID 1), the request is rejected to prevent sensitive information.
Additionally, the database query is rewritten using parameterized statement, ensuring that user input is treated strictly as data rather than executable code. This mitigates SQL injection attacks with proper input validation.
The readfile() function in secure.py is also secured by restricting file access to a predefined directory using a directory variable. The resolved file path is validated to ensure it remains within the allowed directory, preventing directory traversal attacks and unauthorized file access.


# How to run
I ran this in an IDE (VS CODE) and that would be easy to check this.
Run the database.py at first.
In the line 5 of the vulnerable.py and in line 21 of the secure.py, change the path of the users.db. 

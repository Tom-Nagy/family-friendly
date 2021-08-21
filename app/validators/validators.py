import re
from flask import Flask, request

# Credit to GeeksforGeeks for password implementation, validation;
# adapted to the website needs
# (https://www.geeksforgeeks.org/password-validation-in-python/)

# variables
pass_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,30}$"


def validate_passwords(password, conf_password):
    # compiling regex
    pattern = re.compile(pass_pattern)

    # searching regex
    match_one = re.search(pattern, password)
    match_two = re.search(pattern, conf_password)

    # validating conditions
    if match_one and match_two and password == conf_password:
        return True

# End Credit

# 📧 Email Validation Program

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A simple yet effective Python program that checks whether an email is valid based on multiple conditions including syntax, characters, and domain rules. It gives specific error codes and reasons for invalid inputs, helping users understand what went wrong.

## ✅ Features

This email validation program can perform the following validations:

1. Detects if the **first letter** of the email is alphabetic.
2. Counts the number of **@** signs – ensures there’s exactly one.
3. Checks for allowed **top-level domains**: `.com` and `.in`. *(More can be added manually.)*
4. Ensures only `.com` or `.in` are used as domains.
5. Disallows emails that contain:
   - Spaces
   - Underscores (`_`)
   - Extra dots (`.` not in domain)
   - Capital letters
6. Provides **specific error messages with error codes** when invalid.
7. Asks the user to input:
   - `1` to get a detailed reason for the invalid email
   - `0` to exit the program

## 🛠️ Technologies Used

- **Python** – Core programming logic
- **No external libraries** – Simple input, conditionals, and string functions

## 📋 Validation Criteria

### ✅ Valid Email Conditions

- Minimum **6 characters** long  
- Starts with a **letter**  
- Contains exactly **1 '@'**  
- Ends with **'.com'** or **'.in'**  
- Contains only **lowercase alphabets, numbers, and allowed symbols** (`@`, `.`, no spaces or uppercase)  

### ❌ Invalid Email Triggers

Each invalid case is linked to a specific error number:
- `Error 1` – Too short
- `Error 2` – First character not a letter
- `Error 3` – Zero or multiple `@`
- `Error 4` – Missing domain or space at the end
- `Error 5` – Contains space, capital letters, or invalid characters

## 🧠 Lessons Learned

1. Used character-by-character inspection for email input
2. Applied conditions with logical operators and flags
3. Integrated user-driven error feedback
4. Gained better understanding of valid email syntax rules

## 🧪 Example

```bash
Enter your Email:
> g@g.com

Right Email!
Enter your Email:
> 9g@.com

Email incorrect!
Error number: 2
Enter 1 for error detail and enter 0 to exit the email checking:
> 1

Error number:2
Which means that your email address' first letter is a non-alphabatic or it is a space
Which is not valid.
```


## 🚀 How to Run
```
# Save the code in a file called email_validator.py and run it using:
python email_validator.py
```

## 📄 License
This project is licensed under the MIT License.
See the LICENSE file for full details.

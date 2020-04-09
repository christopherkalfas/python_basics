import sys

MASTER_PASSWORD = "opensesame"
password = input("Please enter secret password: ")
attempt_count = 1
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("Too many invalid tries")
    password = input("Invalid password, try again.")
    attempt_count += 1
print("Nice, job. You're in!")
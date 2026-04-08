import re

# File names
input_file = "input.txt"
output_file = "extracted_emails.txt"

# Regular expression pattern for email addresses
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

try:
    # Open and read input file
    with open(input_file, 'r') as file:
        content = file.read()

    # Extract email addresses
    emails = re.findall(email_pattern, content)

    # Write extracted emails to output file
    with open(output_file, 'w') as file:
        for email in emails:
            file.write(email + "\n")

    print("Email extraction completed successfully!")
    print(f"Total emails found: {len(emails)}")

except FileNotFoundError:
    print("Input file not found. Please check the file name.")

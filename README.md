# Validate emails using MX records

Python script to clean your contact, marketing emails list of bad emails with invalid MX records. 

Notice : It doesn't fully validate that an email already exists and legit but it helps cleaning your list a little bit.

Since It's free and unlimited consider using it on your emails list before using a paid email validation service in order to reduce costs.

## How to use

First, install `dnspython` library using `pip install dnspython` command then run thee script using `python validate_emails.py`.

Enter threads number. While choosing the threads number, consider your cpu and network capabilities, the higher threads number the least processing time during the execution your maching performance may be affected.

Finally, Enter the emails list path and wait for the script to finish. The valid emails will be saved in `valid_emails.txt` file.


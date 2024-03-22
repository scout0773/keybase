# Keybase PGP Decoder

## Overview
The Keybase PGP decoder is a Python script designed to fetch PGP public keys from Keybase.io for a list of usernames provided in a text file. It decodes the base64-encoded PGP keys and extracts valid email addresses contained within them. The script then writes the valid usernames and corresponding email addresses to a file named `valid.txt`.

## Features
- Fetches PGP public keys from Keybase.io for provided usernames.
- Decodes base64-encoded PGP keys and extracts valid email addresses.
- Writes valid usernames and corresponding email addresses to a file.

## Requirements
- Python 3.x
- Requests library (can be installed via `pip install requests`)

## Usage
1. Clone this repository to your local machine.
2. Create a text file named `usernames.txt` containing the usernames for which you want to fetch PGP keys, with each username on a new line.
3. Run the script by executing `python main.py`.
4. Check the `valid.txt` file generated in the same directory for the list of valid usernames and corresponding email addresses.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to adjust or add more details as needed. Let me know if you need further assistance!

from fetch import fetch_pgp_keys
from functions.decode import decode_pgp_keys
from extract import extract_emails
from write import write_to_file

def main():
    with open("usernames.txt", "r") as file:
        usernames = file.readlines()
        for username in usernames:
            username = username.strip()
            pgp_key_base64 = fetch_pgp_keys(username)
            if pgp_key_base64:
                decoded_pgp_key = decode_pgp_keys(pgp_key_base64)
                if decoded_pgp_key:
                    valid_emails = extract_emails(decoded_pgp_key)
                    write_to_file(username, valid_emails)

if __name__ == "__main__":
    main()
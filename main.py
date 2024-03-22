import requests
import re
import base64

def fetch_and_decode_pgp_keys(username):
    keybase_url = f"https://keybase.io/{username}/pgp_keys.asc"
    
    try:
        response = requests.get(keybase_url)
        response.raise_for_status()
        pgp_key_block = response.text
        pattern = re.compile(r'(?<=-----BEGIN PGP PUBLIC KEY BLOCK-----)(.*?)(?=-----END PGP PUBLIC KEY BLOCK-----)', re.DOTALL)
        matches = pattern.findall(pgp_key_block)
        if matches:
            pgp_key_base64 = matches[0].strip()
            decoded_pgp_key = base64.b64decode(pgp_key_base64).decode('latin1')
            email_pattern = re.compile(r'<([^<>]+)>')
            email_matches = email_pattern.findall(decoded_pgp_key)
            valid_emails = [email for email in email_matches if '@' in email and re.match(r'^[\w\.-]+@[\w\.-]+$', email)]
            if valid_emails:
                with open("valid.txt", "a") as valid_file:
                    for email in valid_emails:
                        valid_file.write(f"{username}:{email}\n")
            else:
                print(f"No valid email found for {username}.")
        else:
            print(f"No PGP key found for {username}.")
    except Exception as e:
        print(f"Error occurred while fetching or decoding PGP key for {username}: {str(e)}")

def main():
    with open("usernames.txt", "r") as file:
        usernames = file.readlines()
        for username in usernames:
            fetch_and_decode_pgp_keys(username.strip())

if __name__ == "__main__":
    main()
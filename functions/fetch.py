import requests
import re

def fetch_pgp_keys(username):
    keybase_url = f"https://keybase.io/{username}/pgp_keys.asc"
    
    try:
        response = requests.get(keybase_url)
        response.raise_for_status()
        pgp_key_block = response.text
        pattern = re.compile(r'(?<=-----BEGIN PGP PUBLIC KEY BLOCK-----)(.*?)(?=-----END PGP PUBLIC KEY BLOCK-----)', re.DOTALL)
        matches = pattern.findall(pgp_key_block)
        if matches:
            return matches[0].strip()
        else:
            return None
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"PGP key not found for {username}")
        else:
            print(f"Couldn't fetch PGP key for {username}: {str(e)}")
        return None
    except Exception as e:
        print(f"Error occurred while fetching PGP key for {username}: {str(e)}")
        return None
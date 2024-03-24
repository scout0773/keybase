import base64

def decode_pgp_keys(pgp_key_base64):
    try:
        decoded_pgp_key = base64.b64decode(pgp_key_base64).decode('latin1')
        return decoded_pgp_key
    except Exception as e:
        print(f"Error occurred while decoding PGP key: {str(e)}")
        return None
import re

def extract_emails(decoded_pgp_key):
    email_pattern = re.compile(r'<([^<>]+)>')
    email_matches = email_pattern.findall(decoded_pgp_key)
    valid_emails = [email for email in email_matches if '@' in email and re.match(r'^[\w\.-]+@[\w\.-]+$', email)]
    return valid_emails
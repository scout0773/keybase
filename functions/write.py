def write_to_file(username, emails):
    if emails:
        with open("valid.txt", "a") as valid_file:
            for email in emails:
                valid_file.write(f"{username}:{email}\n")
    else:
        print(f"No valid email found for {username}.")
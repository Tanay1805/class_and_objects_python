def extract_username_and_domain(email):
    
    username, domain = email.split('@', 1)

    
    result_tuple = (username, domain)

    return result_tuple


email_address = input("Enter an email address: ")

try:
    username, domain = extract_username_and_domain(email_address)
    print(f"Username: {username}")
    print(f"Domain: {domain}")
except ValueError:
    print("Invalid email address format.")

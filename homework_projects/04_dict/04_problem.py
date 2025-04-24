from hashlib import sha256

def log_in(email, password, stored_logins):
    
     return stored_logins[email] == hash_password(password)
        
def hash_password(password):
    """
    Takes in a password and returns the SHA256 hashed value for that specific password.
    
    Inputs:
        password: the password we want
    
    Outputs:
        the hashed form of the input password
    """

    return sha256(password.encode()).hexdigest()

def main():
    # stored_logins is a dictionary with emails as keys and hashed passwords as values
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
    }
    
    print(log_in("example@gmail.com", "word", stored_logins ))
    print(log_in("example@gmail.com", "password",stored_logins ))
    
    print(log_in("code_in_placer@cip.org","Karel", stored_logins ))
    print(log_in("code_in_placer@cip.org", "karel", stored_logins ))
    
    print(log_in("student@stanford.edu","password", stored_logins ))
    print(log_in("student@stanford.edu", "123!456?789", stored_logins))


if __name__ == '__main__':
    main()
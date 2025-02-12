import bcrypt

# Sample database (Replace with actual DB in production)
user_db = {}

def register_user(email, password, phone):
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    user_db[email] = {'password': hashed_pw, 'phone': phone}
    print("User registered successfully!")

def validate_user(email, password):
    if email in user_db:
        hashed_pw = user_db[email]['password']
        return bcrypt.checkpw(password.encode(), hashed_pw)
    return False


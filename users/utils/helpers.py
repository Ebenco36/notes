import secrets

def generate_reset_token():
    # Generate a random hexadecimal token with a recommended length
    token_length = 32  # You can adjust the length as needed
    token = secrets.token_hex(token_length)
    return token

import pyotp

def generate_otp(secret_key):
    totp = pyotp.TOTP(secret_key)
    return totp.now()

def verify_otp(secret_key, entered_otp):
    totp = pyotp.TOTP(secret_key)
    return totp.verify(entered_otp)
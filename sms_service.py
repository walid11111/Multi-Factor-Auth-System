import random


def send_sms_otp(phone):
    # Generate a random OTP
    otp = str(random.randint(100000, 999999))

    # Simulate SMS sending by printing the OTP to the console
    print(f"Simulated SMS to {phone}: Your OTP is {otp}")

    return otp


#  mailhig open karo ta ke connect hujai

from auth import register_user, validate_user, user_db
from email_service import send_email_otp
from sms_service import send_sms_otp

def main():
    print("Welcome to Multi-Factor Authentication System")
    while True:
        choice = input("1. Register\n2. Login\n3. Exit\nChoose an option: ")
        if choice == '1':
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            phone = input("Enter your phone number: ")
            register_user(email, password, phone)
        elif choice == '2':
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if validate_user(email, password):
                # Email OTP Verification
                email_otp = send_email_otp(email)
                entered_email_otp = input("Enter the OTP sent to your email: ")
                if entered_email_otp != email_otp:
                    print("Invalid email OTP!")
                    continue

                # SMS OTP Verification
                phone = user_db[email]['phone']
                sms_otp = send_sms_otp(phone)
                entered_sms_otp = input("Enter the OTP sent to your phone: ")
                if entered_sms_otp != sms_otp:
                    print("Invalid SMS OTP!")
                    continue

                print("Login successful!")
            else:
                print("Invalid email or password!")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

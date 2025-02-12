
# Multi-Factor Authentication System

## Introduction
This project implements a secure login system using **Two-Factor Authentication (2FA)**, requiring both **email-based OTP** and **SMS-based OTP** for authentication. It enhances account security by adding an extra verification layer to prevent unauthorized access.

## Features
- **User Registration**: Users provide an email, password (hashed using bcrypt), and phone number.
- **Secure Login**: Users enter credentials and verify OTPs sent via email and SMS.
- **Strong Security**: Uses bcrypt for password hashing and OTP verification for added protection.
- **User-Friendly GUI**: Built with Tkinter for easy interaction.

## How It Works
1. **Registration**: Users enter their details. Passwords are securely stored using bcrypt hashing.
2. **Login**: Users enter their email and password; if correct, OTP verification is triggered.
3. **OTP Verification**: A **6-digit OTP** is sent via email and SMS. Users must enter both OTPs to log in successfully.

## Key Components
- **Python Backend**: Manages registration, login, and OTP verification.
- **MailHog**: Used for email OTP testing during development.
- **Tkinter GUI**: Provides an interactive user interface.
- **SMS Simulation**: Prints OTPs in the console for development testing.

## Tools Used
- **bcrypt** - Secure password hashing
- **MailHog** - Email testing tool
- **Tkinter** - GUI framework
- **Python Modules** - Backend logic implementation

## Benefits
✅ **High Security** - Strong authentication with passwords and OTPs.  
✅ **User-Friendly** - Simple and intuitive registration and login flow.  
✅ **Flexible Development** - Easily integrable into real-world applications.  

## Demo Flow
1. User registers with email, password, and phone number.
2. User logs in with their email and password.
3. User verifies email and SMS OTPs.
4. Successful login message is displayed.

## Conclusion
This **Multi-Factor Authentication System** ensures enhanced security with a dual OTP verification mechanism. It prevents unauthorized access and is designed to be easily implemented in various applications.

---
**Developed by:** Walid Khan 🚀

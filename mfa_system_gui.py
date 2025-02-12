import tkinter as tk
from tkinter import messagebox
from auth import register_user, validate_user, user_db
from email_service import send_email_otp
from sms_service import send_sms_otp

class MFAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Factor Authentication System")

        # Frames for different sections
        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=20)

        self.email_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.otp_var = tk.StringVar()

        self.email_otp = None
        self.sms_otp = None

        self.create_widgets()

    def create_widgets(self):
        self.register_button = tk.Button(self.frame, text="Register", command=self.show_register)
        self.register_button.grid(row=0, column=0, padx=10, pady=10)

        self.login_button = tk.Button(self.frame, text="Login", command=self.show_login)
        self.login_button.grid(row=0, column=1, padx=10, pady=10)

        self.exit_button = tk.Button(self.frame, text="Exit", command=self.root.quit)
        self.exit_button.grid(row=0, column=2, padx=10, pady=10)

    def show_register(self):
        self.clear_frame()
        self.frame_register = tk.Frame(self.root)
        self.frame_register.pack(padx=20, pady=20)

        tk.Label(self.frame_register, text="Email:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(self.frame_register, textvariable=self.email_var).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_register, text="Password:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(self.frame_register, textvariable=self.password_var, show="*").grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame_register, text="Phone:").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(self.frame_register, textvariable=self.phone_var).grid(row=2, column=1, padx=5, pady=5)

        self.register_submit_button = tk.Button(self.frame_register, text="Register", command=self.register_user)
        self.register_submit_button.grid(row=3, column=0, columnspan=2, pady=10)

    def register_user(self):
        email = self.email_var.get()
        password = self.password_var.get()
        phone = self.phone_var.get()
        if email and password and phone:
            register_user(email, password, phone)
            messagebox.showinfo("Success", "User registered successfully!")
            self.show_login()
        else:
            messagebox.showerror("Error", "Please fill all fields.")

    def show_login(self):
        self.clear_frame()
        self.frame_login = tk.Frame(self.root)
        self.frame_login.pack(padx=20, pady=20)

        tk.Label(self.frame_login, text="Email:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(self.frame_login, textvariable=self.email_var).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_login, text="Password:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(self.frame_login, textvariable=self.password_var, show="*").grid(row=1, column=1, padx=5, pady=5)

        self.login_submit_button = tk.Button(self.frame_login, text="Login", command=self.login_user)
        self.login_submit_button.grid(row=2, column=0, columnspan=2, pady=10)

    def login_user(self):
        email = self.email_var.get()
        password = self.password_var.get()
        if validate_user(email, password):
            self.otp_verification(email)
        else:
            messagebox.showerror("Error", "Invalid email or password!")

    def otp_verification(self, email):
        self.clear_frame()
        self.frame_otp = tk.Frame(self.root)
        self.frame_otp.pack(padx=20, pady=20)

        # Email OTP generation and verification
        self.email_otp = send_email_otp(email)
        tk.Label(self.frame_otp, text="Enter the OTP sent to your email:").grid(row=0, column=0, padx=5, pady=5)
        email_otp_entry = tk.Entry(self.frame_otp, textvariable=self.otp_var)
        email_otp_entry.grid(row=0, column=1, padx=5, pady=5)

        self.email_otp_button = tk.Button(self.frame_otp, text="Verify Email OTP", command=lambda: self.verify_email_otp(email_otp_entry))
        self.email_otp_button.grid(row=1, column=0, columnspan=2, pady=10)

    def verify_email_otp(self, email_otp_entry):
        if self.otp_var.get() == self.email_otp:
            # SMS OTP generation and verification
            phone = user_db[self.email_var.get()]['phone']
            self.sms_otp = send_sms_otp(phone)
            self.sms_verification()
        else:
            messagebox.showerror("Error", "Invalid email OTP!")

    def sms_verification(self):
        tk.Label(self.frame_otp, text="Enter the OTP sent to your phone:").grid(row=2, column=0, padx=5, pady=5)
        sms_otp_entry = tk.Entry(self.frame_otp, textvariable=self.otp_var)
        sms_otp_entry.grid(row=2, column=1, padx=5, pady=5)

        self.sms_otp_button = tk.Button(self.frame_otp, text="Verify SMS OTP", command=lambda: self.verify_sms_otp(sms_otp_entry))
        self.sms_otp_button.grid(row=3, column=0, columnspan=2, pady=10)

    def verify_sms_otp(self, sms_otp_entry):
        if self.otp_var.get() == self.sms_otp:
            messagebox.showinfo("Success", "Login successful!")
            self.show_login()
        else:
            messagebox.showerror("Error", "Invalid SMS OTP!")

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MFAApp(root)
    root.mainloop()

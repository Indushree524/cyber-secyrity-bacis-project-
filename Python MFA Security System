import tkinter as tk
from tkinter import messagebox
import hashlib
import secrets
import time
import hmac

# User database
users = {}

# OTP settings
otp_store = {}
MAX_ATTEMPTS = 3
login_attempts = {}


def hash_password(password, salt):
    return hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        200000
    ).hex()


def register():
    username = reg_user.get().strip()
    password = reg_pass.get()

    if not username or not password:
        messagebox.showerror("Error", "Enter all details")
        return

    if len(password) < 8:
        messagebox.showerror(
            "Error", "Password must be at least 8 characters"
        )
        return

    if username in users:
        messagebox.showerror("Error", "User already exists")
        return

    salt = secrets.token_bytes(16)
    password_hash = hash_password(password, salt)

    users[username] = {
        "salt": salt,
        "password": password_hash
    }

    messagebox.showinfo("Success", "Registration successful!")

    reg_user.delete(0, tk.END)
    reg_pass.delete(0, tk.END)


def login():
    username = login_user.get().strip()
    password = login_pass.get()

    if login_attempts.get(username, 0) >= MAX_ATTEMPTS:
        messagebox.showerror("Blocked", "Maximum attempts reached")
        return

    if username not in users:
        login_attempts[username] = login_attempts.get(username, 0) + 1
        messagebox.showerror("Error", "Invalid credentials")
        return

    user = users[username]
    entered_hash = hash_password(password, user["salt"])

    if not hmac.compare_digest(entered_hash, user["password"]):
        login_attempts[username] = login_attempts.get(username, 0) + 1
        messagebox.showerror("Error", "Invalid credentials")
        return

    login_attempts[username] = 0
    generate_otp(username)


def generate_otp(username):
    otp = f"{secrets.randbelow(1000000):06d}"

    otp_store[username] = {
        "code": otp,
        "expiry": time.time() + 60
    }

    # Demonstration: OTP appears in the application popup.
    messagebox.showinfo(
        "OTP Generated",
        f"Your verification OTP is: {otp}\nValid for 60 seconds."
    )

    otp_window = tk.Toplevel(root)
    otp_window.title("OTP Verification")
    otp_window.geometry("300x200")

    tk.Label(
        otp_window,
        text="Enter your OTP",
        font=("Arial", 14)
    ).pack(pady=15)

    otp_entry = tk.Entry(otp_window)
    otp_entry.pack(pady=10)

    def verify():
        entered = otp_entry.get()

        stored = otp_store.get(username)

        if not stored:
            messagebox.showerror("Error", "OTP not found")
            return

        if time.time() > stored["expiry"]:
            messagebox.showerror("Expired", "OTP has expired")
            otp_store.pop(username, None)
            otp_window.destroy()
            return

        if hmac.compare_digest(entered, stored["code"]):
            otp_store.pop(username, None)
            messagebox.showinfo(
                "Access Granted",
                f"Welcome {username}!\nLogin successful."
            )
            otp_window.destroy()
        else:
            messagebox.showerror("Error", "Incorrect OTP")

    tk.Button(
        otp_window,
        text="Verify OTP",
        command=verify,
        bg="green",
        fg="white"
    ).pack(pady=10)


# Main window
root = tk.Tk()
root.title("Advanced MFA Security System")
root.geometry("450x500")
root.resizable(False, False)

tk.Label(
    root,
    text="MULTI-FACTOR AUTHENTICATION",
    font=("Arial", 16, "bold"),
    fg="blue"
).pack(pady=20)

# Registration section
tk.Label(
    root,
    text="NEW USER REGISTRATION",
    font=("Arial", 12, "bold")
).pack(pady=10)

reg_user = tk.Entry(root, width=30)
reg_user.pack(pady=5)
reg_user.insert(0, "")

reg_pass = tk.Entry(root, width=30, show="*")
reg_pass.pack(pady=5)

tk.Button(
    root,
    text="Register",
    command=register,
    bg="orange",
    width=20
).pack(pady=10)

# Login section
tk.Label(
    root,
    text="USER LOGIN",
    font=("Arial", 12, "bold")
).pack(pady=10)

login_user = tk.Entry(root, width=30)
login_user.pack(pady=5)

login_pass = tk.Entry(root, width=30, show="*")
login_pass.pack(pady=5)

tk.Button(
    root,
    text="Login",
    command=login,
    bg="green",
    fg="white",
    width=20
).pack(pady=15)

tk.Label(
    root,
    text="Password + OTP Verification",
    fg="gray"
).pack(pady=10)

root.mainloop()

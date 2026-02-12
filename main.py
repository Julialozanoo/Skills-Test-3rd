from pyscript import document, display

def verify_account(event):
    username = document.getElementById("username").value
    password = document.getElementById("password").value

    output = document.getElementById("output")
    output.innerHTML = ""

    if len(username) < 7:
        output.innerHTML = "Username must be at least 7 characters long."
        return

    has_letter = any(c.isalpha() for c in password)
    has_number = any(c.isdigit() for c in password)
    long_enough = len(password) >= 10

    if not has_letter:
        output.innerHTML = "Password must contain at least one letter."
        return

    if not has_number:
        output.innerHTML = "Password must contain at least one number."
        return

    if not long_enough:
        output.innerHTML = "Password must be at least 10 characters long."
        return

    output.innerHTML = "Account Created."
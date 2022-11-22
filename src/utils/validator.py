from email_validator import validate_email, EmailNotValidError

def check_email(email: str) -> bool:
    try:
        validation = validate_email(email)
        return True
    except EmailNotValidError as ex:
        return False

def check_name(name: str) -> bool:
    if len(name.split(' ')) == 3:
        return True
    else:
        return False

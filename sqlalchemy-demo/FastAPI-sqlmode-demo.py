def log_access(func):
    def wrapper(user):
        print(f"User '{user}' accessed '{func.__name__}'")
        return func(user)
    return wrapper

@log_access
def view_dashboard(user=None):
    print(f"{user} displaying dashboard...")

@log_access
def edit_profile(user=None):
    print(f"{user} editing profile...")

view_dashboard(user="Alice")
edit_profile(user="Bob")

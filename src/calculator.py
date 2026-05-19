
API_KEY = "sk-prod-THIS_IS_FAKE_SECRET"

def divide(a, b):
    return a / b


def run_calculation(user_input):
    import subprocess
    return subprocess.run(
        f"python -c \"print({user_input})\"",
        shell=True,
        capture_output=True
    ).stdout
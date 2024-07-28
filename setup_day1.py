import os
import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_python():
    try:
        python_version = subprocess.check_output(["python", "--version"])
        print(f"Python is already installed: {python_version.decode().strip()}")
    except FileNotFoundError:
        print("Python is not installed. Please install Python from the official website: https://www.python.org/downloads/")
        sys.exit(1)

def check_and_install_django():
    try:
        import django
        print(f"Django is already installed: {django.get_version()}")
    except ImportError:
        print("Django is not installed. Installing Django...")
        install_package("django")
        print("Django installed successfully.")

def check_and_install_git():
    try:
        git_version = subprocess.check_output(["git", "--version"])
        print(f"Git is already installed: {git_version.decode().strip()}")
    except FileNotFoundError:
        print("Git is not installed. Please install Git from the official website: https://git-scm.com/downloads/")
        sys.exit(1)

def initialize_git_repo():
    if not os.path.exists(".git"):
        print("Initializing Git repository...")
        subprocess.check_call(["git", "init"])
        subprocess.check_call(["git", "add", "."])
        subprocess.check_call(["git", "commit", "-m", "Initial commit - project structure setup"])
        print("Git repository initialized and initial commit made.")
    else:
        print("Git repository already initialized.")

if __name__ == "__main__":
    base_path = os.getcwd()
    print(f"Working directory: {base_path}")

    check_and_install_python()
    check_and_install_django()
    check_and_install_git()
    initialize_git_repo()

    print("Day 1 setup completed successfully.")

import subprocess


def format_code():
    """Run black, isort, and flake8 on the codebase."""
    print("Formatting code with black...")
    subprocess.run(["black", "."])

    print("Sorting imports with isort...")
    subprocess.run(["isort", "."])

    print("Linting code with flake8...")
    subprocess.run(["flake8", "."])


if __name__ == "__main__":
    format_code()

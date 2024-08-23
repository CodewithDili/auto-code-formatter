Automated Code Formatter

The Automated Code Formatter is a Python-based tool that ensures your code adheres to best practices and style guidelines. It integrates `black` for code formatting, `isort` for import sorting, and `flake8` for linting into a single, easy-to-use script. This tool helps maintain a clean, consistent, and PEP 8-compliant codebase.

## Features

- **Code Formatting:** Formats Python code according to PEP 8 standards using `black`.
- **Import Sorting:** Organizes imports alphabetically and categorizes them with `isort`.
- **Code Linting:** Identifies potential issues like syntax errors and unused imports with `flake8`.
- **Pre-commit Hook:** Enforces formatting and linting checks before commits to ensure code quality.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- `pip` (Python package installer)

### Installation

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/CodewithDili/auto-code-formatter.git
   cd auto-code-formatter
Install Dependencies:

pip install -r requirements.txt
Install Pre-commit Hooks:

pre-commit install
Usage
To format your code, run the following command:
python formatter.py
This will format the code using black, sort imports with isort, and lint the code with flake8.

Running Tests
To ensure everything is working correctly, you can run the tests:
pytest
Contributing
Feel free to submit issues or pull requests if you have suggestions or improvements.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any questions or support, reach out to dilichi20044@gmail.com.

Feel free to adjust any details or sections according to your project's needs!






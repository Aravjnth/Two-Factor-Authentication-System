
Two-Factor Authentication System

## Overview

The Two-Factor Authentication (2FA) System is a Python-based application designed to enhance security by requiring users to provide two forms of identification before accessing a system. This project implements a 2FA system using a combination of factors, such as a password and a time-based one-time password (TOTP) generated via a mobile app or SMS.

## Features

- Implements two-factor authentication using TOTP.
- Supports QR code scanning for easy setup.
- Securely stores user secrets (keys) for TOTP generation.
- Provides a command-line interface (CLI) for setup and administration.
- Logs authentication attempts and outcomes for auditing purposes.

## Requirements

- Python 3.x
- `pyotp` library for TOTP generation
- `flask` library for web interface (optional)

## Installation

1. Clone the repository:
    ```bash
    https://github.com/Aravjnth/Two-Factor-Authentication-System.git
    cd two-factor-authentication
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Command Line Interface (CLI)

1. Set up a user for 2FA:
    ```bash
    python manage.py setup_user --username <username>
    ```

2. Generate a QR code for user setup:
    ```bash
    python manage.py generate_qrcode --username <username>
    ```

3. Verify a TOTP code:
    ```bash
    python manage.py verify_totp --username <username> --code <totp-code>
    ```

### Web Interface (Optional)

1. Start the Flask development server for web interface:
    ```bash
    python app.py
    ```

2. Access the web interface in a browser at `http://localhost:5000`.

## Configuration

- Modify `config.py` to set up database connections, secret key for Flask app (if used), etc.

## Legal Disclaimer

This Two-Factor Authentication System is intended for educational and demonstration purposes. Implementing 2FA in production environments should consider additional security measures, best practices, and compliance requirements. Use this tool responsibly and with consent.

## Contributing

Contributions to this project are welcome! Fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, please contact me at www.linkedin.com/in/aravinth-aj

# Reverse IP Lookup Tool

## Overview

This Python script performs a reverse IP lookup, providing valuable information such as hostname, ISP (Internet Service Provider), Reverse DNS details, and Country information. It leverages both the `socket` module for basic reverse lookup and the "ipinfo.io" API for additional data.

## Features

- **Reverse IP Lookup:** Get the associated hostname for a given IP address.
- **Additional Information:** Retrieve ISP, Reverse DNS, and Country details.
- **Error Handling:** Gracefully handles errors for a smooth user experience.

## Prerequisites

- Python 3.x
- Required Python libraries: `requests`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/reverse-ip-lookup.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Navigate to the project directory:

    ```bash
    cd reverse-ip-lookup
    ```

2. Run the script:

    ```bash
    python reverse_ip_lookup.py
    ```

3. Enter the IP address when prompted.

## Example

```bash
Enter an IP address: 8.8.8.8

## Acknowledgments
This script uses the "ipinfo.io" API for additional IP information.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

Make sure to replace placeholders like Amin Mousavi with your actual GitHub username and include a `LICENSE.md` file if you have chosen a specific license for your project.

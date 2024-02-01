
# Python IP Check

[![License: Apache](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![GitHub](https://img.shields.io/badge/GitHub-kerkpower%2Fpython__ip__check-brightgreen)](https://github.com/kerkpower/python_ip_check)

**python_ip_check** is a simple Python module for checking the validity of IP addresses. It provides a function to determine whether an IP address is valid or not.

## Installation

You can install the package using pip:

```bash
pip install git+https://github.com/Kerkpower/python_ip_check.git
```

## Usage

Here is an example of how to use the `is_valid_ip` function from the `ip_check` module:

```python
from ip_check import is_valid_ip

ip_address = "192.168.1.1"

if is_valid_ip(ip_address):
    print(f"The IP {ip_address} is valid.")
else:
    print(f"The IP {ip_address} is not valid.")
```

## Contributing

If you find issues or have suggestions for improvements, feel free to open an issue or submit a pull request on [GitHub](https://github.com/kerkpower/python_ip_check).

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

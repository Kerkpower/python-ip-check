def is_valid_ip(ip):
    """Check if the provided IP address is valid."""
    octets = ip.split(".")

    if len(octets) != 4 or not all(octet.isdigit() and 0 <= int(octet) <= 255 for octet in octets) or any(
            int(octet) > 255 for octet in octets):
        return False

    return True

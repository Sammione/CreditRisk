BASE_URL = "Baseurllink"
RECORDS_ENDPOINT = "Endpoint"

def get_auth_headers(token: str):
    """
    Dynamically generate request headers with the user's Bearer token.

    Args:
        token (str): User's authentication token from the frontend

    Returns:
        dict: Authorization header dictionary
    """
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"

    }

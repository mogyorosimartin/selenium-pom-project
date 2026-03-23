import uuid

SEARCH_TERMS = {
    "valid": "T-Shirt",
    "invalid": "xkqzwpqzwp"
}

CONTACT_FORM = {
    "name": "Test User",
    "email": "testuser@example.com",
    "subject": "Test Subject",
    "message": "This is an automated test message."
}

EXISTING_EMAIL = "dawak18615@onbap.com"  

REGISTER_USER = {
    "name": "Test User",
    "email": f"test_{uuid.uuid4().hex[:8]}@test.com",
    "title": 1,
    "password": "Test1234!",
    "day": "1",
    "month": "January",
    "year": "1995",
    "newsletter": True,
    "optin": True,
    "first_name": "Test",
    "last_name": "User",
    "address1": "123 Test Street",
    "address2": "",
    "country": "United States",
    "state": "California",
    "city": "Los Angeles",
    "zipcode": "90001",
    "mobile_number": "1234567890"
}
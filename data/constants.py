import os

class Constants:
    try:
        first_name = os.getenv('FIRST_NAME')
        last_name = os.getenv('LAST_NAME')
        email = os.getenv('EMAIL')
        phone = os.getenv('PHONE')
    except KeyError:
        print("Test constant not added to .env")
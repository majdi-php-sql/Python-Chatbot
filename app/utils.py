import re  # I imported the regular expression module for text processing

def extract_product_name(question):
    """
    I wrote this function to extract the product name from the user's question.
    """
    # Placeholder example: You should implement your own logic or use NLP techniques
    match = re.search(r"(\b[\w\s]+\b)", question)  # I used regex to find potential product names
    return match.group(1) if match else None  # I returned the found product name or None if not found

def extract_query_type(question):
    """
    I wrote this function to determine the type of information the user is asking about.
    """
    if "price" in question.lower():  # I checked if the question is about price
        return "price"
    elif "availability" in question.lower() or "stock" in question.lower():  # I checked if the question is about availability
        return "availability"
    elif "company" in question.lower():  # I checked if the question is about the company
        return "company"
    elif "country" in question.lower():  # I checked if the question is about the country
        return "country"
    else:
        return None  # I returned None if the question type is not recognized

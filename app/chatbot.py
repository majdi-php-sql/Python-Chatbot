# I imported necessary modules from the app package
from .database import fetch_product_info  # I imported the function to fetch product info from the database
from .nlp_model import get_nlp_model  # I imported the function to get the NLP model
from .utils import extract_product_name, extract_query_type  # I imported utility functions for extracting product names and query types

def get_answer(question):
    """
    I wrote this function to process user questions and return relevant product information.
    """

    # Initialize the NLP model
    nlp_model = get_nlp_model()  # I initialized the NLP model to understand and process the question

    # Extract query type and product name
    query_type = extract_query_type(question)  # I extracted the type of information the user wants (price, availability, etc.)
    product_name = extract_product_name(question)  # I extracted the product name from the user's question

    if not product_name:  # I checked if the product name was found
        return "Sorry, I couldn't find the product you're asking about. Could you please provide more details?"

    # Fetch product information from the database
    product_info = fetch_product_info(product_name)  # I fetched the product details from the database

    if not product_info:  # I checked if the product was found in the database
        return "Product not found in the database."

    # Respond based on the type of query
    if query_type == "price":  # I checked if the user asked for the product's price
        return f"The price of {product_info['name']} is ${product_info['price_per_unit']:.2f} per unit."  # I formatted the response to include the price
    
    elif query_type == "availability":  # I checked if the user asked for the product's availability
        return f"{product_info['name']} has {product_info['quantity']} units in stock."  # I formatted the response to include the quantity available
    
    elif query_type == "company":  # I checked if the user asked for the product's company
        return f"The company producing {product_info['name']} is {product_info['company']}."  # I formatted the response to include the company name
    
    elif query_type == "country":  # I checked if the user asked for the product's country of origin
        return f"{product_info['name']} is made in {product_info['country']}."  # I formatted the response to include the country of origin

    else:  # I handled unrecognized queries
        return "I’m not sure how to answer that question. Please ask about the price, availability, company, or country."

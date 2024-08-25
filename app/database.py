import psycopg2  # I imported psycopg2 to interact with the PostgreSQL database

def get_db_connection():
    """
    I wrote this function to establish a connection to the PostgreSQL database.
    """
    conn = psycopg2.connect(
        dbname="your_database",  # I specified the database name to connect to
        user="your_username",    # I specified the username for authentication
        password="your_password",# I specified the password for authentication
        host="your_host",        # I specified the host where the database server is running
        port="your_port"         # I specified the port number to connect to
    )
    return conn  # I returned the established connection object

def fetch_product_info(product_name):
    """
    I wrote this function to fetch product information based on the product name.
    """
    conn = get_db_connection()  # I established a connection to the database
    cur = conn.cursor()  # I created a cursor object to execute SQL queries
    
    # I executed a query to fetch the product details from the product table
    cur.execute("""
        SELECT id, name, category, price_per_unit, quantity, company, country 
        FROM product 
        WHERE name = %s
        """, (product_name,))
    
    product_info = cur.fetchone()  # I fetched the first result from the query
    cur.close()  # I closed the cursor after the query was executed
    conn.close()  # I closed the connection to the database

    if product_info:  # I checked if product information was found
        return {
            "id": product_info[0],
            "name": product_info[1],
            "category": product_info[2],
            "price_per_unit": product_info[3],
            "quantity": product_info[4],
            "company": product_info[5],
            "country": product_info[6]
        }  # I returned the product information as a dictionary

    return None  # I returned None if no product information was found

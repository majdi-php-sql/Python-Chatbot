
# Product Information Chatbot

The **Product Information Chatbot** is a Python-based application designed to interact with a PostgreSQL database to provide real-time information about products stored in the database. The chatbot can answer questions related to product availability, price, company, and country of origin.

## Features

- **Natural Language Processing (NLP):** Uses a pre-trained model from HuggingFace's Transformers library to understand and process user queries.
- **PostgreSQL Integration:** Connects to a PostgreSQL database to fetch and display product information.
- **Real-Time Interaction:** Provides immediate responses to user queries about products.
- **Modular Codebase:** Easy to extend and maintain with a clean directory structure.

## Project Directory Structure

```
chatbot_project/
├── app/
│   ├── __init__.py          # Marks the directory as a package
│   ├── chatbot.py           # Core chatbot logic for handling user queries
│   ├── database.py          # Database connection and query functions
│   ├── nlp_model.py         # NLP model setup using transformers
│   └── utils.py             # Utility functions for processing user input
├── requirements.txt         # Python dependencies
└── main.py                  # Entry point to run the chatbot
```

## Setup and Installation

### Prerequisites

- Python 3.7 or later
- PostgreSQL database
- Internet connection for downloading pre-trained NLP models

### Step-by-Step Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/chatbot_project.git
   cd chatbot_project
   ```

2. **Install Python Dependencies:**

   Install the required Python packages by running:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure PostgreSQL Database:**

   Ensure your PostgreSQL database is set up correctly with the `product` table. The table should have the following structure:

   ```sql
   CREATE TABLE product (
       id SERIAL PRIMARY KEY,
       name VARCHAR(100) NOT NULL,
       category VARCHAR(100) NOT NULL,
       price_per_unit NUMERIC(15, 2) NOT NULL,
       quantity INTEGER NOT NULL,
       company VARCHAR(100) NOT NULL,
       country VARCHAR(100) NOT NULL
   );
   ```

   Update the `database.py` file with your actual PostgreSQL connection details:

   ```python
   conn = psycopg2.connect(
       dbname="your_database",
       user="your_username",
       password="your_password",
       host="your_host",
       port="your_port"
   )
   ```

4. **Run the Chatbot:**

   Start the chatbot by running the following command:

   ```bash
   python main.py
   ```

5. **Interact with the Chatbot:**

   After running the `main.py` file, you'll be prompted to ask questions. Here are some examples of questions you can ask:

   - "What is the price of [product name]?"
   - "Is [product name] available?"
   - "Who is the company producing [product name]?"
   - "Where is [product name] made?"

## How It Works

1. **User Input:**
   The user types a question into the console.
   
2. **NLP Processing:**
   The chatbot uses an NLP model to determine the intent of the query and extract relevant entities (such as the product name and query type).

3. **Database Query:**
   Based on the extracted information, the chatbot queries the PostgreSQL database to retrieve the necessary product information.

4. **Response Generation:**
   The chatbot formats the retrieved information into a human-readable response and displays it to the user.

## Code Overview

- **`chatbot.py`:** Contains the core logic to interpret user input and generate responses.
- **`database.py`:** Handles database connections and queries to fetch product information.
- **`nlp_model.py`:** Initializes the NLP model used for understanding user queries.
- **`utils.py`:** Utility functions for processing and extracting information from user input.
- **`main.py`:** Entry point to start the chatbot and handle user interactions.

## Customization and Extensibility

- **Adding More Product Attributes:**
  Modify the `product` table and `fetch_product_info` function in `database.py` to include new attributes.
- **Enhancing NLP Capabilities:**
  Improve the `extract_product_name` and `extract_query_type` functions in `utils.py` to handle more complex queries.
- **Supporting Additional Databases:**
  Extend `database.py` to support other databases like MySQL or SQLite.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue to help improve this project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Acknowledgments

- [HuggingFace Transformers](https://huggingface.co/transformers/) for the pre-trained NLP models.
- PostgreSQL for the robust and reliable database management system.


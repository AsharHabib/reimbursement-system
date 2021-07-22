# Import psycogp2 and os
import psycopg2, os

# Grab environment variables
db_url = os.environ['DB_URL']
db_username = os.environ['DB_USERNAME']
db_password = os.environ['DB_PASSWORD']
db_name = os.environ['DB_NAME']

test_db_url = os.environ['TEST_URL']
test_db_username = os.environ['TEST_USERNAME']
test_db_password = os.environ['TEST_PASSWORD']
test_db_name = os.environ['TEST_NAME']

# Function to return a connection to Database, productionDB to differentiate with
# testing DB done for testing the DAOs and services
def get_connection(productionDB=True):
    if productionDB:
        return psycopg2.connect(
            host=db_url,
            port=5432,
            user=db_username,
            password=db_password,
            database=db_name
        )
    else:
        return psycopg2.connect(
            host=test_db_url,
            port=5432,
            user=test_db_username,
            password=test_db_password,
            database=test_db_name
        )
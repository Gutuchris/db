# import psycopg2
# from psycopg2 import sql, errors

# def connect():
#     """Connect to the PostgreSQL database server."""
#     conn = None
#     try:
#         conn = psycopg2.connect(
#             dbname="sales_system",
#             user="postgres",
#             password="Genius1584.",
#             host="localhost",
          
#         )
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     return conn

# def get_data(conn, customer, product, sale):
#     """Add customer, product, and sale data."""
#     get_customer(conn, *customer)
#     get_product(conn, *product)
#     get_sale(conn, *sale)

# def get_customer(conn, customer_id, customer_name, customer_email):
#     """Insert a new customer into the customers table."""
#     try:
#         with conn.cursor() as cur:
#             cur.execute(
#                 """
#                 INSERT INTO customers (customer_id, customer_name, customer_email)
#                 VALUES (%s, %s, %s)
#                 """,
#                 (customer_id, customer_name, customer_email)
#             )
#         conn.commit()
#     except errors.UniqueViolation:
#         print(f"Customer with customer_id={customer_id} already exists.")
#         conn.rollback()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#         conn.rollback()

# def get_product(conn, product_id, product_name, product_price):
#     """Insert a new product into the products table."""
#     try:
#         with conn.cursor() as cur:
#             cur.execute(
#                 """
#                 INSERT INTO products (product_id, product_name, product_price)
#                 VALUES (%s, %s, %s)
#                 """,
#                 (product_id, product_name, product_price)
#             )
#         conn.commit()
#     except errors.UniqueViolation:
#         print(f"Product with product_id={product_id} already exists.")
#         conn.rollback()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#         conn.rollback()

# def get_sale(conn, sale_id, customer_id, product_id, sale_date, quantity):
#     """Insert a new sale into the sales table."""
#     try:
#         with conn.cursor() as cur:
#             cur.execute(
#                 """
#                 INSERT INTO sales (sale_id, customer_id, product_id, sale_date, quantity)
#                 VALUES (%s, %s, %s, %s, %s)
#                 """,
#                 (sale_id, customer_id, product_id, sale_date, quantity)
#             )
#         conn.commit()
#     except errors.UniqueViolation:
#         print(f"Sale with sale_id={sale_id} already exists.")
#         conn.rollback()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#         conn.rollback()

# def select_customer(conn, customer_id):
#     """Select customer data by customer_id."""
#     try:
#         with conn.cursor() as cur:
#             cur.execute(
#                 """
#                 SELECT customer_id, customer_name, customer_email
#                 FROM customers
#                 WHERE customer_id = %s
#                 """,
#                 (customer_id,)
#             )
#             customer = cur.fetchone()
#             return customer
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)

# def select_product(conn, product_id):
#     """Select product data by product_id."""
#     try:
#         with conn.cursor() as cur:
#             cur.execute(
#                 """
#                 SELECT product_id, product_name, product_price
#                 FROM products
#                 WHERE product_id = %s
#                 """,
#                 (product_id,)
#             )
#             product = cur.fetchone()
#             return product
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)

# def select_sale(conn, sale_id):
#     """Select sale data by sale_id."""
#     try:
#         with conn.cursor() as cur:
#             cur.execute(
#                 """
#                 SELECT sale_id, customer_id, product_id, sale_date, quantity
#                 FROM sales
#                 WHERE sale_id = %s
#                 """,
#                 (sale_id,)
#             )
#             sale = cur.fetchone()
#             return sale
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)

# if __name__ == "__main__":
#     conn = connect()
#     if conn is not None:
#         try:
#             # Example of inserting data
#             customer_data = (1, 'John Doe', 'john.doe@example.com')
#             product_data = (1, 'Widget', 19.99)
#             sale_data = (1, 1, 1, '2024-06-13', 2)

#             get_data(conn, customer_data, product_data, sale_data)

#             # Example of selecting data
#             customer = select_customer(conn, 1)
#             print("Selected Customer:", customer)

#             product = select_product(conn, 1)
#             print("Selected Product:", product)

#             sale = select_sale(conn, 1)
#             print("Selected Sale:", sale)
#         finally:
#             conn.close()



import psycopg2
from psycopg2 import sql, errors

def connect():
    """Connect to the PostgreSQL database server."""
    try:
        conn = psycopg2.connect(
            dbname="sales_system",
            user="postgres",
            password="Genius1584.",
            host="localhost",
        )
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error connecting to database: {error}")
        return None

def get_all_products():
    """Fetch all products from the products table."""
    conn = connect()
    products = []
    if conn is not None:
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT product_id, product_name, product_price FROM products")
                products = cur.fetchall()
                print(f"Fetched {len(products)} products.")  # Debug print
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error fetching products: {error}")
        finally:
            conn.close()
    return products

def get_all_sales():
    """Fetch all sales from the sales table."""
    conn = connect()
    sales = []
    if conn is not None:
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT sale_id, customer_id, product_id, sale_date, quantity FROM sales")
                sales = cur.fetchall()
                print(f"Fetched {len(sales)} sales.")  # Debug print
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error fetching sales: {error}")
        finally:
            conn.close()
    return sales

def insert_product(product_name, product_price):
    """Inserts a new product into the products table."""
    conn = connect()
    if conn is not None:
        try:
            with conn.cursor() as cur:
                # SQL statement to insert a new product
                insert_query = sql.SQL(
                    "INSERT INTO products (product_id,product_name, product_price) VALUES (%s, %s,%s)"
                )
                # Execute the SQL statement
                cur.execute(insert_query, (product_name, product_price))
                # Commit the transaction
                conn.commit()
                print("Product inserted successfully")
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error inserting product: {error}")
        finally:
            conn.close()
# Example usage
#new_product = ('Beef', 500)
# )insert_product (61,'Beef', 500#(new_product)
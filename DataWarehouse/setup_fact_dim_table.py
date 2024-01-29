import psycopg2

# Establishing the connection
conn = psycopg2.connect(
    database="databasename",
    user="username",
    password="password",
    host="hostname",
    port="5432",
)

cursor = conn.cursor()

# fact_transaction stuff
cursor.execute("DROP TABLE IF EXISTS fact_transaction")
create_fact_transaction_sql = """CREATE TABLE fact_transaction(
	webid SERIAL PRIMARY KEY,
    name_key INTEGER,
    mile INTEGER,
    color_key INTEGER,
    gear_key INTEGER,
    web_key INTEGER,
    status_key INTEGER,
    cost INTEGER,
    date_key DATE
)"""
cursor.execute(create_fact_transaction_sql)
print("Table fact_transaction created successfully........")

# staging_transaction stuff
cursor.execute("DROP TABLE IF EXISTS staging_transaction")
create_staging_transaction_sql = """CREATE TABLE staging_transaction (
    webid SERIAL PRIMARY KEY,
    name VARCHAR(255),
    mile INTEGER,
    color VARCHAR(50),
    gear VARCHAR(20),
    web VARCHAR(100),
    status VARCHAR(20),
    cost INTEGER,
    date DATE
)
"""
cursor.execute(create_staging_transaction_sql)
print("Table staging_transaction created successfully........")

# dim_name stuff
cursor.execute("DROP TABLE IF EXISTS dim_name")
create_dim_name_transaction_sql = """CREATE TABLE dim_name(
	index SERIAL PRIMARY KEY,
    name VARCHAR(255),
)"""
cursor.execute(create_dim_name_transaction_sql)
print("Table dim_name created successfully........")

# color stuff
cursor.execute("DROP TABLE IF EXISTS dim_color")
create_dim_color_transaction_sql = """CREATE TABLE dim_color(
	index SERIAL PRIMARY KEY,
    color VARCHAR(255),
)"""
cursor.execute(create_dim_color_transaction_sql)
print("Table dim_color created successfully........")

# gear stuff
cursor.execute("DROP TABLE IF EXISTS dim_gear")
create_dim_gear_transaction_sql = """CREATE TABLE dim_gear(
	index SERIAL PRIMARY KEY,
    gear_type VARCHAR(255),
)"""
cursor.execute(create_dim_gear_transaction_sql)
print("Table dim_gear created successfully........")

# web stuff
cursor.execute("DROP TABLE IF EXISTS dim_web")
create_dim_web_transaction_sql = """CREATE TABLE dim_web(
	index SERIAL PRIMARY KEY,
    web_name VARCHAR(255),
)"""
cursor.execute(create_dim_web_transaction_sql)
print("Table dim_web created successfully........")

# date stuff
cursor.execute("DROP TABLE IF EXISTS dim_date")
create_dim_date_transaction_sql = """CREATE TABLE dim_date(
	index SERIAL PRIMARY KEY,
    date VARCHAR(255),
)"""
cursor.execute(create_dim_date_transaction_sql)
print("Table dim_date created successfully........")

# Closing the connection
conn.commit()
conn.close()

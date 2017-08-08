import sqlalchemy.engine

def get_database_connection():
    params = {
        "username": "take2_bespoke",
        "password": "t4k32_b3sp0k3",
        "db_url": "hq-mysql02-nightly.stagealot.com",
        "db_port": 3306,
        "db_name": "take2"
    }

    engine = sqlalchemy.engine.create_engine(
        "mysql+mysqldb://%(username)s:%(password)s@%(db_url)s:%(db_port)s/%(db_name)s" % params
    )
    connection = engine.connect()
    return connection


def get_tables():
    query = "SELECT table_name FROM information_schema.tables WHERE table_schema = %(db_name)s"
    connection = get_database_connection()
    result_set = connection.execute(query, {"db_name": "take2"})
    tables = result_set.fetchall()
    return [table[0] for table in tables]

def get_table_columns(table_name):
    tables = get_tables()
    if table_name not in tables:
        raise ValueError("Table not found")
    
    query = """
        SELECT column_name
          FROM information_schema.columns
         WHERE table_name = %(table_name)s
           AND table_schema = %(db_name)s
    """
    connection = get_database_connection()
    result_set = connection.execute(query, {'db_name': 'take2', 'table_name': table_name})
    columns = result_set.fetchall()
    return [column[0] for column in columns]
import psycopg2
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',  # формат строки
    handlers=[
        logging.FileHandler("down_hosts.log"),    # писать в файл
    ])
logger = logging.getLogger(__name__)
def connect_to_db():
    try:
        connection = psycopg2.connect(
            dbname="app_db",
            user="user",
            password="password",
            host="192.168.1.130",
            port="5432"
        )
        logger.info("Connection to database successful")

        return connection
    except Exception as e:
        logger.error(f"An error occurred while connecting to the database: {e}")
        return None
def sql_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except Exception as e:
        logger.error(f"An error occurred while executing the SQL query: {e}")
        return None
    finally:
        cursor.close()




def main():
    connection = connect_to_db()
    if connection:
        query = "SELECT * FROM hosts WHERE status = 'down';"
        results = sql_query(connection, query)
        if results is not None:
            for row in results:
                logger.info(row)
        connection.close()

if __name__ == "__main__":    main()
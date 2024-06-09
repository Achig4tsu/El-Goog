import mysql.connector as MC
import logging
from datetime import datetime, timedelta

class MySQLDatabase:
    def __init__(self, host, user, password, database):
        self.connection = MC.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.db_logger = logging.getLogger("DatabaseLogger")
        self.db_logger.setLevel(logging.INFO)
        handler = logging.FileHandler('/app/Logs/DB/mysql_database.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.db_logger.addHandler(handler)

    def get_url_info(self, url):
        try:
            cursor = self.connection.cursor()
            query = "SELECT title, description, banned, timestamp FROM urls WHERE url = %s"
            cursor.execute(query, (url,))
            result = cursor.fetchone()
            cursor.close()
            if result:
                title, description, banned, timestamp = result
                return title, description, banned, timestamp
            return None
        except MC.Error as e:
            self.db_logger.error(f"Error fetching URL info: {e}")
            return None

    def insert_url_info(self, url, title, description):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO urls (url, title, description) VALUES (%s, %s, %s)"
            cursor.execute(query, (url, title, description))
            self.connection.commit()
            cursor.close()
        except MC.Error as e:
            self.db_logger.error(f"Error inserting URL info: {e}")

    def update_url_info(self, url, title, description):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE urls SET title = %s, description = %s WHERE url = %s"
            cursor.execute(query, (title, description, url))
            self.connection.commit()
            cursor.close()
        except MC.Error as e:
            self.db_logger.error(f"Error updating URL info: {e}")

    def url_needs_update(self, last_updated):
        if last_updated is None:
            return True
        return (datetime.now() - last_updated) > timedelta(days=1)

    def create_group_if_not_exists(self, group):
        try:
            cursor = self.connection.cursor()
            query = "INSERT IGNORE INTO groups (name) VALUES (%s)"
            cursor.execute(query, (group,))
            self.connection.commit()
            cursor.close()
        except MC.Error as e:
            self.db_logger.error(f"Error creating group: {e}")

    def add_url_to_group(self, url, group):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE groups SET members = JSON_ARRAY_APPEND(members, '$', %s) WHERE name = %s"
            cursor.execute(query, (url, group))
            if cursor.rowcount == 0:  # Group does not exist, create it
                query = "INSERT INTO groups (name, members) VALUES (%s, JSON_ARRAY(%s))"
                cursor.execute(query, (group, url))
            self.connection.commit()
            cursor.close()
        except MC.Error as e:
            self.db_logger.error(f"Error adding URL to group: {e}")

    def add_keyword_to_table(self, keyword):
        try:
            table_name = f"mot_{keyword[0].lower()}"
            cursor = self.connection.cursor()
            query = f"CREATE TABLE IF NOT EXISTS {table_name} (mot VARCHAR(100) PRIMARY KEY, id_urls JSON)"
            cursor.execute(query)
            self.connection.commit()
            query = f"INSERT INTO {table_name} (mot, id_urls) VALUES (%s, JSON_ARRAY()) ON DUPLICATE KEY UPDATE mot = mot"
            cursor.execute(query, (keyword,))
            query = f"UPDATE {table_name} SET id_urls = JSON_ARRAY_APPEND(id_urls, '$', %s) WHERE mot = %s"
            cursor.execute(query, (keyword, keyword))
            self.connection.commit()
            cursor.close()
        except MC.Error as e:
            self.db_logger.error(f"Error adding keyword to table: {e}")

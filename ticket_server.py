import bisect
import os
from datetime import datetime

import mysql.connector
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

ticket_server = Flask(__name__)

@ticket_server.route("/generate_key", methods=["GET"])
def generate_key():
    random_generator = random_key_generator()
    random_generator.get_id_from_db()
    return {"short_url":random_generator.random_short_key}

class random_key_generator():
    def __init__(self):
        self.random_id = None
        self.random_short_key = None
        self.random_int = None
        self.uniqueRandomSet = os.getenv("uniqueHashCode")
        self.shards = [{"host":'localhost', "user":'mysql', "password":'strong_password', "port":3306, "database":"TINYURL"}, {"host":'localhost', "user":'mysql2', "password":'strong_password', "port":3307, "database":"TINYURL"}, {"host":'localhost', "user":'mysql3', "password":'strong_password', "port":3308, "database":"TINYURL"}]
        self.db_string = None
    
    def get_id_from_db(self):
        query = 'select id, counter from ranges where counter<end order by rand() limit 1'
        self.get_db_string_based_on_consistent_hashing()
        id,counter = self.get_data_from_db(query)[0]
        self.random_id = id
        self.random_int = counter
        self.generate_short_key()

    
    def get_db_string_based_on_consistent_hashing(self):
        slot_id = int(datetime.now().timestamp()*1000000)%(len(self.shards))
        self.db_string = self.shards[slot_id]
    
    def generate_short_key(self):
        unique_base = str(self.uniqueRandomSet)
        short_url = ""
        length = len(unique_base)
        counter = int(self.random_int)
        print(unique_base,length,counter)
        while counter > length:
            rem = counter % length
            counter = counter // length
            short_url = short_url+unique_base[rem]
        short_url = short_url + unique_base[counter]
        self.random_short_key = short_url[::-1]
        self.update_counter() 
    
    def update_counter(self):
        id = self.random_id
        counter = self.random_int
        query = f'''update ranges set counter = {counter+1} where id = {id}'''
        self.get_data_from_db(query)
    
    def get_data_from_db(self,query):
        db_config = self.db_string
        mydb = mysql.connector.connect(
        host=db_config["host"],
        user=db_config["user"],
        password=db_config["password"],
        port=db_config["port"],
        database=db_config["database"]
    )
        mycursor = mydb.cursor()
        mycursor.execute(query)
        data = mycursor.fetchall()
        mydb.commit()
        mycursor.close()
        mydb.close()
        return data        
        


if __name__ == '__main__':
    ticket_server.run(port=5000)
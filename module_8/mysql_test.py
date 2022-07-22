import mysql.connector 
from  mysql.connector import errorcode 

config = { 
    "user" : "pysports_user",
    "password":"MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings" : True
}


try:
    db = mysql.connector.connect(**config)

    print("\n Datababase user {} connected to MySQL on host {} with database {}".format(config["user"],config["host"], config["database"]))
    
    input("\n\n Press any key to continue....")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified username or password are invalid")

    else: 
        print(err)
finally: 
    db.close()
    
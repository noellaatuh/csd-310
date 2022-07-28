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
    print("-- DISPLAYING PLAYER RECORDS  --")

 
    cursor = db.cursor() 
    cursor.execute("SELECT player_id, first_name, last_name,team_name  from player inner join team on player.team_id = team.team_id")

    playerteams = cursor.fetchall()

    for playerteam in playerteams: 
        print("Player ID: {}".format(playerteam[0]))
        print("First Name: {}".format(playerteam[1]))
        print("Last Name: {}".format(playerteam[2]))
        print("Team Name: {}".format(playerteam[3]))
        print("\n")

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
    

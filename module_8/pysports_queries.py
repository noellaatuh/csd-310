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
     
    print("-- Displaying Team Records --")

 
    cursor = db.cursor() 
    cursor.execute("SELECT team_id, team_name, mascot from team")

    teams = cursor.fetchall()

    for team in teams: 
        print("Team ID: {}".format(team[0]))
        print("Team Name: {}".format(team[1]))
        print("Mascot: {}".format(team[2]))
        print("\n")
    print("-- Displaying Player Records --")

 
    pcursor = db.cursor() 
    pcursor.execute("SELECT player_id, first_name, last_name, team_id from player")

    players = pcursor.fetchall()

    for player in players: 
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))  
        print("Last Name: {}".format(player[2]))
        print("Team ID: {}".format(player[3]))
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
    




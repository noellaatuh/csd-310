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
    
    insertquery = "Insert into player(first_name, last_name, team_id) values ('Smeagol','Shire Folk',1)"

    cursor = db.cursor()
    cursor.execute(insertquery)
    db.commit()
    cursor.close()


    print("-- DISPLAYING PLAYERS AFTER INSERT  --")

 
    cursor = db.cursor() 
    cursor.execute("SELECT player_id, first_name, last_name,team_name  from player inner join team on player.team_id = team.team_id")

    playerteams = cursor.fetchall()

    for playerteam in playerteams: 
        print("Player ID: {}".format(playerteam[0]))
        print("First Name: {}".format(playerteam[1]))
        print("Last Name: {}".format(playerteam[2]))
        print("Team Name: {}".format(playerteam[3]))
        print("\n")

    
    updatequery = "update player set team_id = 2, first_name = 'Gollum', last_name= 'Ring Stealer' where first_name= 'Smeagol' and team_id = 1"

    cursor = db.cursor()
    cursor.execute(updatequery)
    db.commit()
    cursor.close()

    
    print("-- DISPLAYING PLAYERS AFTER UPDATE  --")

 
    cursor = db.cursor() 
    cursor.execute("SELECT player_id, first_name, last_name,team_name  from player inner join team on player.team_id = team.team_id")

    playerteams = cursor.fetchall()


    for playerteam in playerteams: 
        print("Player ID: {}".format(playerteam[0]))
        print("First Name: {}".format(playerteam[1]))
        print("Last Name: {}".format(playerteam[2]))
        print("Team Name: {}".format(playerteam[3]))
        print("\n")

    deletequery = "delete from player where first_name = 'Gollum' and last_name ='Ring Stealer'"


    cursor = db.cursor()
    cursor.execute(deletequery)
    db.commit()
    cursor.close()

    
    print("-- DISPLAYING PLAYERS AFTER DELETE  --")

 
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
    

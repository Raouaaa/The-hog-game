import sqlite3
from sqlite3 import Error
db_file = "hog.db"
conn = sqlite3.connect(db_file)
c = conn.cursor()

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e) 
    return None


def create_table(create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
 
def insert_users(name,email,pwd):
    c = conn.cursor()
    query = "INSERT INTO users(name,email,pwd) VALUES ('{}','{}','{}')".format(name, email, pwd)
    c.execute(query)
    conn.commit()

def insert_game(player1_id, player2_id,score0, score1, challengeID):
   c = conn.cursor()
   query = "INSERT INTO game (player1_id, player2_id,score0, score1, challengeID)\
   VALUES('{}','{}','{}','{}','{}')".format(player1_id, player2_id,score0, \
   score1, challengeID)
   c.execute(query)
   conn.commit()

def insert_challenges(player1_id, player2_id ,thestatus):
    c = conn.cursor()
    query = "INSERT INTO challenges (player1_id, player2_id,thestatus) VALUES \
    ('{}','{}','{}')".format(player1_id, player2_id ,thestatus)
    c.execute(query)
    conn.commit()

def update_mail_users(user_id,newemail):
    c = conn.cursor()
    query = "UPDATE users SET email = '{}' WHERE ID = '{}'".format(newemail, user_id)
    c.execute(query)

def update_pwd_users(user_id,new_pwd):
    c = conn.cursor()
    query = "UPDATE users SET pwd = '{}' WHERE ID = '{}'".format(new_pwd, user_id)
    c.execute(query)

def leaderboard(conn):
    c = conn.cursor()
    #sort the player and display them in a leaderboard from the heighest score /
    # to the lowest
    query = "SELECT id as id,SUM(score) as s FROM(SELECT player1_id as id, score0\
    as score FROM game UNION SELECT player2_id as id, score1 as score from game)\
    GROUP BY id ORDER BY s DESC;"
    c.execute(query)
    results = c.fetchall()
    

def update_challenges(IDchallenge, new_status):
    #c=conn.cursor()
    query = "UPDATE challenges SET thestatus = '{}' WHERE challengeID = '{}'".\
    format(new_status, IDchallenge)
    c.execute(query)
    conn.commit()

def update_score_player1(IDgame, newscore):
    query = "UPDATE game SET score0 = '{}' WHERE Id = '{}'".\
    format(newscore, IDgame)
    c.execute(query)
    conn.commit()

def update_score_player2(IDgame, newscore):
    query = "UPDATE game SET score1 = '{}' WHERE Id = '{}'".\
    format(newscore, IDgame)
    c.execute(query)
    conn.commit()


def main() :

    database = "hog.db"
    
    conn=create_connection(database)

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY ,
                                        name text NOT NULL,
                                        email text NOT NULL,
                                        pwd text NOT NULL
                                    ); """
 
    sql_create_challenges_table = """CREATE TABLE IF NOT EXISTS challenges (
                                    challengeID integer PRIMARY KEY,
                                    player1_id text NOT NULL,
                                    player2_id text NOT NULL,
                                    thestatus  text NOT NULL,
                                    FOREIGN KEY(player1_id) REFERENCES users(id),
                                    FOREIGN KEY(player2_id) REFERENCES users(id) 
                                );"""
 
    sql_create_game_table = """ CREATE TABLE IF NOT EXISTS game(
                                            gameID integer PRIMARY KEY,
                                            player1_id text NOT NULL,
                                            player2_id text NOT NULL,
                                            Challenge_id integer NOT NULL,
                                            score0 integer NOT NULL,
                                            score1 integer Not NULL,
                                            FOREIGN KEY(Challenge_id) REFERENCES challenges(challengeID)
                                            );"""


    if conn is not None:
        # create users table
        create_table(sql_create_users_table)
        # create challenges table
        create_table(sql_create_challenges_table)
        #create game table
        create_table(sql_create_game_table)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()


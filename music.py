import sqlite3 as lite
import sys

con = lite.connect('C:/Users/batsh/Documents/IS 211/week10database.db')

with con:

    cur = con.cursor()
    # cur.execute("CREATE TABLE artists(id, name)")
    # albums = cur.execute("SELECT * FROM albums")
    # cur.execute("CREATE TABLE albums(id, artist)")
    # cur.execute(""" DROP TABLE songs;""")
    # cur.execute(""" CREATE TABLE songs (
    #                                       id integer PRIMARY KEY,
    #                                         name text NOT NULL,
    #                                         album text,
    #                                         track_no integer,
    #                                         runtime integer
    #                                     ); """
    #             )

    # cur.execute(""" CREATE TABLE albums (
    #                                       id integer PRIMARY KEY,
    #                                         name text NOT NULL,
    #                                         artist integer
    #
    #                                      ); """)

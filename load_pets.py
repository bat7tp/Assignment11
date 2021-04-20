import sqlite3 as lite
import sys

connection = lite.connect('C:/Users/batsh/Documents/IS 211/pets.db')

with connection:

    db_input = connection.cursor()

    # db_input.execute("""CREATE TABLE person (
    # id INTEGER PRIMARY KEY,
    # first_name TEXT,
    # last_name TEXT,
    # age INTEGER
    # );""")
    #
    # db_input.execute("""CREATE TABLE pet (
    # id INTEGER PRIMARY KEY,
    # name TEXT,
    # breed TEXT,
    # age INTEGER,
    # dead INTEGER
    # );""")
    #
    # db_input.execute("""CREATE TABLE person_pet (
    # person_id INTEGER,
    # pet_id INTEGER
    # );""")


# def insertPersons(person_recordList):
#     try:
#         sqlite_insert_query = """INSERT INTO person
#                           (id, first_name, last_nameTEXT, age)
#                           VALUES (?, ?, ?, ?);"""
#
#         db_input.executemany(sqlite_insert_query, person_recordList)
#         connection.commit()
#         print("Total", db_input.rowcount, "Records inserted successfully into pets table")
#         connection.commit()
#         db_input.close()
#
#     except lite.Error as error:
#         print("Failed to insert multiple records into sqlite table", error)
#     finally:
#         if connection:
#             connection.close()
#             print("The SQLite connection is closed")
#
#
# persons_recordsToInsert = [(1, 'James', 'Smith', 41), (2, 'Diana', 'Greene', 23), (3, 'Sara', 'White', 27),
#                            (4, 'William', 'Gibson', 23)]
#
# insertPersons(persons_recordsToInsert)

def insertPet(pet_recordList):
    try:
        sqlite_insert_query = """INSERT INTO pet
                          (id, name, breed, age, dead) 
                          VALUES (?, ?, ?, ?, ?);"""

        db_input.executemany(sqlite_insert_query, pet_recordList)
        connection.commit()
        print("Total", db_input.rowcount, "Records inserted successfully into pets table")
        connection.commit()
        db_input.close()

    except lite.Error as error:
        print("Failed to insert multiple records into sqlite table", error)
    finally:
        if connection:
            connection.close()
            print("The SQLite connection is closed")


# pet_recordsToInsert = [(1, 'Rusty', 'Dolmation', 4, 1), (2, 'Bella', 'AlaskanMalamute', 3, 0), (3, 'Max', 'CockerSpaniel', 1, 0)
#                            , (4, 'Rocky', 'Beagle', 7, 0),
#                            (5, 'Rufus', 'CockerSpaniel', 1, 0), (6, 'Spot', 'Bloodhound', 2, 1)]
#
# insertPet(pet_recordsToInsert)

def insertPair(pair_recordList):
    try:
        sqlite_insert_query = """INSERT INTO person_pet
                          (person_id, pet_id)
                          VALUES (?, ?);"""

        db_input.executemany(sqlite_insert_query, pair_recordList)
        connection.commit()
        print("Total", db_input.rowcount, "Records inserted successfully into pets table")
        connection.commit()
        db_input.close()

    except lite.Error as error:
        print("Failed to insert multiple records into sqlite table", error)
    finally:
        if connection:
            connection.close()
            print("The SQLite connection is closed")


pair_recordsToInsert = [(1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (4, 6)]

insertPair(pair_recordsToInsert)





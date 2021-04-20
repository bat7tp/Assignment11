import sqlite3 as lite
import sys

def create_connection(file):

    conn = None
    try:
        conn = lite.connect(file)
    except Exception as e:
        print(e)

    return conn
#
#
# def associated_id_info(conn, id_input):
    # "SELECT * FROM person WHERE id=? , (id_input,)


def main():
    database = 'C:/Users/batsh/Documents/IS 211/pets.db'

    conn = create_connection(database)

    while True:
        id_input = input("Please enter the ID number: ")

        if int(id_input) == -1:
            print("The session is ending")
            conn.close()
            break

        print("The associated information with that ID is: ")
        # associated_id_info(conn, id_input)


        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM person INNER JOIN person_pet ON person.id = person_pet.person_id INNER JOIN pet ON person_pet.pet_id = pet.id WHERE person.id=? " , (id_input,))
            rows = cur.fetchall()

            if len(rows) == 0:
                print("Error: No ID exists")
                break

        except Exception as e:
             print(e)

        for row in rows:
            # print(row)
            last_name = row[2]
            first_name = row[1]
            print("NAME: " + first_name + " " + last_name)

            age = row[3]
            print("AGE: ", age)

            name = row[7]
            print("They have a dog named: " + name)
            breed = row[8]
            dog_age = row[9]
            print("It is a " + breed + " dog, who is", dog_age, "years old")


if __name__ == '__main__':
    main()
# b. Ask the user for a person’s ID number
# c. If that user exists:
# i. Print out data on the person (e.g. James Smith, 41 years old)
# ii. Print out all the data on that person’s pets (e.g., James Smith owned Rusty, a
# dalmatian, that was 4 years old)
# d. Otherwise print an error message
# e. Keep doing this until the user enters in a -1, which is an indication to exit the progra
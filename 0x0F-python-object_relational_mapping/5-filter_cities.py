#!/usr/bin/python3
# script that takes in the name of a state as an arg and lists cities

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name\
                FROM states\
                JOIN cities\
                ON states.id = cities.state_id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (sys.argv[4],))
    query = cur.fetchall()
    listofcities = []
    for row in query:
        listofcities.append(row[0])
    print(", ".join(listofcities))
    cur.close()
    db.close()

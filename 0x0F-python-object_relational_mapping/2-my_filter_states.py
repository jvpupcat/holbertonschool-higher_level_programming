#!/usr/bin/python3
"""script that pulls in argv4"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT  id, name\
                FROM states\
                WHERE name = '{:s}'\
                ORDER BY states.id ASC".format(sys.argv[4]))
    query = cur.fetchall()
    for row in query:
        if row[1] == sys.argv[4]:
            print(row)
    cur.close()
    db.close()

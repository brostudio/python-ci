import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='127.0.0.1', user='root', password="root", database="world")

    cursor = db.cursor()

    ## defining the Query
    query = "SELECT * FROM city"

    ## getting records from the table
    cursor.execute(query)

    ## fetching all records from the 'cursor' object
    records = cursor.fetchall()

    ## Showing the data
    for record in records:
        print(record)

    db.close()
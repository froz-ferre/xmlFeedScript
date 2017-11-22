import MySQLdb
import gc

def connection():
    conn = MySQLdb.connect( host = 'localhost',
                            user = 'root',
                            passwd = '322333',
                            )
    
    c = conn.cursor()
    return c, conn

def get_data_base():
    standart_schemas = ['information_schema', 'performance_schema', 'mysql', 'sys']
    db_list = []
    try:
        c, conn = connection()
        c.execute("SHOW DATABASES")

        # add filtered schemas in db_list
        row = c.fetchone()
        while row is not None:
            if row[0] not in standart_schemas:
                db_list.append(row)
            row = c.fetchone()

        # close DB connection
        c.close()
        conn.close()  
        gc.collect()

        # return schemas names array 
        for i in range(len(db_list)):
            db_list[i] = db_list[i][0]  
        return db_list

    except Exception as e:
        return None
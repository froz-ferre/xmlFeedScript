import MySQLdb
import gc

def connection(db = ''):
    '''   Connect to database (db = 'schema_name')   '''
    conn = MySQLdb.connect( host = 'localhost',
                            user = 'root',
                            passwd = '322333',
                            db = db
                            )
    
    c = conn.cursor()
    return c, conn

def get_schemas():
    standart_schemas = ['information_schema', 'performance_schema', 'mysql', 'sys']
    db_list = []
    try:
        c, conn = connection()
        c.execute("SHOW DATABASES")

        # add filtered schemas in db_list
        row = c.fetchone()
        while row is not None:
            if row[0] not in standart_schemas:
                db_list.append(row[0])
            row = c.fetchone()
            

        # close DB connection
        c.close()
        conn.close()  
        gc.collect()

        # return schemas names array 
       
        return db_list

    except Exception as e:
        return str(e)


def get_tables_info(db_name):
    table_info = [[], [], [], []]
    try:
        c, conn = connection(db_name)

        # show all tables in current DataBase
        c.execute("SHOW TABLES")
        row = c.fetchone()
        while row is not None:
            table_info[0].append(row[0])
            row = c.fetchone()

        
        # show amount rows in current DataBase.Table

        #for i in range(len(table_info[0])):
        for table in table_info[0]:
            c.execute("SELECT COUNT(*) FROM {0}".format(table))
            table_info[1].append(c.fetchone()[0])    # Count of rows
            c.execute("SELECT parsed_time FROM {0}".format(table))
            table_info[2].append(c.fetchone()[0])    # Parsed time
            table_info[3].append('/src/{}.xml'.format(table))


        # show parse times in current DataBase
        #c.execute("SHOW TABLES")

        # show links to XML in current DataBase

        # close DB connection
        c.close()
        conn.close()  
        gc.collect()
        return table_info
     
    except Exception as e:
        return str(e)

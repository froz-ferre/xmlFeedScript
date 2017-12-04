import MySQLdb

class TablesInfo():
    cursor, connection = None, None
    tables = []
    parse_times = []
    count_rows = []
    xml_file_links = []
    def __init__(self, db_name):
        self.connection = MySQLdb.connect(host = 'localhost',
                                            user = 'root',
                                            passwd = '322333',
                                            db = db_name)
        self.cursor = self.connection.cursor()

        '''self.tables = self.get_tables_name()
        self.parse_time = get_parse_time()
        self.count_rows = get_count_rows()
        self.xml_file_link = get_xml_file_link()'''

    @staticmethod
    def get_count_rows(self):
        pass

    def get_parse_time(self):
        pass
    @classmethod
    def get_tables_name(self):
        row = self.cursor.execute("SELECT * FROM test")
        row = row.fetchall()
        return str(row)

    def get_xml_file_link(self):
        passs
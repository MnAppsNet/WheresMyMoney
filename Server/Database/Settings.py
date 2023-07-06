from Database.Tables import DatabaseTables

class DatabaseSettings(DatabaseTables):
    def __init__(self):
        super().__init__()
        self.DatabaseName = 'WMM'
        self.Tables = { }
        tables = self.getTables()
        for table in tables:
            fields = self.getFields(table)
            command = f"CREATE TABLE IF NOT EXISTS {table} ("
            key = ""
            for field in fields:
                command += f"{field[0]} {field[1]}, "
                if field[2]:
                    key += f"{field[0]}, "
            command += f"PRIMARY KEY ({key[:-2]}) )"

            self.Tables[f'{table}'] = command
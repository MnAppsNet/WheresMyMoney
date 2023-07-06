import mysql.connector
from Database.Settings import DatabaseSettings

class Database(DatabaseSettings):
    def __init__(self,host,port,user,password):
        super().__init__()
        self.host = host
        self.port = port
        try:
            self.sql = mysql.connector.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=self.DatabaseName )
            if not self.isDatabaseConsistent():
                #Something missing from database, setup again...
                self.setupDatabase(host,port,user,password)
        except mysql.connector.errors.ProgrammingError as exception:
            if exception.errno == 1049 or "Unknown database" in exception.msg:
                #Initial run, start setup...
                self.setupDatabase(host,port,user,password)
        except Exception as exception:
            raise DatabaseError(str(exception),DatabaseError.ErrorCodes.InitializationError)
    
    def isDatabaseConsistent(self):
        command = '''
        SELECT COUNT(TABLE_NAME)
          FROM information_schema.TABLES 
        WHERE TABLE_NAME = '*'
        '''
        cursor = self.sql.cursor()
        for table in self.Tables:
            cursor.execute(command.replace("*",table))
            if cursor.fetchone()[0] != 1:
                cursor.close()
                return False
        cursor.close()
        return True

    def setupDatabase(self,host,port,user,password):
        self.sql = mysql.connector.connect(
                    host=host,
                    port=port,
                    user=user,
                    password=password)
        #Create database :
        cursor = self.sql.cursor()
        command = f"""CREATE DATABASE IF NOT EXISTS {self.DatabaseName}"""
        res = cursor.execute(command)
        cursor.close()
        self.sql.commit()
        
        self.sql = mysql.connector.connect(
                    host=host,
                    port=port,
                    user=user,
                    password=password,
                    database=self.DatabaseName )
        cursor = self.sql.cursor()
        #Create tables :
        for table in self.Tables:
            res = cursor.execute(self.Tables[table])
        
        cursor.close()
        self.sql.commit()


class DatabaseError(Exception):

    class ErrorCodes:
        InitializationError = 1

    def __init__(   self,
                    msg:str = None,
                    errno:int = None ) -> None:
        super().__init__()
        self.msg = msg
        self._full_msg = self.msg
        self.errno = errno or -1

    def __str__(self) -> str:
        return self._full_msg
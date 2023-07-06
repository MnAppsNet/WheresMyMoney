class DatabaseTables:

    def __init__(self):
        self.getTables = DatabaseTables.getTables__
        self.getFields = DatabaseTables.getFields__

    def getTables__():
        return [a for a in dir(DatabaseTables) if not a.endswith('__')]
    def getFields__(table):
        table = getattr(DatabaseTables, table)
        fields = [a for a in dir(table) if not a.endswith('__') and not callable(getattr(table, a))]
        fieldsWithType = [getattr(table, f) for f in fields]
        sortedFieldsWithType = sorted(fieldsWithType,key=lambda x:x[3])
        [a.pop() for a in sortedFieldsWithType]
        return sortedFieldsWithType

    #There is a class for each database table which contains one property per field of the table.
    #Each of these properties is a list which contains on the first index the field name, on the
    #seccond index the field type, on the third index whether it is part of the primary key or not
    #and on the forth index the order of the field in the table 
    class USERS:
        def __str__():
            return 'USERS'
        USERNAME = ['USERNAME','VARCHAR(20) NOT NULL',True,1]
        PASSWORD = ['PASSWORD', 'CHAR(64)',False,2]
        NAME = ['NAME','VARCHAR(25)',False,3]
        SURNAME = ['SURNAME','VARCHAR(25)',False,4]
        EMAIL = ['EMAIL','VARCHAR(150)',False,5]
        CURRENCY = ['CURRENCY','CHAR(4)',False,6]
    class ACCOUNTS:
        def __str__():
            return 'ACCOUNTS'
        ACCOUNT = ['ACCOUNT','VARCHAR(20) NOT NULL',True,1]
        OWNER = ['OWNER','VARCHAR(20)',False,2]
        CURRENCY = ['CURRENCY','CHAR(4)',False,3]
        DESCRIPTION = ['DESCRIPTION','TINYTEXT',False,4]
        DESCRIPTION = ['ICON','INT',False,5]
    class AUTHORIZATIONS:
        def __str__():
            return 'AUTHORIZATIONS'
        ACCOUNT = ['ACCOUNT','VARCHAR(20) NOT NULL',True,1]
        USERNAME = ['USERNAME','VARCHAR(20) NOT NULL',True,2]
        VIEW = ['VIEW_PERM', 'BOOL', False, 3]
        EDIT = ['EDIT_PERM', 'BOOL', False, 4]
        ADD = ['ADD_PERM', 'BOOL', False, 5]
        ADMIN = ['ADMIN_PERM', 'BOOL', False, 6]

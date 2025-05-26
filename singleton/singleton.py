import random


class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DatabaseConnection,cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        # Initialize the connection only once
        # This check ensures that the connection is established only once
        # even if multiple instances are created
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.connection_string = "Database Connection Established"
            print(self.connection_string)
            print('RABDOM NUMBER:', random.randint(1, 100))
    
    
    
if __name__ == "__main__":
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    print(f"db1 id: {id(db1)}")
    print(f"db2 id: {id(db2)}")
    print(f"Are both instances the same? {'Yes' if db1 is db2 else 'No'}")
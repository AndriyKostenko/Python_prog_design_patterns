class SingletonMeta(type):
    """
    A metaclass for creating singleton classes.
    Ensures that only one instance of the class can be created.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
    
class DatabaseConnection(metaclass=SingletonMeta):
    """
    A singleton class for managing a database connection.
    Ensures that only one instance of the connection exists.
    """
    
    def __init__(self):
        # Initialize the connection only once
        self.connection_string = "Database Connection Established"
        print(self.connection_string)
        
if __name__ == "__main__":
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    print(f"db1 id: {id(db1)}")
    print(f"db2 id: {id(db2)}")
    print(f"Are both instances the same? {'Yes' if db1 is db2 else 'No'}")
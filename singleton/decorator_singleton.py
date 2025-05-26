
# Decorator to create a singleton class to prevent multiple instances of a class and only once __init__
def singleton(class_):
    isinstances = {}
    
    def get_instance(*args, **kwargs):
        if class_ not in isinstances:
            isinstances[class_] = class_(*args, **kwargs)
        return isinstances[class_]
    
    return get_instance

@singleton
class DatabaseConnection:
    
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
from pymongo import MongoClient

def init_db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['NetTrafficGuard']  # Create or connect to the database
    print("MongoDB connected and database 'NetTrafficGuard' created.")
    return db

if __name__ == "__main__":
    init_db()

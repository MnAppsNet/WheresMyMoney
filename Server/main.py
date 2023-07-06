from flask import Flask
from config import Config
from Database.database import Database

app = Flask(__name__)
config = Config()
db = None

@app.route('/')
def home():
    return 'Hello, World!'


if __name__ == '__main__':  

    db = Database(
        host=config.getDatabaseHost(),
        port=config.getDatabasePort(),
        user=config.getDatabaseUsername(),
        password=config.getDatabasePassword())
    
    app.run(port=config.getPort())
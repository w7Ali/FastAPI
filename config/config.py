from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://mrwahidali7c:7vZua8SaUVdYNeJ5@craftwork.stazdbp.mongodb.net/?retryWrites=true&w=majority&appName=CraftWork"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))
db = client.CraftWork
# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

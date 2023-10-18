from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        #
        # Connection Variables
        HOST = "nv-desktop-services.apporto.com"
        PORT = 30371
        DB = "AAC"
        COL = "animals"
        #
        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Create method in CRUD - Passes self and document data
    def create(self, data):
        # Check if data parameter is null or empty
        if data is None or data == {}:
            print("Animal failed to be added. Data parameter is empty")
            # Insert unsuccessful - returns false
            return False
        
        else:
            # command to insert document
            self.database.animals.insert_one(data)  # data should be dictionary
            # Insert successful - returns True
            return True

# Read method in CRUD - Passes self and query data
    def read(self, query = None):
        # Check if query parameter is null or empty
        if query is None or query == {}:
            # variable to hold MongoDB cursor position on open query
            data = self.database.animals.find({},{"_id": False}) 
           
        else:
            # variable to hold MongoDB cursor position on animal query
            data = self.database.animals.find(query, {"_id": False})
            # counts number of documents matching query
            count = self.database.animals.count_documents(query)
            # For loop to print query result(s)
            #for document in data:
                #print(document)
            # checks count for query matches and prints if nothing found
            if count == 0:
                print(query, " not found")
        # Returns MongoDB cusor position
        return data
    
# Update method in CRUD - Passes self, queried document to update, updated data
    def update(self, query, update):
        # Check if queried document parameter is null
        if query is not None:
            # variable to hold document update information
            result = self.database.animals.update_many(query, {"$set": update})
            # set variable to the count of modified documents
            count = result.modified_count
            # Check update failed
            if count == 0:
                print("Animal not found")           
        else:
            print("Data parameter is empty. No animal data has been updated")
            # set variable to the count of modified documents
            count = 0

        # Returns number of modified documents in animals collection
        return count

# Delete method in CRUD - Passes self and query data
    def delete(self, query):
        # Check if query parameter is null or empty
        if query is not None:
            # variable to hold document delete information
            result = self.database.animals.delete_many(query)
            # set variable to the count of deleted documents
            count = result.deleted_count
            # Check if deletion failed any documents
            if count == 0:
                print("Animal not found")             
        else:
            print("Data parameter is empty. No animal data has been deleted")
            # set variable to the count of modified documents
            count = 0
        # Returns number of deleted documents in animals collection
        return count

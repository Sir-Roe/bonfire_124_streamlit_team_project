from base import Base
from dotenv import load_dotenv
import pymongo
import os

# Class Declaration:
class ToMongo(Base):
    '''
    Designed as a class to transport the data from the Base class to a MongoDB instance.
    Initializes an instance of the inherited class.
    
    Defined methods are as follows:.
    upload_collection: upload an entire document of items to MongoDB
    delete_collection: drops an entire collection of data
    '''
    
    def __init__(self, user=os.getenv('USERNAME'), password=os.getenv('PASSWORD')):
        
        # Load the env variables:
        load_dotenv()
        self.user = user
        self.password = password
        self.mongo_url = "mongodb+srv://lmproe27:SirRoe124@cluster0.zhnjqzj.mongodb.net/?retryWrites=true&w=majority"
        #self.mongo_url = os.getenv('MONGO_URL')
        #Connect to PyMongo
        self.client = pymongo.MongoClient(self.mongo_url)
        # Create a database
        self.db = self.client.db
        # Create a collection:
        self.park_info = self.db.park_info
        # Set dataframe index to the id column:
        
        
    #def upload_collection(self):
    #    self.park_info.insert_many([self.df.to_dict()])

    def upload_one_by_one(self):
        #delete old db on every re upload
        self.park_info.drop()
        # Initialize the instance of our inherited class:
        Base.__init__(self)
        self.df.set_index('id', inplace=True)
        for i in self.df.index:
            self.park_info.insert_one(self.df.loc[i].to_dict())
        
if __name__ == '__main__':
    c = ToMongo()
    print('Successful Connection to Client Object')
    c.upload_one_by_one()
    print('Successfully Uploaded all Park Info to Mongo')
# Hash Package
import hashlib

from compose.progress_stream import print_output_event
from samba.dcerpc.lsa import String

TABLE_SIZE = 5

def HashID(ID, size = TABLE_SIZE):
    # Using SHA256 to hash the string, and then mod it by the desired size
    return int(hashlib.sha256(ID.encode('utf-8')).hexdigest(), 16) % size

class HashTable:
    def __init__(self):
        # Index To Contain Item Ids
        self.id_index = [[] for _ in range(TABLE_SIZE)]

        # Index To Contain Names
        self.nameIndex = [[] for _ in range(TABLE_SIZE)]
        #Simple Array To Contain Name For Listing
        self.names = []


        # Index To Contain Expiry Allowing Grouping Of Items With Same Expiry
        self.expiryIndex = [[] for _ in range(TABLE_SIZE)]
        self.expiryList = []

        # Index to Contain Categories
        self.categoryIndex = [[] for _ in range(TABLE_SIZE)]
        # Simple Array To Contain Listable Categories
        self.categories = []


        # Index To Save Stock Allowing Grouping Of Items With Same Stock
        self.stockIndex = [[] for _ in range(TABLE_SIZE)]
        self.stockLists = []

    def HashID(self, value, size=TABLE_SIZE):
        # Using SHA256 to hash the string, and then mod it by the desired size
        return int(hashlib.sha256(value.encode('utf-8')).hexdigest(), 16) % size

    def put(self, itemid, name, current_stock, price, category, expiry):

        # Creating Object For The Data
        DataObject = {
            name: name,
            itemid: itemid,
            price: price,
            category: category,
            expiry: expiry
        }

        # Save Data Based On ItemID Index
        idHash = HashID(str(itemid))
        self.id_index[idHash] = [DataObject] # No Need To Append As Item ID will be unique.

        # Save Data Based On Name
        nameHash = HashID(str(name))
        self.nameIndex[nameHash].append(DataObject) # Multiple Items For Same Name Can Be Added
        self.names.append(name)

        # Save Data Based On Expiry
        expiryHash = HashID(expiry)
        self.expiryIndex[expiryHash].append(DataObject) # Multiple Item For Same Expiry Can Be Added
        self.expiryList.append(expiry)

        categoryHash = HashID(category)
        self.categoryIndex[categoryHash].append(DataObject)
        self.categories.append(category)

        stockHash = HashID(current_stock)
        self.stockIndex[stockHash].append(DataObject)
        self.stockLists.append(current_stock)

    def getID(self, value):
        print("Hello")

    def getName(self, value):
        print(1)

    def getCategory(self, value):
        print(2)

    def delete(self, id):
        print("HEllo")

    def updateStock(self, id, value):
        print("Hello")

    def Save(self):
        print("Hello")

    def Load(self):
        print("Hello")


talbex = HashTable()
talbex.put(12, "Ghee", "12", "11", "Home", "2024-11-13")
print(talbex.id_index)
print(talbex.nameIndex)
print(talbex.stockIndex)
print(talbex.categoryIndex)
print(talbex.expiryIndex)
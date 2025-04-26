TABLE_SIZE = 15
id_index = [[] for _ in range(TABLE_SIZE)]
import hashlib
def HashID(value, size=TABLE_SIZE):
    # Using SHA256 to hash the string, and then mod it by the desired size
    return int(hashlib.sha256(value.encode('utf-8')).hexdigest(), 16) % size

id = HashID("Almarai Milk")

itemid = 3
name = "Ghee"
price = 22
category = "Home Items"
expiry = "2024-12-11"

idHash = HashID(str(itemid))
id_index[idHash].append({"itemID": itemid, "itemName":name, "itemPrice":price, "Category":category, "expiry":expiry})
id_index[idHash].append({"itemID": 5, "itemName":name, "itemPrice":price, "Category":category, "expiry":expiry})
print(id_index[idHash])
id_index[idHash] = {"itemID": 5, "itemName":name, "itemPrice":price, "Category":category, "expiry":expiry}
print(id_index[idHash])



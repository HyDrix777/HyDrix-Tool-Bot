import pymongo

from infog import DATABASE_URI, DATABASE_NAME
myclient = pymongo.MongoClient(DATABASE_URI)
mydb = myclient[DATABASE_NAME]
mycol = mydb['CONNECTION']




async def active_connection(user_id):

    query = mycol.find_one(
        { "_id": user_id },
        { "_id": 0, "group_details": 0 }
    )
    if not query:
        return None

    group_id = query['active_group']
    if group_id != None:
        return int(group_id)
    else:
        return None

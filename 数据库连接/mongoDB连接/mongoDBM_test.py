from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId  # 按照id查询的时候需要用到


class TestMongo(object):
    def __init__(self):
        self.client = MongoClient()  # 获取连接
        # self.client2 = MongoClient('localhost', 27017)
        # self.client3 = MongoClient('mongodb://localhost:27017')
        self.db = self.client['student']  # 打开相应的数据库

    def add_one(self):
        post = {'name': '姓名1', 'age': 16, 'sex': 'male', 'grade': 63.2, 'address': datetime.now()}
        return self.db.student.insert_one(post)

    def get_one(self):
        return self.db.student.find_one()

    def get_more(self):
        # return self.db.student.find()#查询全部
        return self.db.student.find({'sex': 'male'})  # 查询性别为男的数据

    def get_one_from_oid(self, oid):
        obj = ObjectId(oid)
        return self.db.student.find_one({'_id': obj})

    def update(self):
        # 更新一条数据，修改name是xi的年龄加10
        # return self.db.student.update_one({'name':'xi'},{'$inc':{'age':10}})
        # 更新多条数据，年龄全部加10
        return self.db.student.update_many({}, {'$inc': {'age': 10}})

    def delete(self):
        #删除一条数据
        # return self.db.student.delete_one({'name':'xi'})
        #删除多条数据
        return self.db.student.delete_many({'age': 26})



def main():
    obj = TestMongo()
    # rest = obj.add_one()
    # print(rest.inserted_id)

    # rest=obj.get_one()
    # print(rest)
    # print(rest['_id'])

    # rest = obj.get_more()
    # for item in rest:
    #     print(item)

    # rest = obj.get_one_from_oid('5e4f8c785b110f7c5fa20a0e')
    # print(rest)

    # rest = obj.update()

    rest = obj.delete()
    print(rest.deleted_count)

if __name__ == '__main__':
    main()

# print(client.PORT)
# print(client.HOST)
# print(client.list_database_names())

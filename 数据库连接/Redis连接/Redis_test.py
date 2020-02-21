# pip install redis
# https://github.com/andymccurdy/redis-py

import redis

class Base(object):
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

class TestString(object):
    def __init__(self):
        # r = redis.Redis(host='localhost', port=6379, db=0)
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)
    # 设置单个值
    def test_set(self):
        rest = self.r.set('user2','Amy')
        print(rest)
        return rest
    # 获取单个值
    def test_get(self):
        rest = self.r.get('user2')
        print(rest)
        return rest
    # 设置多个值
    def test_mset(self):
        d = {'user3':'Bob','user4':'Bobx'}
        rest= self.r.mset(d)
        print(rest)
        return rest

    # 获取多个值
    def test_mget(self):
        lst = ['user3', 'user4']
        rest = self.r.mget(lst)
        print(rest)
        return rest
    # 删除
    def test_del(self):
        rest = self.r.delete('user3')
        print(rest)


class TestList(object):
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)
    # 设置和读取
    def test_push(self):
        t= ['Amy','Jhon']
        rest=self.r.lpush('l_eat',*t)
        print(rest)
        rest=self.r.lrange('l_eat',0,-1)
        print(rest)
    # pop删除元素
    def test_pop(self):
        rest=self.r.lpop('l_eat')
        print(rest)
        rest = self.r.lrange('l_eat',0,-1)
        print(rest)


class TestSet(Base):
    # 添加元素
    def test_sadd(self):
        lst = ['Cat', 'Dog']
        rest = self.r.sadd('zoo3', *lst)
        print(rest)
        rest = self.r.smembers('zoo3')
        print(rest)
    # 删除元素
    def test_srem(self):
        rest = self.r.srem('zoo2', 'Dog')
        print(rest)
        rest = self.r.smembers('zoo2')
        print(rest)
    # 求交集
    def test_sinter(self):
        rest = self.r.sinter('zoo2', 'zoo3')
        print(rest)

    # 求并集
    def test_sunion(self):
        rest = self.r.sunion('zoo2', 'zoo3')
        print(rest)




def main():
    # str_obj = TestString()
    # str_obj.test_set()
    # str_obj.test_get()
    # str_obj.test_mset()
    # str_obj.test_mget()
    # str_obj.test_del()

    # list_obj=TestList()
    # # list_obj.test_push()
    # list_obj.test_pop()

    set_obj=TestSet()
    # set_obj.test_sadd()
    # set_obj.test_srem()
    # set_obj.test_sinter()
    set_obj.test_sunion()


if __name__ == '__main__':
    main()
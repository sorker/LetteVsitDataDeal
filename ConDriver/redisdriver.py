# -*- coding:utf-8 -*-
"""
 @time    : 2019/4/19 14:18
 @desc    : this is a desc
 @Author  : Sorke
 @Email   : sorker0129@hotmail.com
"""
import redis



class RedisDriver:
    def __init__(self):
        self.POOL = redis.ConnectionPool(host='127.0.0.1', port='6379')
        self.CON = redis.Redis(connection_pool=self.POOL)

    def driver(self):
        return self.CON

    def department_fre_set(self, name_value, frequency, ex=3, px=None, nx=False, xx=False):
        """
        :param name_value: 部门名.词
        :param frequency: 词频
        :return:
        """
        self.driver().set(name_value, frequency, ex=ex, px=px, nx=nx, xx=xx)

    def classification_weight_set(self, classification, context, nx=False, xx=False):
        """
        :param name_value: 部门名.词
        :param frequency: 词频
        :return:
        """
        self.driver().set(classification, context, nx=nx, xx=xx)

    def city_area_department(self, name_value, department, nx=False, xx=False):
        """
        :param name_value: 部门名.词
        :param frequency: 词频
        :return:
        """
        self.driver().set(name_value, department, nx=nx, xx=xx)

    def value_get(self, name_value):
        """
        :param name_value: 部门名.词
        :return frequency 频率
        """
        return self.driver().get(name_value)

    def key_exists(self, key):
        return self.driver().exists(key)

    def keys_get(self):
        """
        :param name_value: 部门名.词
        :return frequency 频率
        """
        return self.driver().keys()


redisdriver = RedisDriver()

if __name__ == "__main__":
    # redisdriver.driver().set('123', '122')
    # keys = redisdriver.driver().keys()
    # for key in keys:
    #     if key.decode() == '123':
    #         redisdriver.department_fre_get(key)
    #         print('=========================================================================')
    #         print('=========================================================================')
    #         print('=========================================================================')
    #         print('=========================================================================')
        # print(key.decode())
        # print(str(key).split('\'')[1])
    # print(redisdriver.value_get(b'123'))
    # redisdriver.driver().delete(b'123')
    # redisdriver.driver().delete(b'asd')
    for a in redisdriver.keys_get():
        redisdriver.driver().delete(a)

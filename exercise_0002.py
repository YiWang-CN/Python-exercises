#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）
# 保存到 MySQL 关系型数据库中。
import pymysql.cursors
from exercise_0001 import exercise_0001

connect = pymysql.connect(
    host='localhost',
    port=3306,
    user='',
    password='123456',
    db='test',   #默认连接的数据库
    # charset='utf8',  #编码方式
)

# 获取游标(sql查询窗口）
cursor = connect.cursor()

def create_table(name,db):
    cursor.execute('SHOW TABLES IN %s;' % db)  #sql语句，查看表格
    #fetchall()执行查询时，获取结果集的所有行，一行构成一个元组，再将这些元组装入一个元组返回
    tables = cursor.fetchall()
    findtables = False  #辅助判断语句
    for table in tables:
        if name in table:
            findtables = True
            print ('表格已经创建')
    if not findtables:
        cursor.execute('''
                    CREATE TABLE %s(
                    id INT NOT NULL AUTO_INCREMENT,
                    encode_keys varchar(50),
                    PRIMARY KEY(id))
        ''' % name)  #SQL语句，创建表格，里面的参数设置
        connect.commit() #提交语句，才能执行上面创建表格命令
        print('成功创建' + str(name) + '表格')
def input_keys( table_name , keys  ): #输入商品名与密匙
    sql = "INSERT INTO " + str(table_name)  + " (encode_keys) VALUES ('%s')"
    data = str(keys)
    cursor.execute(sql % data)
    connect.commit()
if __name__ == '__main__':

    db = 'test'
    table = 'try'
    create_table(table, db)
    num = 5
    keys = exercise_0001.gen_key(num)
    i = 1
    for key in keys:
        input_keys(table, key)
        print('已经输入了 %s 条数据' %str(i))
        i=i+1

    cursor.close() #关闭游标
    connect.close()  #关闭连接


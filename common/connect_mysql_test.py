import pymysql


#连接数据库
db = pymysql.connect(host='49.235.92.12',
                     port=3309,
                     user='root',
                     passwd='123456',
                     db='online',
                     cursorclass=pymysql.cursors.DictCursor
                     )

#创建游标cursor
cursor = db.cursor()

#sql查询语句
sql1 = "SELECT * FROM users_userprofile WHERE username = '1234@qq.com';"

#根据游标执行sql语句，得到一条数据
cursor.execute(sql1)

#获取数据完整内容
result = cursor.fetchall() #默认返回是元组，不易取值，连接配置时设置返回list of dict
print(result)
print(result[0]['username'])

#删除数据sql语句
delete_sql = "DELETE FROM users_userprofile WHERE username = '928371343@qq.com';"

#游标执行删除sql
cursor.execute(delete_sql)

#数据库提交操作；在操作数据库进行新增、编辑、删除时需要执行
db.commit()

#关闭游标
cursor.close()

#关闭数据库
db.close()

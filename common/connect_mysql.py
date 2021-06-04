import pymysql

#封装数据库操作

#配置数据库相关信息
dbinfo = {
    'host':'49.235.92.12',
    'user':'root',
    'password':'123456',
    'port':3309
}


#创建DbConnect类
class DbConnect():
    #数据库初始化配置
    def __init__(self, db_conf, database=''):
        self.db_conf = db_conf
        #打开数据库连接
        self.db = pymysql.connect(database=database,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  **db_conf     # **表示字典分别以键值对传入参数
                                  )

        #使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()

    #定义select查询方法
    def select(self,sql):
        # SQL 查询语句返回 list of dict
        # sql = "SELECT * FROM employee WHERE income > %s" %(1000)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    #定义execute执行方法
    def execute(self,sql):
        # SQL 删除、新增、修改语句
        # sql = "DELETE FROM employee WHERE age > %s"% (20)
        try:
            #执行sql语句
            self.cursor.execute(sql)
            #提交修改
            self.db.commit()
        except:
            # 发生错误时进行回滚
            self.db.rollback()


    #定义close方法
    def close(self):
        #关闭数据库连接
        self.db.close()



if __name__ == '__main__':
    db = DbConnect(dbinfo,'online')    #数据库连接实例化
    sql1 = "SELECT * FROM users_userprofile WHERE username = '1234@qq.com';"
    result = db.select(sql1)
    print(result)

    # 删除数据
    sql2 = "DELETE FROM users_userprofile WHERE username = 'saggadfadfeew2233@qq.com';"
    db.execute(sql2)
# -*- coding:utf-8 -*-
import pyodbc

host = '127.0.0.1'
user = 'kqdba'
pwd = 'tc3h81'
db = 'qykq'


class MSSQL:
    # def __init__(self, host, user, pwd, db):
    #     self.host = host
    #     self.user = user
    #     self.pwd = pwd
    #     self.db = db

    def __GetConnect(self):
        if not db:
            raise (NameError, "没有设置数据库信息")
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s' % (
            host, db, user, pwd), charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    def ExecQuery(self, sql, parameters):
        """
        执行语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段

        调用示例：
                ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id),NickName
        """
        cur = self.__GetConnect()
        cur.execute(sql, parameters)
        # resList = cur.fetchall()
        self.conn.commit()
        # 查询完毕后必须关闭连接
        self.conn.close()
        # print u"执行完毕"

    def exec_select_query(self, sql, parameters):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段

        调用示例：
                ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id),NickName
        """
        cur = self.__GetConnect()
        cur.execute(sql, parameters)
        resList = cur.fetchall()
        self.conn.commit()
        # 查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def exec_simple_select_query(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()
        self.conn.commit()
        # 查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def exec_one_query(self, sql, parameters):
        cur = self.__GetConnect()
        cur.execute(sql, parameters)
        resList = cur.fetchone()
        self.conn.commit()
        # 查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ClearTable(self, tb):
        sql = "Truncate Table " + tb + ";"
        cur = self.__GetConnect()
        cur.execute(sql)
        # resList = cur.fetchall()
        self.conn.commit()
        # 查询完毕后必须关闭连接
        self.conn.close()
        print u"执行清除完毕"

    def ExecNonQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()


def main():
    ## ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
    ## #返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
    ## ms.ExecNonQuery("insert into WeiBoUser values('2','3')")

    ms = MSSQL()

    resList = ms.exec_simple_select_query("select EMPNAME, ORGNAME from v_oa_bm")
    for (EMPNAME, ORGNAME) in resList:
        print EMPNAME, ORGNAME


if __name__ == '__main__':
    main()

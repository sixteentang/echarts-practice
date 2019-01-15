
import sqlite3

# 连接数据库，打开该数据库文件，如果没有则自动新建
conn = sqlite3.connect('test.db')

# 创建游标
cursor = conn.cursor()

# 创建表
cursor.execute('drop table if exists table1')
cursor.execute('create table table1 (categories text,data int)')

# 数据
dd = [
    ("衬衫",5),
    ("羊毛衫",20),
    ("雪纺衫",36),
    ("裤子",10),
    ("高跟鞋",10),
    ("袜子",20)
    ]

# 插入数据
cursor.executemany('insert into table1 values (?,?)',dd)

# 关闭游标
cursor.close()

# 提交
conn.commit()

# 关闭连接
conn.close()


和sqlite不同之处：
这里的数据库文件不是用Python代码生成，而是事先用mysql工具生成。
该数据库文件在C:\ProgramData\MySQL\MySQL Server 5.7（显示隐藏文件）
这个目录也就是服务器上的数据所在位置。（简单来说，就是这台本机，既是服务器，又是客户端，而服务器有数据库的服务器，和web服务器，这个目录就是数据库服务器所在位置）

另，要想显示可视化，必须访问数据库的服务器，所以必须打开数据库的服务器，命令行（管理员）输入：
net start mysql57
关闭服务器：
net stop mysql57
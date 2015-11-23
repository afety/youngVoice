## 大部分代码和news中相似

1. youngVoice 文件夹里面是代码
2. 建立数据库的时候直接source youngVoice.sql

## youngVoice文件夹里面的内容

### model 数据库操作:
- admin.py
	和管理员相关的数据库操作
- article.py
	青听和青说
- notice.py
	公告
- question.py
 	青问/青答

### controller 视图函数相关：
- index.py
	首页
- article.py
	青听和青说
- notice.py
	公告
- question.py
	青问/青答
- admin.py
	后台相关
- log.py
	日志记录
- utils.py
	工具相关

> 所以大概有article/admin/notice/question这四个模块相应的model层和controller层要写，没人选一个好了QWQ。

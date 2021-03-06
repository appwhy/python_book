# python其他库

[TOC]

<!-- toc -->

---

## argparse

链接：[link](https://docs.python.org/zh-cn/dev/library/argparse.html)

```python
import argparse

if __name__=='__main__':
	parser = argparse.ArgumentParser(description="Demo of argparse")  # 参数解析器
    
    parser.add_argument('cmd', type=str, nargs='?', help='help info')

    parser.add_argument('-n', '--name', default=' Li ')
    parser.add_argument('-y', '--year', default='20')
    
    parser.add_argument('--debug', action="store_true")  # 不需要跟值，使用该选项就会使debug属性为True。如果不加该参数，debug值默认False。'store_false'则相反
    
    args = parser.parse_args()
    print(args)
    name = args.name
    year = args.year
    
    print('Hello {}  {}'.format(name, year))
```

`nargs` 参数来限定输入的位置参数的个数，默认为1。当然nargs参数也可用于普通带标签的参数。

nargs 字符串：

* `'*'`：之后所有的输入都将作为该位置参数的值
* `'+'`：表示读取至少1个该位置参数。
* `'?'`：表示该位置参数要么没有，要么就只要一个。



参数被多次传递，可能会失真，尤其是带有单引号、双引号时。参考argparse模块。

## jinja2

Jinja2是Python下一个被广泛应用的模版引擎，他的设计思想来源于Django的模板引擎，并扩展了其语法和一系列强大的功能。其中最显著的一个是增加了沙箱执行功能和可选的自动转义功能，这对大多应用的安全性来说是非常重要的。

Flask使用jinja2作为框架的模板系统。使用django等其他Python web框架也可以方便的集成jinja2模板系统

如果将减号（`-`）添加到块的开头或结尾（例如For标签），注释或变量表达式，则将删除该块之前或之后的空格。

```python
from jinja2 import Template
template = Template('Hello {{ name }}!')
template.render(name='John Doe')
# Out: 'Hello John Doe!'
```

jinja2可以操作列表（元组 ）、字典、对象。

列表：

```jinja2
li.0
li[0]
{% for i in range(10) %}
      {{ i }}
{% endfor %}
```

jinja2预定义的一些变量：

|     变量      |              含义               |
| :-----------: | :-----------------------------: |
| `loop.index`  |    循环中的迭代计数，从1开始    |
| `loop.index0` |    循环中的迭代计数，从0开始    |
| `loop.first`  |     是否为循环的第一个元素      |
|  `loop.last`  |    是否为循环的最后一个元素     |
| `loop.length` |      循环序列中元素的个数       |
| `loop.depth`  | 当前循环在递归中的层级，从1开始 |
| `loop.depth0` | 当前循环在递归中的层级，从0开始 |



## codecs

```
codecs : Python Codec Registry, API and helpers. coder, decoder
```

python的内部是使用unicode来处理的，但是unicode的使用需要考虑的是它的编码格式有两种，一是UCS-2，它一共有65536个码 位，另一种是UCS-4，它有2147483648g个码位。

可以通过以下代码查看：

```python
import sys
print(sys.maxunicode)
```



```python
import codecs
fw = codecs.open('test1.txt','a','utf-8')
fw.write(line2)
```

```python
open(filename, mode='r', encoding=None, errors='strict', buffering=1)
```



## pipreqs

pipreqs可以找到当前项目使用的所有python包及其版本。

```bash
# 1.在项目根目录下执行命令
pipreqs ./  # 报错就执行下面这条
pipreqs ./ --encoding=utf-8

# 2.可以看到在根目录下生成了requirements.txt

# 3.执行下面代码就会把项目用到的所有组件装上
pip3 install -r requirements.txt
```



## colorama：命令行输出彩色文字

想要输出带有颜色的文字，需要加上前后缀。首先是27的8进制或者16进制的表示，然后a代表显示方式（可省略），x代表前景色（字体颜色），y代表背景色

```python
"\033[a;x;ym【文字】\033[x;ym"

"\x1b[a;x;ym【文字】\x1b[x;ym"


前景色         背景色           颜色
---------------------------------------
30                40              黑色
31                41              红色
32                42              绿色
33                43              黃色
34                44              蓝色
35                45              洋红
36                46              青色
37                47              白色

显示方式             　 意义
----------------------------------
0                    终端默认设置
1                    高亮显示
22　　　　　　　　　　　非高亮显示
4                    使用下划线
24　　　　　　　　　　　去下划线
5                    闪烁
25　　　　　　　　　　　去闪烁
7                    反白显示
27　　　　　　　　　　　非反显
8                    不可见
28　　　　　　　　　　　可见
 
例：
\033[1;32;41m   #---1-高亮显示 32-前景色绿色  40-背景色红色---
\033[0m         #---采用终端默认设置，即缺省颜色---   
```



 *colorama*是一个python专门用来在控制台、命令行输出彩色文字的模块，可以跨平台使用。

colorama内部模块：Fore是针对字体颜色，Back是针对字体背景颜色，Style是针对字体格式。

```
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
```



init()接受一些* * kwargs覆盖缺省行为，

autoreset是自动恢复到默认颜色。

```python
from colorama import init, Fore, Back

init(autoreset=True)

print(Fore.BLUE + "hgg")
print(Fore.YELLOW + Back.RED + "XXXX")
print("hello world")
```








## curses

python 中curses封装了c语言的curses。curses是一个在linux/unix下广泛应用的图形函数库，作用是可以在终端内绘制简单的图形用户界面。*curses*库不*支持Windows*操作系统，但有一个非正式curses包可以尝试，另外windows平台可以使用Console模块。

curses的名字起源于"cursor optimization"，即光标优化。

可以说，curses是Linux终端图形编程的不二选择（比如著名的文字编辑器 vi 就是基于curses编的）。



## csv相关

python标准库自带CSV模块。

```python
import csv

csvfile = open('csv_test.csv', 'r')

# 以列表形式输出
reader = csv.reader(csvfile)
rows = [row for row in reader]

# 以字典形式输出，第一行作为字典的键
reader = csv.DictReader(csvfile)
for row in reader:
	# row 是一个 dict

# 写文件
# 若存在文件，打开csv文件，若不存在即新建文件
# 如不设置newline=''，每行数据会隔一行空白行
csvfile = open('csv_test.csv', 'w', newline='')
# 将文件加载到csv对象中
writer = csv.writer(csvfile)
# 写入一行数据
writer.writerow(['姓名', '年龄', '电话'])
# 多行数据写入
data = [
    ('小P', '18', '138001380000'),
    ('小Y', '22', '138001380000')
]
writer.writerows(data)
# 关闭csv对象
csvfile.close()
```



## excel相关

python操作excel的有xlrd（xls read），xlwt（xls write）。

```
pip install xlrd
pip install xlwt
```


```python
import xlwt

# 新建一个Excel文件
wb = xlwt.Workbook()
# 新建一个Sheet
ws = wb.add_sheet('Python', cell_overwrite_ok=True)

# 定义格式对象
style = xlwt.XFStyle()

# 合并单元格write_merge(开始行, 结束行, 开始列, 结束列, 内容, 格式)
ws.write_merge(0, 0, 0, 5, 'Python', style)

# 写入数据wb.write(行,列,内容)
for i in range(2, 7):
    for k in range(5):
        ws.write(i, k, i+k)
    # Excel公式xlwt.Formula
    ws.write(i, 5, xlwt.Formula('SUM(A'+str(i+1)+':E'+str(i+1)+')'))

# 插入图片，insert_bitmap(img, x, y, x1, y1, scale_x=0.8, scale_y=1)
# 图片格式必须为bmp
# x表示行数，y表示列数
# x1表示相对原来位置向下偏移的像素
# y1表示相对原来位置向右偏移的像素
# scale_x，scale_y缩放比例
ws.insert_bitmap('test.bmp', 9, 1, 2, 2, scale_x=0.3, scale_y=0.3)

# 保存文件
wb.save('file.xls')
```




```python
import xlrd

wb = xlrd.open_workbook('file.xls')

# 获取Sheets总数
ws_count = wb.nsheets

# 通过索引顺序获取Sheets
# ws = wb.sheets()[0]
# ws = wb.sheet_by_index(0)

# 通过Sheets名获取Sheets
ws = wb.sheet_by_name('Python')

# 获取整行的值（以列表返回内容）
row_value = ws.row_values(3)

# 获取整列的值（以列表返回内容）
row_col = ws.col_values(3)

# 获得行列数
nrows = ws.nrows
ncols = ws.ncols

# 获取某个单元格内容cell(行, 列)
cell_F3 = ws.cell(2, 5).value

# 使用行列索引获取某个单元格内容
row_F3 = ws.row(2)[5].value
col_F3 = ws.col(5)[2].value
```



## word相关

```
pip install python-docx
```


```python
import docx
from docx.shared import Inches

doc = docx.Document('test.docx')
# 读取全部内容
paras = doc.paragraphs
# 处理每一个段落（以\n划分段落）
for p in paras:
    # xxx


# 创建对象
document = Document()

# 添加正文内容并设置部分内容格式
p = document.add_paragraph('Python 爬虫开发-')
# 设置内容加粗
p.runs[0].bold = True

p.add_run('存储实例。').italic = True

# 添加正文，设置'样式'-'明显引用'
document.add_paragraph('样式-明显引用', style='IntenseQuote')

# 添加图片
document.add_picture('test.png', width=Inches(1.25))

# 添加表格
table = document.add_table(rows=1, cols=3)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = 'Qty'

# 保存文件
document.add_page_break()
document.save('test.docx')
```




## mongodb

可视化工具：**RoboMongo**，MongoBooster。

```
pip install pymongo
```


```python
import pymongo

# 创建对象
client = pymongo.MongoClient()
# client = pymongo.MongoClient('localhost', 27017)
# client = pymongo.MongoClient('mongodb://localhost:27017/')

# 进行认证
db_auth = client.admin
db_auth.authenticate(username, password)

# 用户验证方法2
# client = pymongo.MongoClient('mongodb://username:password@localhost:27017/')

# 连接DB数据库
db = client['DB']

# 连接集合user，集合类似关系数据库的数据表。如果集合不存在，会新建集合user
user_collection = db.user

# 插入数据，user_info是一个dict
user_id = user_collection.insert_one(user_info).inserted_id

# 批量添加，user_infos是一个关于dict的列表
user_collection.insert_many(user_infos)
```


更新文档

$set：指定键值，不存在则创建。

$unset：从文档中移除指定的键。

$inc：进行算术加减操作，只用于整数、长整数、双精度浮点数。

$rename：重命名字段名称

$push：如果指定的键存在，就向已有的数组末尾添加一个元素。否则创建一个新的数组。

$and、$or：后面跟数组。

$lt、$lte、$gt、$gte、$in、$nin：比较操作符。

$regex：正则表达式



## mysql/sqlalchemy

```bash
pip install SQLAlchemy
pip install pymysql
```


```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# 创建数据表方法一
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class mytable(Base):
    # 表名
    __tablename__ = 'mytable'
    # 字段，属性
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    age = Column(Integer)
    birth = Column(DateTime)
    class_name = Column(String(50))

Base.metadata.create_all(engine)

# 创建数据表方法二
from sqlalchemy import Column, MetaData, ForeignKey, Table
from sqlalchemy.dialects.mysql import (INTEGER, CHAR)
meta = MetaData()
myclass = Table('myclass', meta,
                Column('id', INTEGER, primary_key=True),
                Column('name', CHAR(50), ForeignKey(mytable.name)),
                Column('class_name', CHAR(50))
                )
myclass.create(bind=engine)



engine = create_engine("mysql+pymysql://root:1990@localhost:3306/test?charset=utf8",echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()

new_data = mytable(name='Li Lei',age=10,birth='2017-10-01',class_name='一年级一班')
session.add(new_data)
session.commit()

session.query(mytable).filter_by(id=1).update({ mytable.age : 12})
session.commit()

get_data = session.query(myclass.name, myclass.class_name).all()
get_data = session.query(myclass).filter_by(id=1).all()

# 内连接
get_data = session.query(mytable).join(myclass).filter(mytable.class_name == '三年级二班').all()

# 外连接
get_data = session.query(mytable).outerjoin(
             myclass).filter(mytable.class_name == '三年级二班').all()

sql = 'select * from mytable '
session.execute(sql)

session.close()
```

### 通过反射获取对象

反射可以得到2种对象，`class 'sqlalchemy.ext.declarative.api.DeclarativeMeta' (class 'sqlalchemy.ext.automap.data_sync')`， `class 'sqlalchemy.sql.schema.Table'`， Table一点都不好操作，推荐使用前一个。

```python
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.automap import automap_base

engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(user, pswd, ip, port, dbname),
                        pool_size=30, pool_recycle=300, pool_pre_ping=True, echo=echo)

# Base.prepare本质是调用Base.metadata的reflect方法
def reflect_all_tables(engine):
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    table = Base.classes['data_sync']           # class 'sqlalchemy.ext.declarative.api.DeclarativeMeta'
    table = Base.metadata.tables['data_sync']   # class 'sqlalchemy.sql.schema.Table'

def reflect_single_table(engine, table_name):
    metadata = MetaData(engine)
    metadata.reflect(engine, only=[table_name])

    Base = automap_base(metadata=metadata)
    Base.prepare()

    table = metadata.tables[table_name]
    table = Base.classes[table_name]
```





打印mysql语句

```python
from sqlalchemy.dialects import mysql

print(q.statement.compile(dialect=mysql.dialect(), compile_kwargs={"literal_binds": True}))

# 这种方式可以打印包含参数的执行语句，但是参数只包括数字和字符串等基本类型。

print(q.statement.compile().params)
# {u'id_1': 1} 
```



### 反射没有主键的表




## redis





## OCR

```
pip install pyocr
pip install Pillow
```


Pillow处理图像。

```python
from PIL import Image
from pyocr import tesseract

im = Image.open('1.png')
im = im.convert('L')  # 图片转换为灰色图像, 转化后识别率更高
# 保存转换后的图片
im.save("temp.png")
code = tesseract.image_to_string(im)
print(code)
```




## GUI库：PyQt5

```
pip install PyQt5
pip install PyQt5-tools
```


安装PyQt5-tools后，在Lib/site-packages/pyqt5-tools中找到designer.exe，用其进行界面设计。



将ui文件转换为py文件。

```
python -m PyQt5.uic.pyuic xxx.ui -o xxx_v.py
```




## 进度条：tqdm

1. tqdm：阿拉伯语中的“process“，对循环或者迭代器，显示进度条。

   ```
   from tqdm import tqdm
   import time
   for i in tqdm(range(19), desc="进度条"):
       time.sleep(0.5)
   ```



## kazoo：zookeeper API

建立连接：

```python
from kazoo.client import KazooClient
host = 'localhost:2181'
zk = KazooClient(host)
zk.start()

# 相关操作

zk.stop()
```



获得某个节点的信息，返回一个元组：

```python
zk.get('/')
# Out[10]:(b'', ZnodeStat(czxid=0, mzxid=4, ctime=0, mtime=1558407882652, version=1, cversion=4, aversion=1, ephemeralOwner=0, dataLength=0, numChildren=6, pzxid=288))
```

获取某个节点的所有字节点，返回一个子节点名称的列表：

```python
zk.get_children('/')
# Out[11]: ['default', 'route', 'zookeeper', 'test', 'config']
```

获取某个节点的acl（access control list），返回一个元组：

```python
zk.get_acls('/')
# Out[12]: ([ACL(perms=31, acl_list=['ALL'], id=Id(scheme='world', id='anyone')),  ACL(perms=31, acl_list=['ALL'], id=Id(scheme='digest', id='fsi:NLfFQJbUxUqJLJOtUIyVEQrlNeM='))],   ZnodeStat(czxid=0, mzxid=4, ctime=0, mtime=1558407882652, version=1, cversion=4, aversion=1, ephemeralOwner=0, dataLength=0, numChildren=6, pzxid=288))
```

创建一个节点，返回一个路径字符串：

```python
zk.create('/test/hg_test/test2/test3/node',b'hello world')
```



## retrying

`pip install retrying`

```python
from retrying import retry

# 一直重试，直到成功
@retry
def func():
    pass


# 最多重试5次， 每次重试间隔时间增加2秒
@retry(stop_max_attempt_number=5, wait_incrementing_increment=2000)
```



## inspect

inspect模块用于收集python对象的信息，可以获取类或函数的参数的信息，源码，解析堆栈，对对象进行类型检查等等。

```python
from inspect import Signature, signature

# 获取函数参数及其默认值
sig = signature(getattr(A_Class, func_name))
for field, parameter in sig.parameters.items():  
    if parameter.default is not Signature.empty: # 参数带有默认值 
        print('参数名: {}, 默认值: {}'.format(field, parameter.default))
```






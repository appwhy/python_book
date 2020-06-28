# python常用库

[TOC]

<!-- toc -->

---

## collections

### namedtupe

跟`tuple`相比，`namedtuple` 返回的子类可以使用名称来访问元素。

```python
from collections import namedtuple

Point = namedtuple('点',['x', 'y'])
a = Point(1,5)  # 这里只能传2个参数
print(a)
# Out: 点(x=1, y=5)

print(a.x)
# Out: 1

# 为namedtupe 赋予默认值
Point = namedtuple('点',['x', 'y'])
Field.__new__.__defaults__ = (0, 0)
Field.__new__.__defaults__ = (0,) # 如果赋值的数量少于原有数量，则会从右往左进行赋值。 在这里是将y属性赋值为0
```



## functools

### partial

```python
functools.partial(func[,*args][, **kwargs])
```

用来对函数func的某些参数进行默认设置。

```python
def multiply(x, y):
    return x * y

double = functools.partial(multiply, y=2)

double(5)
# Out: 10
```





## 时间相关

Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。还有datetime模块

### time

time.time() 返回一个时间戳（浮点数），代表从1970-01-01 00:00:00 到现在经过了多少秒。

```python
import time

time.time()
# Out[5]: 1585811480.8246994
```

time.localtime()，可以接受一个时间戳（默认为当前时间），返回一个时间元组，如下图所示：

```python
time.localtime()
# Out[6]: time.struct_time(tm_year=2020, tm_mon=4, tm_mday=2, tm_hour=15, tm_min=13, tm_sec=28, tm_wday=3, tm_yday=93, tm_isdst=0)
```

（年，月，日，时，分，秒，一周的第几天（0是周一），一年中的第几天，是否是夏令时）

dst：夏令时（Daylight Saving time）

**格式化输出时间：**

```python
time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# Out[7]: '2020-04-02 15:15:20'
```

### datetime

引入datetime：

```python
# datetime是一个模块，在里面有一个类叫datetime
from datetime import datetime
```

获取当前时间：

```python
datetime.now()
# Out[9]: datetime.datetime(2020, 4, 2, 15, 17, 33, 188997)
```

格式化时间：

```python
datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# Out[10]: '2020-04-02 15:19:27'
```

获取本月第一天和最后一天：

```python
import calendar
import datetime
from datetime import timedelta

this_month_start = datetime.datetime(now.year, now.month, 1)
this_month_end = datetime.datetime(now.year, now.month, calendar.monthrange(now.year, now.month)[1])
```



## logging

级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG

debug : 打印全部的日志,详细的信息,通常只出现在诊断问题上

info : 打印info,warning,error,critical级别的日志,确认一切按预期运行

warning : 打印warning,error,critical级别的日志,一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”),这个软件还能按预期工作

error : 打印error,critical级别的日志,更严重的问题,软件没能执行一些功能

critical : 打印critical级别,一个严重的错误,这表明程序本身可能无法继续运行



典型的日志记录的步骤是这样的：

1. 创建logger
2. 创建handler（用于写入日志文件，或输出到控制台）
3. 定义formatter（定义handler的输出格式（formatter））
4. 给handler添加formatter
5. 给logger添加handler



fmt：

```
%(name)s            Name of the logger (logging channel)
%(levelno)s         Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL)
%(levelname)s       Text logging level for the message ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")
%(pathname)s        Full pathname of the source file where the logging call was issued (if available)
%(filename)s        Filename portion of pathname
%(module)s          Module (name portion of filename)
%(lineno)d          Source line number where the logging call was issued (if available)
%(funcName)s        Function name
%(created)f         Time when the LogRecord was created (time.time() return value)
%(asctime)s         Textual time when the LogRecord was created
%(msecs)d           Millisecond portion of the creation time
%(relativeCreated)d Time in milliseconds when the LogRecord was created, relative to the time the logging module was loaded
(typically at application startup time)
%(thread)d          Thread ID (if available)
%(threadName)s      Thread name (if available)
%(process)d         Process ID (if available)
%(message)s         The result of record.getMessage(), computed just as the record is emitted
```



```python
import logging

# 1、创建一个logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

# 2、创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')
fh.setLevel(logging.DEBUG)

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 3、定义handler的输出格式（formatter）
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 4、给handler添加formatter
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 5、给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)
```



## yaml

python使用yaml：

```python
import yaml

f = open('cfg.yaml', 'rt', encoding='utf8')   # ? rt模式下，python在读取文本时会自动把\r\n转换成\n.
cfg = yaml.load(f_cfg)
        
s = """
s: hello
li: 
 - 1
 - 黄钢
"""
yaml.load(s)
# {'s': 'hello', 'li': [1, '黄钢']}
```

主要有3种类型：

- 对象：键值对的集合
- 数组：一组按次序排列的值，又称为序列（sequence） / 列表（list）
- 纯量（scalars）：单个的、不可再分的值
  - 字符串
  - 布尔值：`isSet: true` 或 `isSet: True`
  - 整数
  - 浮点数
  - Null：`parent: ~ ` 或 `parent: null `
  - 时间
  - 日期

注意：

- 大小写敏感
- 使用缩进表示层级关系
- 缩进时不允许使用Tab键，只允许使用空格。
- 缩进的空格数目不重要，只要相同层级的元素左侧对齐即可



强制转换类型：`isTrue: !!str True`



引用 与解耦：

```yaml
defaults: &defaults
  adapter:  postgres
  host:     localhost

development:
  database: myapp_development
  <<: *defaults

"""
{'defaults': {'adapter': 'postgres', 'host': 'localhost'},
 'development': {
  'adapter': 'postgres',
  'host': 'localhost',
  'database': 'myapp_development'
  }
}
"""
```
















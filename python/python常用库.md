# python常用库

[TOC]

<!-- toc -->

---

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


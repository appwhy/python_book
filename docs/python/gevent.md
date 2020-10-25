# gevent

[TOC]

<!-- toc -->

---

gevent是一个基于libev的并发库。它为各种并发和网络相关的任务提供了整洁的API。

```python
from gevent import monkey
monkey.patch_all()
import gevent

def func():
    pass

gevent.spawn(func)

gevent.joinall([
    gevent.spawn(func),
    gevent.spawn(func),
])
```


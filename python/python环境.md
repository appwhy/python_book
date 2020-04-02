# python环境

[TOC]

<!-- toc -->

---

## python编辑器

在windows上，安装python后会自带IDLE编辑器，能用，但一般般。

集成开发一般用PyCharm，功能十分强大。

## python交互

### python

最简单的方式是直接执行python命令，会启动一个python命令行，可以执行相关代码。但是该方式操作有些不方便。

### ipython

功能介绍：

* Tab补全
* func?：快速查询文档，相当于`help(func)`。
* !shell_cmd：在shell命令前加上感叹号，直接执行shell命令，无需退出ipython。

魔术方法（以%开头）：

* `%run python_file_path`：运行py文件。
* `%time func()`：查看func函数的运行时间。
* `%lsmagic`：列出所有魔术方法。



### jupyter

jupyter是一种交互式计算和开发环境的笔记，支持多语言，输出图形、音频、视频等功能。

安装：

```bash
pip3 install jupyter
```

启动：

```bash
jupyter notebook  # 启动一个web服务，用于交互。是基于ipython的
```



#### 配置多个内核

一般情况下，我安装了jupyter之后，只有一个python环境。比如，我是使用python3启动的jupyter notebook，我就只能使用python3。但我想使用python2怎么办呢？使用如下方法：

首先，要有python2的环境，假设`python2`启动的是python2相关的环境。

```bash
python2 -m pip install ipykernel   # 安装 IPython Kernel for Jupyter
python2 -m ipykernel install       # 将该python2的ipython内核添加进jupyter配置中
```

此时就能使用python2和python3两个环境了。

查看jupyter的ipython内核：

```bash
jupyter kernelspec list

# 输出
Available kernels:
  python3    C:\ProgramData\Anaconda3\lib\site-packages\ipykernel\resources
  python2    C:\ProgramData\jupyter\kernels\python2
```



有时为避免冲突，需要指定唯一的名称

```bash
python -m ipykernel install --name myenv --display-name 'py27"
```

  --name 是给jupyter 启动Kernel 使用（是`jupyter kernelspec list`显示在前面的name，如果指定的name已存在则会覆盖。--display-name 是为Jupyter notebook 菜单显示。

#### 搭建 jupyter notebook 服务

首先在linux上安装好python及相应的包，然后进行下面的操作。

编辑配置文件：/root/.jupyter/jupyter_notebook_config：（当前用户关于jupyter的配置文件）

如果没有，就先生成：

```bash
jupyter notebook --generate-config
```

修改配置：

```
c.NotebookApp.allow_remote_access = True
c.NotebookApp.ip = '*'
c.NotebookApp.password = 'sha1:xxx:xxx'
```

自己设置一个密码：

```python
# 启动ipython

from notebook.auth import passwd
passwd()
```

将生成的'sha1:xxx:xxx'写入到配置文件中的 c.NotebookApp.password 项中。

后台启动jupyter botebook，并将日志写入指定文件：

```
nohup jupyter notebook --allow-root &>jupyter.log &
```



设置nginx代理：

```
server {
    listen  80;
    server_name python.opstar.club;
    
    proxy_http_version  1.1;
    proxy_set_header    Upgrade $http_upgrade;
    proxy_set_header    Connection "upgrade";
    
    proxy_redirect  off;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Is-EDU 0;
    
    location / {
        proxy_pass http://127.0.0.1:8888;
    }
    
    error_page 404 /404.html;
    location = /404.html {
    }
    
    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
    }
}
```

重启nginx服务：

```bash
systemctl restart nginx.service 
```

nginx日志存放在： /var/log/nginx/access.log

### ipython与jupyter的关系

ipython最初是一个python的交互式解释器，随着ipython的不断发展，它的组件与具体的编程语言逐渐解耦。IPython 3.x 是IPython的最后一个独立发行版，包含了notebook服务器、qtconsole等。

从IPython 4.0 开始，项目中与语言无关的部分：the notebook format、 message protocol、 qtconsole、notebook web application 等都转移到了新的项目中，并命名为Jupyter。

而IPython本身专注于交互式Python，其中一部分是为Jupyter提供Python内核。

## python 虚拟环境


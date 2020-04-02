# python环境

[TOC]

<!-- toc -->

---

## python编辑器



集成开发一般用PyCharm。

## python交互

### python

最简单的方式是直接执行python命令，会启动一个python命令行，可以执行相关代码。但是该方式操作有些不方便。

### ipython



### jupyter notebook





#### 配置多个内核



#### 搭建 jupyter notebook 服务

首先在linux上安装好python及相应的包，然后进行下面的操作。

编辑配置文件：/root/.jupyter/jupyter_notebook_config：

如果没有，就先生成：

```
jupyter notebook --generate-config
```

```
c.NotebookApp.allow_remote_access = True
c.NotebookApp.ip = '*'
```



自己设置一个密码：

```
ipython

> from notebook.auth import passwd
> passwd()
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

```
nginx -s reload
```

nginx日志：

/var/log/nginx/access.log

## python 虚拟环境


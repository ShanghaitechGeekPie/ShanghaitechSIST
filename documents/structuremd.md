# Chapter 1 基本结构

##结构说明

整体站点构建在Python Django 1.8.6的Python 3版本上，使用django的基本框架、Django_CMS框架以及部分Django_CMS官方插件。

##安装

安装Python3(ubuntu)

```
apt-get install python3 python3-pip
```

安装Django

```
pip3 install 'django==1.8.6'
```

安装Django_CMS

```
pip install django-cms
```

安装插件

```
pip3 install djangocms-text-ckeditor
pip3 install djangocms-picture
pip3 install djangocms-file
```

安装数据库支持

数据库连接使用Django官方的连接模块，可以任意选择Django支持的数据库postgresql、mysql、sqlite3、oracle等，可能需要对特定的服务器安装特定的组件，具体查阅Django官方文档。

源代码默认状态使用sqlite3。

##配置

核心配置文件位于shanghaitech_SIST/settings.py，内部内容说明参见注释，Django官方文档及Django_CMS官方文档。

##数据库

数据库连接使用Django官方的连接模块，可以任意选择Django支持的数据库postgresql、mysql、sqlite3、oracle等，可能需要对特定的服务器安装特定的组件，具体查阅Django官方文档。

##目录结构


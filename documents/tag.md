# Chapter 4 tag扩展

Tag 和 Filter概念与运作机制，详见Django官方文档。

##涉及代码

* shanghaitech_SIST
	* templatetags
		* __init__.py Python模块标记文件
		* sist_tags.py Tag逻辑文件

##ShowPlaceholderByIdwithAS

###Tag注册关键字

show_placeholder_as

###简介

提取指定页面的指定Placeholder渲染之后的内容并存储在指定模板变量中。

主逻辑继承Django-CMS的ShowPlaceholderById，可参考相关文档。

###用法

```
show_placeholder_as placeholder_name page_lookup language site as varname
```
参数
```
placeholder_name 必选 placeholder名称
page_lookup 必选 placeholder名称
language 必选 placeholder名称
site 必选 placeholder名称
as 关键字
varname 必选 placeholder名称


        Argument('placeholder_name'),
        Argument('reverse_id'),
        Argument('lang', required=False, default=None),
        Argument('site', required=False, default=None),
        'as',
        Argument('varname', required=False, resolve=False),
```
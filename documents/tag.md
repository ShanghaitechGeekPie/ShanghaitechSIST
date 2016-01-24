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
show_placeholder_as [placeholder_name] [page_lookup] [language] [site] as [varname]
```
参数
```
placeholder_name 必选 placeholder名称
page_lookup 必选 请看Django-CMS API关于page_lookup页面定位的描述
language 可选 语言，默认为和当前渲染语言一致
site 可选 站点，默认只有一个站点不需要填写
as 关键字
varname 必选 渲染结果存储在前端变量varname中
```

###实例


* templates
	* menu
		* home_news_menu.html
		* 

```
{% show_placeholder_as "article_content" child.id as article_content %}
<div class="col-md-12 home-news-block clickbox" href="{{ child.attr.redirect_url|default:child.get_absolute_url }}">
	<h4>{{ child.get_menu_title }}</h4>
	<p>{{ article_content | striptags | truncatechars:300 }}</p>
</div>
```

##Paginate

###Tag注册关键字

Paginate

###简介

各种分页插件。

###用法

```
Paginate [request] [container] maxitem [maxitem] maxmenuitem [maxmenuitem] page [page] key [key] as [varname]
```
参数
```
request 必选 Django request对象，一般只需要在模板传递request对象即可
container 必选 需要被分页的数据，一般为一个list集合
maxitem 关键字
maxitem 可选 每页显示多少个，默认为30
maxmenuitem 关键字
maxmenuitem 可选 页码选择器最多显示多少个，默认为10
page 关键字
page 可选 当前页号，默认从request.GET中解析
key 关键字
key 可选 request.GET中页号关键字，默认为'paginate_id'
as 关键字
varname 必选 渲染结果存储在前端变量varname中
```

###实例


* templates
	* menu
		* home_news_menu.html
		* 

```
{% show_placeholder_as "article_content" child.id as article_content %}
<div class="col-md-12 home-news-block clickbox" href="{{ child.attr.redirect_url|default:child.get_absolute_url }}">
	<h4>{{ child.get_menu_title }}</h4>
	<p>{{ article_content | striptags | truncatechars:300 }}</p>
</div>
```






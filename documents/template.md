# Chapter 5 前端页面模板

前端页面模板主要依照的是Django对于Template的定义，详细内容参考DJango官方文档。

##主要前端约定

###变量渲染

模板渲染是会有一些变量，在前端可以使用如下代码取得变量值。

```
{{ attr }}
{{ attr.attr }}字典属性查找/函数调用
```

###变量过滤器

变量数据渲染的时候可以使用一些内置的filter，filter也可以带有一定的变量，允许自定义filter，参考官方文档。

```
{{ attr | filter:arg }}
{{ ship_date | date:"F j, Y" }} 格式化日期
{{ attr | lower | truncatewords:"30" }} 转为小写后截取前30个字
```

###逻辑块

逻辑块可以理解为一些内置的语句。

```
{% cmd %}
```

####逻辑块 if

接受逻辑运算，接受==, !=, <, >, <=, >= and in 判断，逻辑运算中and优先于or。else可选。建议不做复杂判断。

```
{% if attr %}
    {{ attr }}
{% else %}
    {{ attr2 }}
{% endif %}

{% if attr or attr2 %}
    {{ attr }}
{% else %}
    {{ attr2 }}
{% endif %}

{% if not attr == 1 and attr2 > 2 %}
    {{ attr }}
{% else %}
    {{ attr2 }}
{% endif %}
```

####逻辑块 ifequal & ifnotequal

字面意义，if的一种shortcut。


```
{% ifequal attr attr2 %}
    {{ attr }}
{% else %}
    {{ attr2 }}
{% endifequal %}
```

####逻辑块 for


类Python循环，不接受计数器循环。empty可选，当被循环对象不存在或为空时触发。循环内存在forloop循环状态变量。

```
{% for item in list %}
    {{ item.name }}
{% endfor %}

{% for item in list %}
    {{ item.name }}
{% empty %}
    There is no item.
{% endfor %}

{% for key, value in data.items %}
    {{ key }}: {{ value }}
{% endfor %}

{% for item in list %}
    {{ item.name }}
    {% if not forloop.first %}、{% endif %}
{% endfor %}
```


##涉及代码

* templates
	* article.html
	* home.html
	* list.html
	* list_news.html
	* list_overview.html
	* list_seminars.html
	* people.html
	* root.html
	* root_with_right_menu.html
	* seminars.html

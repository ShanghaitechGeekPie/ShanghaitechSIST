# Chapter 6 前端菜单模板

前端菜单页面模板主要依照的是Django对于Template的定义，由Django-CMS的menu模块负责处理。详细内容参考DJango和Django-CMS官方文档。

##主要前端约定

菜单模板提供一个基本的children对象，对象内为menu的具体内容。对每一个children对象的子对象，提供对象的基本参数，部分函数接口，可以结合page_lookup和id属性取得页面对象，继而使用tag扩展访问页面对象内容。

##前端页面列表

前端页面均位于templates/menu目录，下面列出的顺序为由继承定义的页面继承关系。

* root.html 根节点，定义了基本的页面样式，基本页面结构，公共header部分，渲染页面标题。
    * home.html 主页，重载root的root_body。
	* root_with_right_menu.html 分栏根节点，重载root的root_body，定义了左右分栏的页面结构，右分栏定义为一级节点的目录，左分栏定义为空。
    	* list.html 基本列表页面，重载root_with_right_menu的root_with_right_menu_body。
        	* list_news.html 新闻列表页面，重载list的list_body,修改列表项显示方式为新闻+新闻简介的样式。
        	* list_seminars.html 讲座列表页面，重载list的list_body,修改列表项显示方式为讲座+讲座时间的样式。
        	* list_overview.html 总览列表页面，重载list的list_body,修改列表项显示方式为一级加二级标题的样式。
    	* article.html 基本文章页面，重载root_with_right_menu的root_with_right_menu_body，可编辑文章内容。
        	* people.html 人员文章页面，重载article的article_content，可独立编辑个人信息。
        	* seminars.html 讲座文章页面，重载article的article_content，可独立编辑讲座信息。

##涉及代码

* templates
	* menu
		* home_news_menu.html
		* home_seminars_menu.html
		* language_chooser.html
		* list_menu.html
		* list_news_menu.html
		* list_overview_inner_menu.html
		* list_overview_menu.html
		* list_seminars_menu.html
		* root_menu.html
		* root_with_right_menu_menu.html

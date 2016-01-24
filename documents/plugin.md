# Chapter 3 plugin扩展

Plain概念与运作机制，详见Django-CMS官方文档

##PlainText原始文本插件

###涉及代码

* djangocms_plaintext
	* __init__.py Python模块标记文件
	* admin.py Admin注册文件（未使用）
	* cms_plugins.py 插件逻辑代码
	* models.py 数据库模型定义
	* templates 插件模板
		* cms
			* plugins
				* plaintext_plugin.html
	* tests.py 测试文件（未使用）
	* views.py 视图文件（未使用）
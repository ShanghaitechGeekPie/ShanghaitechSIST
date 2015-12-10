#coding=utf-8

from django.db import models
import hashlib

class Article(models.Model):
	"""System instruction article"""
	abstract=models.TextField(verbose_name='文章摘要',blank=True)
	content=models.TextField(verbose_name='文章内容',blank=True)
	time=models.DateTimeField(verbose_name='发表时间',blank=False,auto_now_add=True)

	def GetAbstract(self):
		return(self.abstract_zh)
	def GetContent(self):
		return(self.content_zh)

class Point(models.Model):
	"""System instruction point"""
	name=models.CharField(max_length=255,verbose_name='节点名称',blank=True)
	template=models.CharField(max_length=255,verbose_name='渲染模板',blank=False)
	url=models.CharField(max_length=255,verbose_name='URL段',blank=False)
	view=models.BooleanField(verbose_name='View',blank=False,default=False)
	parent=models.ForeignKey('self',verbose_name='上级节点',null=True,blank=True)
	foreignkey_article=models.ForeignKey(Article,verbose_name='文章对象',null=True,blank=True)
	type=models.IntegerField(verbose_name='节点类型',choices=(
		(0,'普通分支节点'),
		(2,'文章节点'),
		(3,'链接节点'),))
	def GetName(self,lang='ZH'):
		if (lang=='ZH'):
			return(self.name)
	def GetType(self,lang='ZH'):
		if (lang=='ZH'):
			return({
				0:'普通分支节点',
				2:'文章节点',
				3:'链接节点',
			}[self.type])
	def GetView(self,lang='ZH'):
		if (lang=='ZH'):
			if self.view:
				return('是')
			else:
				return('否')
	def GetChildNodes(self):
		return(Point.objects.filter(parent=self))
	def GetChildKeyNodes(self):
		return(Point.objects.filter(parent=self,type=0))
	def __unicode__(self):
		return(self.name_zh)
	def __str__(self):
		return(self.name_zh)
  

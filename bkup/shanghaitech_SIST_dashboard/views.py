from django.shortcuts import render,render_to_response,Http404
from django.http import HttpResponse
from shanghaitech_SIST_db.models import *
import simplejson

def GetKeyNodes(request):
	if request.GET.get('id',None) and int(request.GET.get('id',None)):
		node_parent=Point.objects.get(id=request.GET['id'])
		nodes_array=node_parent.GetChildKeyNodes()
		response_nodes_array=[{'id':node.id,'pID':node.parent.id,'name':node.name,'isParent':bool(node.GetChildKeyNodes())} for node in nodes_array]
		return HttpResponse(
			simplejson.dumps(response_nodes_array,ensure_ascii=False))
	else:
		nodes_array=Point.objects.filter(parent=None,type=0)
		response_nodes_array=[{'id':node.id,'pID':0,'name':node.name,'isParent':bool(node.GetChildKeyNodes())} for node in nodes_array]
		return HttpResponse(
			simplejson.dumps(response_nodes_array,ensure_ascii=False))

def GetNodes(request):
	if request.GET.get('id',None) and int(request.GET.get('id',None)):
		node_parent=Point.objects.get(id=request.GET['id'])
		nodes_array=node_parent.GetChildNodes()
		response_nodes_array=[[node.GetName(),node.url,node.GetType(),node.GetView(),'Manage'] for node in nodes_array]
		return HttpResponse(
			simplejson.dumps(response_nodes_array,ensure_ascii=False))
	else:
		nodes_array=Point.objects.filter(parent=None)
		response_nodes_array=[[node.GetName(),node.url,node.GetType(),node.GetView(),'Manage'] for node in nodes_array]
		return HttpResponse(
			simplejson.dumps(response_nodes_array,ensure_ascii=False))
		

def datacontrol(request):
	procedure_list={
		'GetKeyNodes':GetKeyNodes,
		'GetNodes':GetNodes,
		}
	if request.method=='GET':
		return(procedure_list[request.GET['request']](request))
	return HttpResponse('''
		[
	{id:1, pId:0, name: "父节点1"},
	{id:11, pId:1, name: "子节点1"},
	{id:12, pId:1, isParent:true, name: "子节点2"}
]
''')

def url_redirect(request,url):
	url_md5=url#hashlib.md5(url.encode("utf8")).hexdigest()
	url_point=get_or_http404(Point,full_url=url_md5)
	if url_point.type == 1:
		return render_to_response(url_point.template.address+'/list.html', {})
	elif url_point.type == 2:
		return render_to_response(url_point.template.address+'/article.html', {
			'point':url_point,
			})
	elif url_point.type == 3:
		pass
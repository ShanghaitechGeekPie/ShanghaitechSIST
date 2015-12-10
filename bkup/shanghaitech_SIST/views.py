#coding=utf-8

from django.shortcuts import render,render_to_response,Http404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import hashlib
from shanghaitech_SIST_db.models import *

def get_or_http404(handle, *args, **kwargs):
    try:
        return handle.objects.get(*args, **kwargs)
    except:
        raise Http404('No %s matches the given query or multiple objects are returned.' % handle.objects.model._meta.object_name)

# Create your views here.
@csrf_exempt
def a(request):
	if request.method=='POST':
		return HttpResponse('''
<response>
	<return>
		<status>200</status>
		<message>NONE</message>
	</return>
	<data>
		<id>20140125</id>
		<name>张三</name>
		<school>山东蓝翔高级技工学校</school>
		<register>
			<status>1</status>
			<time>2015-05-02 11:55:25</time>
			<group>A</group>
			<room>R201</room>
		</register>
	</data>
</response>
''')
	return HttpResponse("GET Hello world")

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
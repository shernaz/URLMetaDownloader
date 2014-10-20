from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from umd.models import URL
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

def index(request):

	url_list = URL.objects.order_by('url') [:5]
	'''a= "<b>hello world.. </b></br>"
	url_list = URL.objects.order_by('url') [:5]
	output = ', '.join([p.url for p in url_list])
	return HttpResponse (a + output );
	
	template = loader.get_template('umd/index.html')
	context = RequestContext(request, {
	'url_list': url_list,
	})
	return HttpResponse(template.render(context))
	
	'''
	
	context = {'url_list': url_list}
	return render(request, 'umd/index.html', context)
	
	
def detail(request, url_id):
	'''
	try:
		url = URL.objects.get(pk=url_id)
	except URL.DoesNotExist:
		raise Http404
	return render(request, 'umd/detail.html', {'url': url})
	'''
	u = get_object_or_404(URL, pk=url_id)
	return render(request, 'umd/detail.html', {'url': u})
# Create your views here.

def modify(request, url_id):
	
	p = get_object_or_404(URL, pk=url_id)
	p.url=request.POST['url']
	p.title=request.POST['title']
	p.meta_desc=request.POST['meta_desc']
	p.meta_keyword=request.POST['meta_keyword']
	p.save()
	return HttpResponseRedirect(reverse('detail', args=(p.id,)))
	#return HttpResponseRedirect(reverse('detail'))
	#render(request, 'umd/detail.html', {'url': url})
	
def add(request):
	return HttpResponse("Add")
	
	'''a= "<b>hello world.. </b></br>"
	url_list = URL.objects.order_by('url') [:5]
	output = ', '.join([p.url for p in url_list])
	return HttpResponse (a + output );
	
	template = loader.get_template('umd/index.html')
	context = RequestContext(request, {
	'url_list': url_list,
	})
	return HttpResponse(template.render(context))
	'''
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from umd.models import URL
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from umd.forms import URLForm

def index(request):

	url_list = URL.objects.order_by('url')
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
	return render(request, 'umd/base.html', context)
	
	
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
	
	return render(request, 'umd/add.html')
	
def add_url(request):
	
	url = request.POST['url']
	title = request.POST['title']
	meta_desc = request.POST['meta_desc']
	meta_keyword = request.POST['meta_keyword']
	
	p = URL(url = url, title = title, meta_desc = meta_desc, meta_keyword = meta_keyword)
	p.save()

	url_list = URL.objects.order_by('url') 
	context = {'url_list': url_list}
	return HttpResponseRedirect('/umd/')

	#return render(request, 'umd/index.html', context)
	
	'''
	if request.method == 'POST':
		form = URLForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'umd/index.html')
		else:
			messages.error(request, "Error")
	return render(request, 'umd/addurl.html' , {'form': URLForm()})

	url = request.POST['url']
	title = request.POST['title']
	meta_desc = request.POST['meta_desc']
	meta_keyword = request.POST['meta_keyword']
	
	p = URL (url = url, title = title, meta_desc = meta_desc, meta_keyword = meta_keyword)
	p.save()

	return HttpResponseRedirect(reverse('add_url'))
	
	
	a= "<b>hello world.. </b></br>"
	url_list = URL.objects.order_by('url') [:5]
	output = ', '.join([p.url for p in url_list])
	return HttpResponse (a + output );
	
	template = loader.get_template('umd/index.html')
	context = RequestContext(request, {
	'url_list': url_list,
	})
	return HttpResponse(template.render(context))
	'''
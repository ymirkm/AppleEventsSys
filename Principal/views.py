from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Imagen
from django.core.mail import send_mail

def home(request):
	return render(request, 'index.html')

def contact(request):
	return render(request, 'contact.html')

def about(request):
	return render(request, 'about.html')

def blog(request):
	return render(request, 'blog_main.html')

def linenIndex(request):
	return render(request, 'linen_index.html')

def chairIndex(request):
	return render(request, 'chair_index.html')

def chevronDetail(request):
	db = Imagen.objects.filter(kind='chevron')
	return render(request, 'chevron_detail.html', {'dic': db})

def fortunyDetail(request):
	db = Imagen.objects.filter(kind='fortuny')
	return render(request, 'fortuny_detail.html', {'dic': db})

def galaxyDetail(request):
	db = Imagen.objects.filter(kind='galaxy')
	return render(request, 'galaxy_detail.html', {'dic': db})

def noveltyDetail(request, page=0):
	db = Imagen.objects.filter(kind='novelty')
	paginator = Paginator(db, 16);
	print "Pagina: " + str(page) 
	try:
		images = paginator.page(page)
	except PageNotAnInteger:
		images = paginator.page(1)
	except EmptyPage:
		images = paginator.page(paginator.num_pages)
	return render(request, 'novelty_detail.html', {'dic': images})

def organzaDetail(request):
	db = Imagen.objects.filter(kind='organza')
	return render(request, 'organza_detail.html', {'dic': db})

def pintuckDetail(request):
	db = Imagen.objects.filter(kind='pintuck')
	return render(request, 'pintuck_detail.html', {'dic': db})

def satinDetail(request):
	db = Imagen.objects.filter(kind='satin')
	return render(request, 'satin_detail.html', {'dic': db})

def serviceLaundry(request):
	return render(request, 'service_laundry.html')
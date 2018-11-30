from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import TambahFoto_Form,Profil_Edit_Form
from .models import Gallery_Foto,Profil
from django.contrib.auth import logout

def logout_views(request):
    logout(request)
    return HttpResponseRedirect('/dashboard/')


def dashboard(request):
	form = TambahFoto_Form(request.POST,request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		print(obj)
		obj.save()
		return HttpResponseRedirect('/dashboard/')

	template = 'admin_rjf/tambah_gallery.html'
	context = {'form':form}

	return render(request, template, context)
def login(request):
	form = TambahFoto_Form(request.POST,request.FILES or None)

	if form.is_valid():
		obj = form.save(commit=False)
		print(obj)
		obj.save()
		return HttpResponseRedirect('list_gallery/')

	template = 'admin_rjf/tambah_gallery.html'
	context = {'form':form}
	return render(request, template, context)
def list_gallery(request):
	images = Gallery_Foto.objects.all()

	backdrop = Gallery_Foto.objects.filter(kategori='backdrop')
	meja_meeting = Gallery_Foto.objects.filter(kategori='meja_meeting')
	bedroom = Gallery_Foto.objects.filter(kategori='bedroom')
	front_office = Gallery_Foto.objects.filter(kategori='front_office')
	rak = Gallery_Foto.objects.filter(kategori='Rak')
	tangga = Gallery_Foto.objects.filter(kategori='tangga')
	template = 'admin_rjf/list_gallery.html'


	context = {
		'backdrop':backdrop,		
		'foto':bedroom,
		'meja_meeting':meja_meeting,
		'front_office':front_office,
		'rak':rak,
		'tangga':tangga,
		'images':images
		}
	return render(request, template, context)
def hapus_foto(request,list_gallery_id):
	objectnya =  Gallery_Foto.objects.get(id=list_gallery_id)
	
	objectnya.delete()	

	return HttpResponseRedirect('/dashboard/')

def profil_edit(request, id=None):
    obj = get_object_or_404(Profil, id=id)
    form = Profil_Edit_Form(request.POST or None, instance=obj)
	    
    context = {
        "form": form
    }
    if form.is_valid():
    	form = Profil_Edit_Form(request.POST,request.FILES or None, instance=obj)
    	obj = form.save(commit=True)
    	print(obj)
    	obj.save()
    	return HttpResponseRedirect('/dashboard/')
    template = "admin_rjf/edit2.html"
    return render(request, template, context)

def buat_profil(request):
	form = Profil_Edit_Form(request.POST,request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		print(obj)
		obj.save()
		return HttpResponseRedirect('/dashboard/')
	else:
		form = Profil_Edit_Form()

	template = 'admin_rjf/buat_profil.html'
	context = {
         "form": form
    }

	


	return render(request, template, context)







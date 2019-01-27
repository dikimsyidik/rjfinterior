from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from admin_rjf.models import Gallery_Foto,Profil
from admin_rjf.forms import FormKomentar

def index(requset):
	backdrop = Gallery_Foto.objects.filter(kategori='backdrop')
	kitchen_set = Gallery_Foto.objects.filter(kategori='kitchen set')
	ruang_keluarga = Gallery_Foto.objects.filter(kategori='ruang_keluarga')
	galery = Gallery_Foto.objects.all()


	meja_meeting = Gallery_Foto.objects.filter(kategori='meja_meeting')
	bedroom = Gallery_Foto.objects.filter(kategori='bedroom')
	front_office = Gallery_Foto.objects.filter(kategori='front_office')
	rak = Gallery_Foto.objects.filter(kategori='rak')
	tangga = Gallery_Foto.objects.filter(kategori='tangga')

	profil = Profil.objects.all()

	template = 'basic/index.html'
	context = {
		'backdrop':backdrop,		
		'foto':bedroom,
		'kitchen_set':kitchen_set,
		'ruang_keluarga':ruang_keluarga,
		'meja_meeting':meja_meeting,
		'front_office':front_office,
		'rak':rak,
		'tangga':tangga,
		'profil':profil,
		}
	for g in galery:
		print(g)
	print(galery.filter(kategori='rak'))
	print(rak)
	return render(requset,template,context)
def tentang_kami(requset):
	backdrop = Gallery_Foto.objects.filter(kategori='backdrop')
	meja_meeting = Gallery_Foto.objects.filter(kategori='meja_meeting')
	bedroom = Gallery_Foto.objects.filter(kategori='bedroom')
	front_office = Gallery_Foto.objects.filter(kategori='front_office')
	rak = Gallery_Foto.objects.filter(kategori='Rak')
	tangga = Gallery_Foto.objects.filter(kategori='tangga')
	profil = Profil.objects.all()


	
	template = 'basic/about.html'
	context = {
		'backdrop':backdrop,		
		'foto':bedroom,
		'meja_meeting':meja_meeting,
		'front_office':front_office,
		'rak':rak,
		'tangga':tangga,
		'profil':profil,
		
		}
	print(type(rak))
	print(bedroom)

	return render(requset,template,context)
def gallery(requset):
	backdrop = Gallery_Foto.objects.filter(kategori='backdrop')
	kitchen_set = Gallery_Foto.objects.filter(kategori='kitchen set')
	ruang_keluarga = Gallery_Foto.objects.filter(kategori='ruang_keluarga')
	galery = Gallery_Foto.objects.all()


	meja_meeting = Gallery_Foto.objects.filter(kategori='meja_meeting')
	bedroom = Gallery_Foto.objects.filter(kategori='bedroom')
	front_office = Gallery_Foto.objects.filter(kategori='front_office')
	rak = Gallery_Foto.objects.filter(kategori='rak')
	tangga = Gallery_Foto.objects.filter(kategori='tangga')

	profil = Profil.objects.all()

	template = 'basic/index.html'
	context = {
		'backdrop':backdrop,		
		'foto':bedroom,
		'kitchen_set':kitchen_set,
		'ruang_keluarga':ruang_keluarga,
		'meja_meeting':meja_meeting,
		'front_office':front_office,
		'rak':rak,
		'tangga':tangga,
		'profil':profil,
		}	
	template = 'basic/gallery.html'
	
	print(type(rak))
	print(bedroom)

	return render(requset,template,context)
def contact(request):
	backdrop = Gallery_Foto.objects.filter(kategori='backdrop')
	meja_meeting = Gallery_Foto.objects.filter(kategori='meja_meeting')
	bedroom = Gallery_Foto.objects.filter(kategori='bedroom')
	front_office = Gallery_Foto.objects.filter(kategori='front_office')
	rak = Gallery_Foto.objects.filter(kategori='Rak')
	tangga = Gallery_Foto.objects.filter(kategori='tangga')
	form = FormKomentar(request.POST or None)



		
	template = 'basic/contact.html'
	profil = Profil.objects.all()


	if form.is_valid():
		obj = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/')



	context = {
		'backdrop':backdrop,		
		'foto':bedroom,
		'meja_meeting':meja_meeting,
		'front_office':front_office,
		'rak':rak,
		'tangga':tangga,
		'profil':profil,
		'form':form,
		}

	print(type(rak))
	print(bedroom)

	return render(request,template,context)

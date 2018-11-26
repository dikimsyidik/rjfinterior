from django.contrib import admin

# Register your models here.
from .models import Testimoni,Kontak,Produk_Unggulan,Gallery_Foto




admin.site.register(Testimoni)
admin.site.register(Kontak)
admin.site.register(Produk_Unggulan)
admin.site.register(Gallery_Foto)
from django import forms


from .models import Gallery_Foto

class TambahFoto_Form(forms.ModelForm):
    class Meta:
        model = Gallery_Foto
        fields = [
            'produk',
            'post_thumbnail',
            'kategori',
       
        ]
        widgets = {
            'produk': forms.TextInput(attrs={'class': 'form-control','name':'Nama'}),
            'kategori': forms.Select(attrs={'class': 'form-control'}),
            'post_thumnail':forms.FileInput(attrs={'class':'form-control'}),
        }

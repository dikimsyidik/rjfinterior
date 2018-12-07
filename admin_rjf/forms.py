from django import forms
from django.contrib.auth import authenticate,get_user_model

from .models import Gallery_Foto,Profil


User = get_user_model()

class LoginForm(forms.Form):

	username = forms.CharField(label='username')
	password = forms.CharField(label='password',widget=forms.PasswordInput)

	def clean(self,*args,**kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		user_obj = User.objects.filter(username=username).first()

		if not user_obj:
			raise forms.ValidationError("invalid username")
		else:
			if not user_obj.check_password(password):
				raise forms.ValidationError("invalid username")
		return super(LoginForm,self).clean(*args,**kwargs)

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
class Profil_Edit_Form(forms.ModelForm):
	class Meta:
		model = Profil
		fields = [
            'foto_perusahaan',
            'deskripsi_perusahaan',
            'foto1',
            'nama_produk',
            'deskripsi_produk',
            
            'foto2',
			'nama_produk2',
			'deskripsi_produk2', 
			
			'foto3',
			'nama_produk3',
			'deskripsi_produk3',
			
			'nama_dan_pekerjaan',
			'project_dan_asal',
			'komentar',
			
			'nama_dan_pekerjaan2',
			'project_dan_asal2',
			'komentar2',
			
			'nama_dan_pekerjaan3',
			'project_dan_asal3',
			'komentar3',
			
			'alamat',
			'no_hp',
			'whatsapp',
			'email',
			
			'facebook',
			'twitter',
			'instagram',
			'google_plus',
        ]
		widgets = {
        # 'foto_perusahaan':forms.FileInput(attrs={'class': 'fileupload','required':'False','name':'fileupload'}),

		# 'deskripsi_perusahaan':forms.Textarea(attrs={'class': 'form-control','placeholder':'Deskripsi Perusahaan'}),
	 # 	'foto1':forms.FileInput(attrs={'class': 'fileupload','name':'fileupload'}),
        
		# 'nama_produk':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama Produk'}),
  #    	'deskripsi_produk':forms.Textarea(attrs={'class': 'form-control','placeholder':'Deskripsi'}),
  #       'foto2':forms.FileInput(attrs={'class': 'fileupload','name':'fileupload'}),
		# 'nama_produk2':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama Produk'}),
		# 'deskripsi_produk2':forms.Textarea(attrs={'class': 'form-control','placeholder':'Deskripsi'}),
		# 'foto3':forms.FileInput(attrs={'class': 'fileupload','name':'fileupload'}),
		# 'nama_produk3':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama Produk'}),
		# 'deskripsi_produk3':forms.Textarea(attrs={'class': 'form-control','placeholder':'Deskripsi'}),
		# 'nama_dan_pekerjaan':forms.TextInput(attrs={'class': 'form-control','placeholder':'Contoh : isna , Wiraswasta'}),
		# 'project_dan_asal':forms.TextInput(attrs={'class': 'form-control','placeholder':'Contoh : Kitchen set ,Rumah'}),
		# 'komentar':forms.Textarea(attrs={'class': 'form-control','placeholder':'Komentar'}),
		# 'nama_dan_pekerjaan2':forms.TextInput(attrs={'class': 'form-control','placeholder':'Contoh : isna , Wiraswasta'}),
		# 'project_dan_asal2':forms.TextInput(attrs={'class': 'form-control','placeholder':'Contoh : Kitchen set ,Rumah'}),
		# 'komentar2':forms.Textarea(attrs={'class': 'form-control','placeholder':'Komentar'}),
		# 'nama_dan_pekerjaan3':forms.TextInput(attrs={'class': 'form-control','placeholder':'Contoh : isna , Wiraswasta'}),
		# 'project_dan_asal3':forms.TextInput(attrs={'class': 'form-control','placeholder':'Contoh : Kitchen set ,Rumah'}),		
		# 'komentar3':forms.Textarea(attrs={'class': 'form-control','placeholder':'Komentar'}),
		# 'alamat':forms.TextInput(attrs={'class': 'form-control','name':'Nama'}),
		# 'no_hp':forms.TextInput(attrs={'class': 'form-control','name':'Nama'}),
		# 'whatsapp':forms.TextInput(attrs={'class': 'form-control','name':'Nama'}),
		# 'email':forms.EmailInput(attrs={'class': 'form-control','name':'Nama'}),
		# 'facebook':forms.TextInput(attrs={'class': 'form-control','id':'k6','placeholder':'http://'}),
		# 'twitter':forms.TextInput(attrs={'class': 'form-control','id':'k6','placeholder':'http://'}),
		# 'instagram':forms.TextInput(attrs={'class': 'form-control','id':'k6','placeholder':'http://'}),
		# 'google_plus':forms.TextInput(attrs={'class': 'form-control','id':'k6','placeholder':'http://'}),
		}
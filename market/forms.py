
from django import forms
from market.models import Blog

class BlogUpdate(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body']

class BlogForm(forms.ModelForm) :
    class Meta : # Meta 클래스
        model = Blog
        fields = ['title', 'body']

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__' #Blog 클래스 안에 있는 모든 객체 대상
        #fields = ['title', 'body'] #특정 데이터 대상
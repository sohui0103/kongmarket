from django.shortcuts import render, redirect, get_object_or_404
from market.models import *
from market.forms import BlogForm

#메인화면
def home(request):
    return render(request, 'home.html')

#중고거래
def market(request):
    return render(request, 'market.html')
    # blogs = Blog.objects.order_by('-id')
    # blog_list = Blog.objects.all().order_by('-id')
    # paginator = Paginator(blog_list,3)
    # page = request.GET.get('page')
    # posts = paginator.get_page(page)
    # return render(request,'market.html', {'blogs':blogs,'posts':posts})  

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'detail.html',{'blog': blog_detail})

def create(request):
    if(request.method == 'POST'):
        blog = Blog()
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.save()
    return redirect('/')

def search(request):
    blogs = Blog.objects.all().order_by('-id')

    q = request.POST.get('q', "")

    if q:
        blogs = blogs.filter(title__icontains=q)
        return render(request, 'search.html',{'blogs' : blogs, 'q' : q})
    
    else:
        return render(request, 'search.html')

def delete(request, blog_id):
    delete_post = get_object_or_404(Blog, pk=blog_id)
    delete_post.delete()
    return redirect('market.html')

def update(request, blog_id):
    post = Blog.objects.get(id=blog_id)
    # 글을 수정사항을 입력하고 제출을 눌렀을 때
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            # {'name': '수정된 이름', 'image': <InMemoryUploadedFile: Birman_43.jpg 	(image/jpeg)>, 'gender': 'female', 'body': '수정된 내용'}
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('/detail/'+str(post.pk))
        
    # 수정사항을 입력하기 위해 페이지에 처음 접속했을 때
    else:
        form = BlogForm()
        return render(request, 'update.html',{'form':form})



#약속
def promise(request):
    return render(request, 'promise.html')

#채팅방
def chat(request):
    return render(request, 'chat.html')
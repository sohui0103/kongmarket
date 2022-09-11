from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User



# 회원가입 
def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username = request.POST["username"], password = request.POST["password1"]
            )
            auth.login(request, user)
            return redirect('home')
        return render(request, 'signup.html')
    return render(request, 'signup.html')

#로그인
def login(request):
    #POST 요청이 들어오면 로그인 처리 해줌
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None: #존재하는 회원이면
            auth.login(request, user) #로그인
            return redirect('home')
        else: #존재하지 않는 회원이면
            return render(request, 'login.html', {'error':'username or password is incorrect'})
        

    #GET 요청이 들어오면 login form을 담고있는 login.html을 띄워줌
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
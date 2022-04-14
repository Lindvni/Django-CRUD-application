from django.shortcuts import render

 
# Create your views here.

def login(request):
    if request.method =='POST':
        username =request.POST['username']
        password =request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
    else:
            return render(request,'login.html')

def reg(request):
    if request.method=='POST':
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        username =request.POST['username']
        email =request.POST['email']
        password1 =request.POST['password1']
        password2 =request.POST['password2']

        
        user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)    
        user.save();
        print('user created')
        return redirect('/')
    else: 
       
        return render(request,'reg.html')

def logout(request):
    auth.logout(request)
    return redirect('/')




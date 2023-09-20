from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .models import ChatModel
from django.contrib.auth import login , authenticate
# Create your views here.

def index(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'chat/index.html', context={'users': users})

def chatPage(request , username):
    user_obj = User.objects.get(username = username)
    users = User.objects.exclude(username=request.user.username)
    
    if request.user.id > user_obj.id:
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
    else:
        thread_name = f'chat_{user_obj.id}-{request.user.id}'
    
    message_obj = ChatModel.objects.filter(thread_name = thread_name)
    return render(request, 'chat/main_chat.html', context={'users': users , 'user' : user_obj , 'messages' : message_obj})
    
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username = username , password = password)
        if user is not None:
            login(request , user)
            return redirect('index')
    return render(request , 'chat/login.html')

def register(request):
    return render(request , 'chat/register.html')
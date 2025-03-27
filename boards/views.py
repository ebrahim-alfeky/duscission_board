from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from django.urls import reverse
from .models import Post,Topic,Board
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime
current_date = datetime.now().date()
from .form import*
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.

#! her link   in url of discussion_boards 
def home(request):
    username=request.GET.get('username')
    profile=User.objects.filter(username=username).first()
    if profile:
        boards=Board.objects.filter(created_by=profile)
        topics=Topic.objects.filter(created_by=profile)
        posts=Post.objects.filter(created_by=profile)
        my_variables1={
            'boards':boards,
            'topics':topics,
            'posts':posts,
            'profile':profile
        }
        return render(request,'accounts/profile.html',my_variables1)
    return render(request,'boards/home.html')
    
    
def show_boards(request):
    boardss = Board.objects.all()
    numm=boardss.count()
    page=request.GET.get('page',1)
    paginator=Paginator(boardss,3)
    boardss=paginator.get_page(page)
    id = request.GET.get('id')
    board = Board.objects.filter(id=id).first()
    if board:
        return render(request,'boards/oneBoard.html',{'my_board':board})
    
    username=request.GET.get('username')
    profile=User.objects.filter(username=username).first()
    if profile:
        boards=Board.objects.filter(created_by=profile)
        topics=Topic.objects.filter(created_by=profile)
        posts=Post.objects.filter(created_by=profile)
        my_variables1={
            'boards':boards,
            'topics':topics,
            'posts':posts,
            'profile':profile
        }
        return render(request,'accounts/profile.html',my_variables1)
    my_variables= {'boards': boardss,'num':numm}
    return render(request, 'boards/boards.html',my_variables )
    
@login_required
def add_board(request):
    form = Board1()
    if request.method == "POST":
        #!الريكويست عباره عن ديكشانرى
        data={
            "name":request.POST.get('name'),
            "description":request.POST.get('description'),
            "created_by":request.user.id
        }
        form = Board1(data)
        if form.is_valid():
            form.save()
            return redirect("boards") 

    return render(request, 'boards/add_board.html', {'form': form})  

@login_required
def update_board(request, id):
    board=Board.objects.filter(id=id).first()
    if board:
        if board.created_by==request.user:
            if request.method == "POST":
                name = request.POST.get("name")
                description = request.POST.get("description")
                
                if name:
                    board.name = name
                if description:
                    board.description = description
                
                board.save()
                return redirect('boards')
        else:
            return render(request,"boards/didn't_add.html")
    
    return render(request, 'boards/update_board.html', {'board': board})


def show_topic(request):
    topicss = Topic.objects.all().order_by('-created_date')
    numm = topicss.count()
    page = request.GET.get('page', 1)
    paginator = Paginator(topicss, 3)
    topicss=paginator.get_page(page)
    id=request.GET.get('id')
    topic=Topic.objects.filter(id=id).first()
    if topic:
        return render(request,'boards/oneTopic.html',{'my_topic':topic})

    username=request.GET.get('username')
    profile=User.objects.filter(username=username).first()
    if profile:
        boards=Board.objects.filter(created_by=profile)
        topics=Topic.objects.filter(created_by=profile)
        posts=Post.objects.filter(created_by=profile)
        my_variables1={
            'boards':boards,
            'topics':topics,
            'posts':posts,
            'profile':profile
        }
        return render(request,'accounts/profile.html',my_variables1)
    
    
    my_variables = {'topics': topicss, 'num': numm}
    return render(request, 'boards/topic.html', my_variables)
   

@login_required
def add_topic(request):
    form = Topic1()
    if request.method == "POST":
        form = Topic1(request.POST)
        if form.is_valid():
            topic=form.save(commit=False)
            topic.created_by=request.user
            topic.save()
            return redirect("topics") 
    return render(request, 'boards/add_topic.html', {'form': form})  

@login_required
def update_topic(request,id):
    topic=Topic.objects.filter(id=id).first()
    if topic:
        if topic.created_by==request.user:
            if request.method=="POST":
                en_subject=request.POST['subject']
                en_board=request.POST['board']
                en_board=Board.objects.get(name=en_board)
                if en_subject:
                    topic.subject=en_subject
                if en_board:
                    topic.board=en_board
                    topic.save()
                    return redirect ('topics')
            boards=Board.objects.all()
        else:
            return render(request,"boards/didn't_add.html")
        
    return render (request,'boards/update_topic.html',{'boards':boards,'topic':topic})

def show_post(request):
    postss=Post.objects.all().order_by('-created_date')
    numm=postss.count()
    
    
    page=request.GET.get('page',1)
    paginator=Paginator(postss,3)
    postss=paginator.get_page(page)
    
    
    id=request.GET.get('id')
    post=Post.objects.filter(id=id).first()
    if post:
        return render(request,'boards/onePost.html',{'my_post':post})
    
    
    username=request.GET.get('username')
    profile=User.objects.filter(username=username).first()
    if profile:
        boards=Board.objects.filter(created_by=profile)
        topics=Topic.objects.filter(created_by=profile)
        posts=Post.objects.filter(created_by=profile)
        my_variables1={
            'boards':boards,
            'topics':topics,
            'posts':posts,
            'profile':profile
        }
        return render(request,'accounts/profile.html',my_variables1)
    
    
    my_variables={'posts':postss,'num':numm}
    return render(request,'boards/post.html',my_variables)  

@login_required
def add_post(request):
    form = Post1()
    if request.method == "POST":
        form = Post1(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.created_by=request.user
            post.save()
            return redirect("posts")     

    return render(request, 'boards/add_post.html', {'form': form})  

@login_required
def update_post(request,id):
    post=Post.objects.filter(id=id).first()
    if post:
        if post.created_by==request.user:
            if request.method=='POST':
                en_message=request.POST['message']
                en_topic=request.POST['topic']
                en_topic=Topic.objects.get(subject=en_topic)
                if en_message:
                    post.message=en_message
                if en_topic:
                    post.topic=en_topic
                    post.save()
                    return redirect ('posts')
            topics=Topic.objects.all()
        else:
            return render(request,"boards/didn't_add.html")
        
    return render (request,'boards/update_post.html',{'topics':topics,'post':post})




def all(request):
    boards=Board.objects.all()
    my_variables={'boards':boards}
    
    board_id=request.GET.get('board_id')
    board=Board.objects.filter(id=board_id).first()
    topics=Topic.objects.filter(board=board)
    if topics:
        my_variables['topics']=topics
    
    topic_id=request.GET.get('topic_id')
    topic=Topic.objects.filter(id=topic_id).first()
    posts=Post.objects.filter(topic=topic)
    if posts:
        my_variables['posts']=posts
    
    return render(request,'boards/all.html',my_variables)
    
    
from django.shortcuts import render, HttpResponse,  redirect,get_object_or_404
from .forms import PostForm, UserRegistrationForm
from .models import Post , Comment
from  django.contrib.auth.decorators import login_required
from django.contrib.auth import login




# Create your views here.

def index(request):
    # return HttpResponse("dskjgndkjsgnk")
    return render(request, 'index.html')
# @login_required
# def post_list(request):    
    # posts = Post.objects.all().order_by('-created_at')
    # return render(request, 'post_list.html',{'posts':posts})
# @login_required
def post_list(request):
    posts = Post.objects.prefetch_related('comments').all().order_by('-created_at')
   
    # print(posts)
    # for post in posts:
    #   print(f"Post Title: Created At: {post.created_at}")
    #   comments = post.comments.all()  # Access the related comments for this post
    #   for comment in comments:
    #     print(f"  Comment: {comment.content}, Created At: {comment.created_at}")
       
    
    return render(request, 'post_list.html', {'posts': posts})
   

@login_required
def post_created(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})


@login_required
def post_edit(request,post_id):
    post = get_object_or_404(Post, pk = post_id, user =request.user )
    if request.method == 'POST':              
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()  
            return redirect('post_list')      
            
    else:
        form = PostForm(instance=post)    
    return render(request, 'post_form.html',{'form':form})



@login_required
def post_delete(request,post_id):
    post = get_object_or_404(Post, pk = post_id, user =request.user )
    if request.method == 'POST':
 
        post.delete()
        return redirect('post_list')
    # return render(request, 'tweet_confirm_delete.html',{'post':post})

     
def register(request):
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            # login(register, user)
            return redirect('post_list')
    else:
            form = UserRegistrationForm()
        
    return render(request, 'registration/register.html',{'form':form})
        

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(post=post, user=request.user, content=content)
    return redirect('post_list')


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.user:  # Only allow the comment owner to edit
        if request.method == 'POST':
            content = request.POST.get('content')
            if content:
                comment.content = content
                comment.save()
    return redirect('post_list')

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.user:  # Only allow the comment owner to delete
        if request.method == 'POST':
            comment.delete()
    return redirect('post_list')


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_list')  # Adjust this if you redirect to a different view




@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user in comment.likes.all():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)
    return redirect('post_list')  # Adjust this if you redirect to a different view



    
    
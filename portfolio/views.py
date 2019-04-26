from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Person
from .forms import PersonForm

# Create your views here.
def home(request):
    posts = Person.objects
    return render(request, 'portfolio/home.html', {'posts':posts})
def detail(request, post_id):
    post_detail = get_object_or_404(Person, pk= post_id)
    return render(request, 'portfolio/detail.html',{'post': post_detail})
def post_new(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if  form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.datetime.now()
            post.save()
            return redirect('detail', post_id=post.pk)
    else:
        form = PersonForm()
        return render(request, 'portfolio/new.html/',{'form':form})

def post_edit(request, post_id):
    post=get_object_or_404(Person, pk=post_id)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=post)
        if  form.is_valid():
            post = form.save(commit=False)
            post.published_data = timezone.datetime.now()
            post.save()
            return redirect('detail', post_id=post.pk)
    else:
        form = PersonForm(instance=post)
        return render(request, 'portfolio/new.html/',{'form':form})
def post_delete(request,post_id):
    post=get_object_or_404(Person,pk=post_id)
    post.delete()
    return redirect('home')
    
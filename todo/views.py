from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages

# import todo form and models

from .forms import TodoForm
from .models import Todo
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout  # Import Django's login function


###############################################


def index(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)


### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save user if form is valid
            return redirect("login")  # Redirect to login page after signup
    else:
        form = UserCreationForm()  # Show empty form

    return render(request, "registration/login.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Correct usage of Django's login function
            return redirect('/main/')

    else:
        form = AuthenticationForm()

    return render(request, 'registration\login.html', {'form': form})


@login_required
def main(request):
    return render(request, "todo\main.html")


def landingpage(request):
    return render(request, "todo\landingpage.html")


def logout_user(request):
    logout(request)
    messages.success(request, "log out now redirecting")
    return redirect('landing-page')  # Ensure this matches the correct route

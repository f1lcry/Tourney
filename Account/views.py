from django.shortcuts import render
from .forms import LoginForm, RegistrationForm, EditAccountForm
from django.contrib import auth
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse


def index(request):
    title = "Profile"

    context = {
        'title': title,
    }
    return render(request, 'Account/index.html', context)


def user_games(request):
    title = "User's games"
    games = {}
    for game in request.user.get_games():
        games.update({game: game.is_user_winner(request)})

    context = {
        'title': title,
        'games': games,
    }
    return render(request, 'Account/user_games.html', context)


def login(request):
    form = LoginForm(data=request.POST)
    title = "Login"

    if request.method == "POST" and form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse("home"))

    context = {
        "title": title,
        "form": form,
    }
    return render(request, "Account/login.html", context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("home"))


def registration(request):
    # TODO: Hide fields requirements
    # TODO: Make a field where user need to choose preferred game modes
    title = "Registration"
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home"))
    else:
        form = RegistrationForm()
    context = {
        "title": title,
        "form": form
    }
    return render(request, "Account/register.html", context)


def edit_account(request):
    title = "Edit account"
    if request.method == "POST":
        form = EditAccountForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("profile"))
    else:
        form = EditAccountForm(instance=request.user)
    context = {
        "title": title,
        "form": form
    }
    return render(request, "Account/edit_account.html", context)


from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import HomeModel, AboutModel, MenuModel, contacModel, OrderModel
from django.core.paginator import Paginator


# Create your views here.


def Home(request):
    HomeModelPage = HomeModel.objects.all()
    if request.method == 'GET':
        st = request.GET.get('name')
        if st != None:
            HomeModelPage = HomeModel.objects.filter(name__icontains=st)
    HomeParams = {'HomeModelPage': HomeModelPage}
    return render(request, 'Home.html', HomeParams)


def DishesPage(request):
    dishModel = HomeModel.objects.all()
    if request.method == 'GET':
        st = request.GET.get('name')
        if st != None:
            dishModel = HomeModel.objects.filter(name__icontains=st)
    P = Paginator(dishModel, 3)
    pageNumber = request.GET.get('page')
    dishDataFinal = P.get_page(pageNumber)
    totalpage = dishDataFinal.paginator.num_pages
    dishesDataParams = {'dishModel': dishDataFinal, 'lastpage': totalpage,
                         'totalPageNumber': [n + 1 for n in range(totalpage)]}
    return render(request, 'Dishes.html', dishesDataParams)


def aboutPage(request):
    aboutModel = AboutModel.objects.all()
    aboutParams = {'aboutModel': aboutModel}
    return render(request, 'about.html', aboutParams)


def MenuPage(request):
    menuModel = MenuModel.objects.all()
    if request.method == 'GET':
        st = request.GET.get('name')
        if st != None:
            menuModel = HomeModel.objects.filter(name__icontains=st)
    menuParams = {'menuModel': menuModel}
    return render(request, 'Menu.html', menuParams)


def contactUs(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        number = request.POST.get("number")
        address = request.POST.get("address")
        query = request.POST.get("query")
        contactData = contacModel(name=name, number=number, address=address, Query=query)
        contactData.save()
        messages.info(request, " Your Query Has Been submitted Successfully ")
    return render(request, 'contactUs.html')


def orderPage(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        number = request.POST.get("number")
        foodName = request.POST.get("foodName")
        food = request.POST.get("food")
        quantity = int(request.POST.get("quantity"))
        DateTime = request.POST.get("DateTime")
        address = request.POST.get("address")
        message = request.POST.get("message")
        if name is None:
            messages.error(request, "Name field Can not be Empty")
        elif message is None:
            messages.error(request, "message field Can not be Empty")
        else:
            order = OrderModel(name=name, number=number, foodName=foodName, AdditionalFood=food, myDate=DateTime, address=address, message=message, quantity=quantity)
            order.save()
            messages.error(request, "Order Has been Submitted Successfully! Thanks")
    return render(request, 'order.html')


def ReadMorePage(request, slug):
    More = HomeModel.objects.get(Home_slug=slug)
    return render(request, 'ReadMore.html', {'More': More})


def registerPage(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        Cpassword = request.POST['Cpassword']
        if password == Cpassword:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, "user Name Exist")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Exist")
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=user_name, email=email, password=password)
                user.save()
                return redirect('/LoginPage')
        else:
            messages.error(request, "password is not matching")
    return render(request, 'register.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, " Successfully User Logged In")
            return redirect("/")
        else:
            messages.info(request, "Invalid Credential")
    return render(request, 'MyLogin.html')


def LogoutPage(request):
    auth.logout(request)
    return redirect('/')


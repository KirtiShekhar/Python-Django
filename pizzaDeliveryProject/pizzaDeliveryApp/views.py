from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import PizzaModel,CustomerModel,PizzasOrderModel

# Create your views here.
def welcomepageview(request):
    return render(request,"pizzaDelivery/pizzaswelcome.html")

def adminloginview(request):
    return render(request,"pizzaDelivery/adminlogin.html")

def authenticateadmin(request):
    adminusername = request.POST['adminusername']
    adminpassword = request.POST['adminpassword']

    admin = authenticate(username = adminusername,password = adminpassword)

    # admin exist
    if admin is not None and admin.username=="Admin":
        login(request,admin)
        return redirect('adminhomepageview')

    # admin exist
    if admin is None:
        messages.add_message(request, messages.ERROR, "invalid credentials")
        return redirect('adminloginview')

def adminhomepageview(request):
    pizzasContext = {'pizzas' : PizzaModel.objects.all()}
    return render(request,"pizzaDelivery/admindashboard.html",pizzasContext)

def adminlogoutview(request):
    logout(request)
    return redirect('adminloginview')

def addPizzas(request):
    # write a code to add the pizzas entered by user in the database
    pizzaName = request.POST['pizzaName']
    pizzaPrice = request.POST['pizzaPrice']
    PizzaModel(pizzaName = pizzaName,pizzaPrice = pizzaPrice).save()
    return redirect('adminhomepageview')

def deletePizzas(request,pizzaspk):
    # write a code to add the pizzas entered by user in the database
    PizzaModel.objects.filter(id = pizzaspk).delete()
    return redirect('adminhomepageview')

def customerhomepageview(request):
    return render(request,"pizzaDelivery/customerdashboard.html")

def customersignup(request):
    # write a code to signup a application for a customer
    username = request.POST['username']
    password = request.POST['password']
    contactNumber = request.POST['contactNumber']
    emailAddress = request.POST['emailAddress']

    # if customer username already exists
    if User.objects.filter(username = username).exists():
        messages.add_message(request,messages.ERROR,"user already exist")
        return redirect('customerhomepageview')

    # if customer username does not already exist (everything is fine to register the customer)
    User.objects.create_user(username=username,password=password).save()
    lastObject = len(User.objects.all())-1
    CustomerModel(customerId = User.objects.all()[int(lastObject)].id,emailAddress = emailAddress,contactNumber = contactNumber).save()
    messages.add_message(request,messages.ERROR,"user succesfully registered")
    return redirect('customerhomepageview')

def customersignin(request):
    # write a code to signin a application for a customer
    return render(request,"pizzaDelivery/customerlogin.html")

def authenticatecustomer(request):
    # write a code to authenticate the customer
    customerusername = request.POST['customerusername']
    customerpassword = request.POST['customerpassword']

    customer = authenticate(username=customerusername, password=customerpassword)

    # admin exist
    if customer is not None:
        login(request,customer)
        return redirect('customerwelcomepageview')

    # admin exist
    if customer is None:
        messages.add_message(request, messages.ERROR, "invalid credentials")
        return redirect('customersignin')

def customerwelcomepageview(request):
    username = request.user.username
    customerContext = {'customerName':username,'pizzas' : PizzaModel.objects.all()}
    return render(request,"pizzaDelivery/customerwelcome.html",customerContext)

def customerlogout(request):
    # write a code for a customer to logout
    return redirect('customersignin')

def placepizzasorder(request):
    if not request.user.is_authenticated:
        return redirect('customersignin')

    customerUsername = request.user.username
    customerContactNumber = CustomerModel.objects.filter(customerId = request.user.id)[0].contactNumber
    customerAddress = request.POST['address']
    PizzasOrderedItems = ""
    for pizza in PizzaModel.objects.all():
        pizzaId = pizza.id
        pizzaName = pizza.pizzaName
        pizzaPrice = pizza.pizzaPrice

        pizzaQuantity = request.POST.get(str(pizzaId)," ")




        if str(pizzaQuantity)!="0" and str(pizzaQuantity)!=" ":
            PizzasOrderedItems = PizzasOrderedItems + pizzaName+" " + "price : " + str(int(pizzaQuantity)*int(pizzaPrice)) +" "+ "quantity : "+ pizzaQuantity+"    "

    print(PizzasOrderedItems)

    PizzasOrderModel(customerUsername = customerUsername,customerContactNumber = customerContactNumber,customerAddress = customerAddress,PizzasOrderedItems = PizzasOrderedItems).save()
    messages.add_message(request,messages.INFO,"pizza order succesfully placed")
    return redirect('customerwelcomepageview')


def customerpizzasorder(request):
    PizzasOrdered = PizzasOrderModel.objects.filter(customerUsername = request.user.username)
    PizzasOrderedContext = {'PizzasOrdered':PizzasOrdered}
    return render(request,'pizzaDelivery/customerpizzasorder.html',PizzasOrderedContext)

def adminpizzasorder(request):
    PizzasOrdered = PizzasOrderModel.objects.all()
    PizzasOrderedContext = {'PizzasOrdered':PizzasOrdered}
    return render(request,'pizzaDelivery/adminpizzasorder.html',PizzasOrderedContext)


def acceptpizzasorder(request,pizzaorderpk):
    pizzaAcceptOrders = PizzasOrderModel.objects.filter(id = pizzaorderpk)[0]
    pizzaAcceptOrders.customerStatus = "accepted"
    pizzaAcceptOrders.save()
    return redirect(request.META['HTTP_REFERER'])


def declinedpizzasorder(request,pizzaorderpk):
    pizzaAcceptOrders = PizzasOrderModel.objects.filter(id=pizzaorderpk)[0]
    pizzaAcceptOrders.customerStatus = "declined"
    pizzaAcceptOrders.save()
    return redirect(request.META['HTTP_REFERER'])
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecords
from .models import Customer
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
	customers = Customer.objects.all()

	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('home')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('home')
	else:
		return render(request, 'myapp/home.html', {'customers':customers})
	



def login_user(request):
    pass
    #return render(request, 'myapp/login.html')


def logout_user(request):
	logout(request)
	messages.success(request, 'You have been logged out')
	return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if  form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {user_name}. You can now login')
            return redirect('home')
    else:
        form = SignUpForm()
    context = {
        "form":form
    }
    return render(request, 'myapp/register.html', context)


def customer_records(request, pk):
	if request.user.is_authenticated:
		customer_record = Customer.objects.get(id = pk)
		return render(request, 'myapp/customer.html', {'customer_record':customer_record})
	else:
		messages.success(request, 'You must Login to view the Customer Record')
		return redirect('home')

@login_required(login_url='home')
def delete(request, pk):
	items = Customer.objects.get(id =pk)
	if request.method == 'POST':
		items.delete()
		messages.success(request, f' {items} has been delete successfully!')
		return redirect('home')
	else:
		return render(request, 'myapp/delete.html', {'items':items})      

@login_required(login_url='home')
def AddCustomer(request):
	if request.method =="POST":
		form = AddRecords(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Customer has been added successfully')
			return redirect('home')
		
	else:
		form = AddRecords()
	return render(request, 'myapp/add_record.html', {'form':form})


@login_required(login_url='home')
def UpdateCustomer(request, pk):
	item = Customer.objects.get(id=pk)
	if request.method =="POST":
		form = AddRecords(request.POST, instance=item)
		if form.is_valid():
			form.save()
			messages.success(request, 'Customer record has been updated successfully')
			return redirect('home')
		
	else:
		form = AddRecords(instance=item)
	
	return render(request, 'myapp/update.html', {'form':form})
    
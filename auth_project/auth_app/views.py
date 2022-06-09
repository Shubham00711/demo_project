from django.shortcuts import redirect, render
from django.views import View
from .forms import CustomerRegistrationForm
from django.contrib import messages

def home(request):
    if request.user.is_authenticated:
        return render(request, 'app/main.html')
    return render(request, 'app/home.html')

def main(request):
    if request.user.is_authenticated:
        return render(request, 'app/main.html')
    return redirect('home')

class UserRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/userregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'app/userregistration.html', {'form': form})
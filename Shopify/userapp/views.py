from django.shortcuts import render, redirect
from django.views import View
from userapp.forms import CustomUserCreationForm

class UserRegisterView(View):
    def get(self, request, role):
        context = {
            'form': CustomUserCreationForm()
        }
        return render(request, 'userapp/register.html', context)

    def post(self, request, role):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if role == 'seller':
                instance.is_seller = True
            elif role == 'buyer':
                instance.is_buyer = True
            instance.save()
            
        return redirect('shopify:home')
       




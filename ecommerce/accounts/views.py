from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout





def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully. You can now login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})




# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('product-list')
#             # next_url = request.GET.get('next', '/')
#             # return redirect(next_url) 
#         else:
#             messages.error(request, 'Invalid credentials')
#         return render(request, 'accounts/login.html')



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Redirect to next page if exists
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)

            return redirect('/')  # Redirect home after login

        messages.error(request, "Invalid username or password")
        return render(request, 'accounts/login.html')

    # GET request → show login page
    return render(request, 'accounts/login.html')















def user_logout(request):
    logout(request)
    return redirect('product-list')

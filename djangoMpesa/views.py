from django.shortcuts import render, redirect

def paypage(request):
    return render(request, "payments.html")

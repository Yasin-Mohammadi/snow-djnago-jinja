from django.shortcuts import render, get_object_or_404
from .models import Blog, Portfolio

# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    return render(request, "home.html", {"blogs": blogs})

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, "blog.html", {"blogs": blogs})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, "blog_detail.html", {"blog": blog})

def portfolio_list(request):
    portfolios = Portfolio.objects.all()
    return render(request, "portfolio.html", {"portfolios": portfolios})

def portfolio_detail(request, id):
    portfolio = get_object_or_404(Portfolio, id=id)
    return render(request, "portfolio_detail.html", {"portfolio": portfolio})
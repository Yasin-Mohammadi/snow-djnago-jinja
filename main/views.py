from django.shortcuts import render, get_object_or_404
from .models import Blog, Portfolio, Contact
from django.contrib import messages
from .forms import ContactForm

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
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save to database
            messages.success(request, "Your message has been sent successfully!")
            form = ContactForm()  # Reset the form

    return render(request, "portfolio_detail.html", {"portfolio": portfolio, "form": form})


import threading

from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewsForms, UserLoginForm
from .models import News, Categories


def add_news(request, set_up_cloud=None):
    if request.method == 'POST':
        form = NewsForms(request.POST, request.FILES)
        if form.is_valid():
            form_instance = form.save()  # Formani oldin saqlaymiz

            video_file = request.FILES.get("video")  # ✅ get() ishlatilmoqda

            if video_file and set_up_cloud:  # ✅ set_up_cloud tekshirilmoqda
                thread = threading.Thread(target=set_up_cloud, args=(video_file, form_instance))
                thread.start()

            messages.success(request, "OK, saqlandi!")
            return redirect('home')  # Asosiy sahifaga qaytish

    else:
        form = NewsForms()

    return render(request, 'news/add_news.html', {'form': form})
def about_new(request,new_id):
    new=get_object_or_404(News,id=new_id)
    if request.method== 'POST':
        form=NewsForms(request.POST,instance=new)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=NewsForms(instance=new)
    return render(request,'news/about_new.html',{'form':form,'new':new})


def delete(request, new_id):
    new = get_object_or_404(News, id=new_id)  # Yangilik mavjudligini tekshiramiz

    if new:  # Agar yangilik topilsa
        new.delete()
        messages.success(request, "Yangilik muvaffaqiyatli o‘chirildi!")  # Muvaffaqiyatli xabar
        return redirect('home')

    else:
        messages.error(request, "Yangilik topilmadi yoki o‘chirib bo‘lmadi!")  # Xato xabar

    return redirect('home')
#





def index(request):
    query = request.GET.get('q', '')  # Qidiruv so‘rovini olish
    news = News.objects.all()  # Barcha yangiliklarni olish
    categories = Categories.objects.all()  # Kategoriyalarni olish

    if query:
        news = news.filter(title__icontains=query)  # Foydalanuvchi kiritgan so‘zga mos yangiliklarni chiqarish

    context = {
        "news": news,
        "categories": categories,
        "query": query  # Qidiruv maydonida yozilgan matnni saqlash
    }
    return render(request, 'news/index.html', context=context)


#
def category(request, id):
    category = get_object_or_404(Categories, id=id)  # Kategoriya mavjudligini tekshirish
    news = News.objects.filter(category=category)  # Ushbu kategoriyaga tegishli yangiliklarni olish

    context = {
        "news": news,
        "category": category,  # Template ichida foydalanish uchun nomni aniqroq qildik
    }
    return render(request, 'news/category.html', context)

#

def loginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            return redirect('home')
    else:
        form =UserLoginForm()
    return render(request,'news/login.html',{'form':form})

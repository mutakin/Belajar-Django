from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'judul':'Blog Kelas Terbuka',
        'subjudul':'Selamat Datang',
        'banner':'blog/img/banner_blog.png'
    }
    return render(request,'index.html',context)
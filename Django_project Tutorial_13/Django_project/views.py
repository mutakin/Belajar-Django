from django.shortcuts import render


def index(request):
    context = {
        'titile':'Kelas Terbuka',
        'heading':'Selamat Datang',
        'subheading':'Di kelas terbuka',
    }
    return render(request,'index.html',context)
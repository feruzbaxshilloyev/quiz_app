from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from profil.models import CustomUser
from .models import Category, Baza, Test
from .forms import TestSolveForm, BazaForm
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()


def home(request):
    user = request.user
    categories = Category.objects.all().prefetch_related('baza_set')
    return render(request, 'home.html', {'categories': categories, 'user': user})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def baza_detail(request, id):
    baza = get_object_or_404(Baza, id=id)
    tests = baza.test_set.all()
    total = tests.count()

    baza.views += 1
    baza.save()

    return render(request, 'detail.html', {
        'baza': baza,
        'total': total
    })


@csrf_exempt
def submit_answer(request):
    if request.method == 'POST':
        user = get_object_or_404(CustomUser, id=request.user.id)
        test_id = request.POST.get('test_id')
        user_answer = request.POST.get('answer')

        try:
            test = Test.objects.get(id=test_id)
        except Test.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Test topilmadi.'})

        user.total_quiz += 1
        correct = False
        if user_answer == test.true_var:
            user.true_quiz += 1
            correct = True

        user.save()

        return JsonResponse({
            'status': 'ok',
            'correct': correct,
            'true_answer': test.true_var
        })

    return JsonResponse({'status': 'error', 'message': 'Noto‘g‘ri metod'})


def add_baza(request, id):
    user = get_object_or_404(CustomUser, id=request.user.id)
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST' and user:
        form = BazaForm(request.POST)
        if form.is_valid():
            baza = form.save(commit=False)
            baza.author = user
            baza.category = category
            baza.t_count = 0
            baza.views = 0
            category.baza_count += 1
            category.save()
            baza.save()

            return redirect('app:baza_detail', id=baza.id)
    else:
        form = BazaForm()
    return render(request, 'add_baza.html', {'form': form})


def bazalar_view(request):
    categories = Category.objects.all()
    bazalar = Baza.objects.select_related('category', 'author').all().order_by('-views')
    return render(request, 'bazalar.html', {'categories': categories, 'bazalar': bazalar})


@login_required
def add_test(request, id):
    baza = get_object_or_404(Baza, id=id)

    if request.method == 'POST':
        savol = request.POST.get('savol')
        image = request.FILES.get('image')
        a = request.POST.get('a')
        b = request.POST.get('b')
        c = request.POST.get('c')
        d = request.POST.get('d')
        true_var = request.POST.get('true_var')
        times = request.POST.get('times')

        times = int(times) if times and times.isdigit() else 60

        Test.objects.create(
            baza=baza,
            savol=savol,
            image=image,
            a=a,
            b=b,
            c=c,
            d=d,
            true_var=true_var.lower(),
            times=times
        )
        return redirect('app:baza_detail', id=baza.id)

    return render(request, 'add_test.html', {'baza': baza})


def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Category.objects.create(name=name)
            return redirect('app:home')
    return render(request, 'add_ctg.html')


@csrf_exempt
def submit_answer(request):
    if request.method == 'POST':
        user = get_object_or_404(CustomUser, id=request.user.id)
        test_id = request.POST.get('test_id')
        user_answer = request.POST.get('answer')

        try:
            test = Test.objects.get(id=test_id)
        except Test.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Test topilmadi.'})

        user.total_quiz += 1
        correct = False
        if user_answer.lower() == test.true_var.lower():
            user.true_quiz += 1
            correct = True
            print(correct)

        user.save()

        return JsonResponse({
            'status': 'ok',
            'correct': correct,
            'true_answer': test.true_var
        })

    return JsonResponse({'status': 'error', 'message': 'Noto‘g‘ri metod'})


def delete_baza(request, id):
    baza = get_object_or_404(Baza, id=id)
    if request.user == baza.author:
        baza.delete()
    return redirect('profil:my_tests')

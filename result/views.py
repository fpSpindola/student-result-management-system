from django.shortcuts import render, redirect
from .forms import ResultForm
from .models import Result


def add_result(request):
    form = ResultForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('result_list')

    return render(request, 'add_result.html', {'form': form})


def result_list(request):
    results = Result.objects.all()
    return render(request, 'result_list.html', {'results': results})
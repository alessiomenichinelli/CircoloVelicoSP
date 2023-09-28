from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Barca, Proprietario, Uscita
from .forms import UscitaForm

def is_istruttore(user):
    return user.groups.filter(name='Istruttore').exists()

@login_required
def b_index(request):
    if is_istruttore(request.user):
        raise Http404
    else:
        uscite = Uscita.objects.all()
        return render(request, 'b_index.html', {'uscite': uscite})

@login_required
def uscita_new(request):
    if is_istruttore(request.user):
        raise Http404
    else:
        if request.method == "POST":
            form = UscitaForm(request.POST)
            if form.is_valid():
                uscita = form.save(commit=False)
                uscita.user = request.user
                uscita.save()
                form.save_m2m()
                return redirect('b_index')
        else:
            form = UscitaForm()
        return render(request, 'uscita_new.html', {'form': form})

@login_required
def uscita_edit(request, pk):
    if is_istruttore(request.user):
        raise Http404
    else:
        uscita = get_object_or_404(Uscita, pk=pk)
        if request.method == "POST":
            form = UscitaForm(request.POST, instance=uscita)
            if form.is_valid():
                uscita = form.save(commit=False)
                uscita.user = request.user
                uscita.save()
                form.save_m2m()
                return redirect('b_index')
        else:
            form = UscitaForm(instance=uscita)
        return render(request, 'uscita_edit.html', {'form': form})

@login_required
def uscita_delete(request, pk):
    if is_istruttore(request.user):
        raise Http404
    else:
        uscita = get_object_or_404(Uscita, pk=pk)
        if request.method == "POST":
            uscita.delete()
            return redirect('b_index')
        else:
            return render(request, 'uscita_delete.html', {'uscita':uscita})

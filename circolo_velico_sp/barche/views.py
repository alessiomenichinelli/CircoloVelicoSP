from django.utils import timezone
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Barca, Proprietario, Uscita
from .forms import UscitaForm

def is_istruttore(user):
    return user.groups.filter(name='Istruttore').exists() or user.groups.filter(name='DS').exists()

@login_required
def b_index(request):
    if is_istruttore(request.user):
        raise Http404
    else:
        uscite = Uscita.objects.all()
        data_attuale = timezone.now().date()
        uscite_giorno_t = Uscita.objects.filter(data=data_attuale, tm='terra')
        uscite_giorno_m = Uscita.objects.filter(data=data_attuale, tm='mare')
        uscite_giorno = uscite_giorno_t | uscite_giorno_m
        uscite_archivio = uscite ^ uscite_giorno
        return render(request, 'b_index.html', {'uscite_t': uscite_giorno_t, 'uscite_m': uscite_giorno_m, 'uscite_a': uscite_archivio})

@login_required
def uscita_new(request, tm):
    if is_istruttore(request.user):
        raise Http404
    else:
        if request.method == "POST":
            form = UscitaForm(tm, request.POST,)
            if form.is_valid():
                uscita = form.save(commit=False)
                uscita.tm = tm
                uscita.save()
                form.save_m2m()
                return redirect('b_index')
        else:
            form = UscitaForm(tm)
        return render(request, 'uscita_new.html', {'form': form})

@login_required
def uscita_edit(request, pk):
    if is_istruttore(request.user):
        raise Http404
    else:
        uscita = get_object_or_404(Uscita, pk=pk)
        if request.method == "POST":
            form = UscitaForm(uscita.tm, request.POST, instance=uscita)
            if form.is_valid():
                uscita = form.save(commit=False)
                uscita.save()
                form.save_m2m()
                return redirect('b_index')
        else:
            form = UscitaForm(uscita.tm, instance=uscita)
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
            return render(request, 'uscita_delete.html', {'u':uscita})
        
@login_required
def uscita_view(request, pk):
    uscita = get_object_or_404(Uscita, pk=pk)
    form = UscitaForm(uscita.tm, instance=uscita)
    return render(request, 'uscita_view.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Istruttore, Gommone, Allievo, Uscita
from .forms import UscitaIstruttoreForm, UscitaAmministratoreForm

def is_istruttore(user):
    return user.groups.filter(name='Istruttore').exists()

@login_required
def sv_index(request):
    if is_istruttore(request.user):
        istruttore_associato = Istruttore.objects.get(user=request.user)
        data_attuale = timezone.now().date()
        uscite = Uscita.objects.filter(istruttore=istruttore_associato, data=data_attuale).order_by('-data')
        return render(request, 'sv_index.html', {'uscite': uscite})
    else:
        uscite = Uscita.objects.all().order_by('-data')
        return render(request, 'sv_index.html', {'uscite': uscite})

@login_required
def uscita_new(request):
    if is_istruttore(request.user):
        if request.method == "POST":
            form = UscitaIstruttoreForm(request.user, request.POST)
            if form.is_valid():
                uscita = form.save(commit=False)
                uscita.user = request.user
                uscita.save()
                form.save_m2m()
                return redirect('sv_index')
        else:
            form = UscitaIstruttoreForm(request.user)
        return render(request, 'sv_uscita_new.html', {'form': form})
    else:
        if request.method == "POST":
            form = UscitaAmministratoreForm(request.user, request.POST)
            if form.is_valid():
                uscita = form.save(commit=False)
                uscita.user = request.user
                uscita.save()
                form.save_m2m()
                return redirect('sv_index')
        else:
            form = UscitaAmministratoreForm(request.user)
        return render(request, 'sv_uscita_new.html', {'form': form})

@login_required
def uscita_edit(request, pk):
    if is_istruttore(request.user):
        istruttore_associato = Istruttore.objects.get(user=request.user)
        data_attuale = timezone.now().date()
        uscita = get_object_or_404(Uscita, pk=pk, istruttore=istruttore_associato, data=data_attuale)
        if request.method == "POST":
            form = UscitaIstruttoreForm(request.user, request.POST, instance=uscita)
            if form.is_valid():
                uscita = form.save(commit=False)
                uscita.user = request.user
                uscita.save()
                form.save_m2m()
                return redirect('sv_index')
        else:
            form = UscitaAmministratoreForm(request.user, instance=uscita)
        return render(request, 'sv_uscita_edit.html', {'form': form})
    else:
        uscita = get_object_or_404(Uscita, pk=pk)
        if request.method == "POST":
            form = UscitaAmministratoreForm(request.user, request.POST, instance=uscita)
            if form.is_valid():
                uscita = form.save(commit=False)
                uscita.user = request.user
                uscita.save()
                form.save_m2m()
                return redirect('sv_index')
        else:
            form = UscitaAmministratoreForm(request.user, instance=uscita)
        return render(request, 'sv_uscita_edit.html', {'form': form})

@login_required
def uscita_delete(request, pk):
    if is_istruttore(request.user):
        istruttore_associato = Istruttore.objects.get(user=request.user)
        data_attuale = timezone.now().date()
        uscita = get_object_or_404(Uscita, pk=pk, istruttore=istruttore_associato, data=data_attuale)
        if request.method == "POST":
            uscita.delete()
            return redirect('sv_index')
        else:
            return render(request, 'sv_uscita_delete.html', {'uscita':uscita})
    else:
        uscita = get_object_or_404(Uscita, pk=pk)
        if request.method == "POST":
            uscita.delete()
            return redirect('sv_index')
        else:
            return render(request, 'sv_uscita_delete.html', {'uscita':uscita})

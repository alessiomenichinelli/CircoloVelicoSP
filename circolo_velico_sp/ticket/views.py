from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Ticket
from .forms import NewTicketForm, EditTicketForm

def is_istruttore(user):
    return user.groups.filter(name='Istruttore').exists()

def is_nostromo(user):
    return user.groups.filter(name='Nostromo').exists()

@login_required
def index(request):
    istruttore = is_istruttore(request.user)
    nostromo = is_nostromo(request.user)
    return render(request, 'index.html', {'istruttore': istruttore, 'nostromo': nostromo})

@login_required
def ticket_list(request):
    if is_istruttore(request.user) or is_nostromo(request.user):
        tickets = Ticket.objects.filter(user=request.user)
        return render(request, 'ticket_list_in.html', {'tickets': tickets})
    else:
        tickets = Ticket.objects.all()
        return render(request, 'ticket_list_a.html', {'tickets': tickets})

@login_required
def ticket_new(request):
    if not is_istruttore(request.user) and not is_nostromo(request.user):
        raise Http404
    else:
        if request.method == "POST":
            form = NewTicketForm(request.POST)
            if form.is_valid():
                ticket = form.save(commit=False)
                ticket.user = request.user
                ticket.stato = 'Inviato'
                ticket.save()
                form.save_m2m()
                return redirect('ticket_list')
        else:
            form = NewTicketForm()
        return render(request, 'ticket_new.html', {'form': form})

@login_required
def ticket_edit(request, pk):
    if is_istruttore(request.user) or is_nostromo(request.user):
        raise Http404
    else:
        ticket = get_object_or_404(Ticket, pk=pk)
        if request.method == "POST":
            form = EditTicketForm(request.POST, instance=ticket)
            if form.is_valid():
                ticket = form.save(commit=False)
                ticket.save()
                form.save_m2m()
                return redirect('ticket_list')
        else:
            form = EditTicketForm(instance=ticket)
        return render(request, 'ticket_edit.html', {'form': form})

@login_required
def ticket_delete(request, pk):
    if not is_istruttore(request.user) and not is_nostromo(request.user):
        raise Http404
    else:
        ticket = get_object_or_404(ticket, pk=pk, user=request.user)
        if request.method == "POST":
            ticket.delete()
            return redirect('ticket_list')
        else:
            return render(request, 'ticket_delete.html', {'ticket':ticket})
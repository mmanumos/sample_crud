from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm

# views


def index(request):
    persons = Person.objects.all()
    context = {
        "persons": persons
    }
    return render(request, 'index.html', context)


def create_person(request):
    if request.method == 'GET':
        form = PersonForm()
        context = {
            'form': form
        }
    else:
        form = PersonForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
        print(form)
    return render(request, 'create_person.html', context)


def editPerson(request, id):
    person = Person.objects.get(id=id)
    if request.method == 'GET':
        form = PersonForm(instance=person)
        context = {
            'form': form
        }
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('/edit_person/' + str(person.id))
    return render(request, 'create_person.html', context)


def deletePerson(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return redirect('index')

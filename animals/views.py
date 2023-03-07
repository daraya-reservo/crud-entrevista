from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from .models import Animal
from .forms import AnimalForm


def list_view(request):
    animals = Animal.objects.all()
    return render(request, "animals/list_view.html", {'animals': animals})

def create_view(request):
    form = AnimalForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('animals'))
    return render (request, 'animals/create_view.html', {'form': form})

def detail_view(request, pk):
    animal = Animal.objects.get(id=pk)
    return render(request, "animals/detail_view.html", {'animal': animal})

def update_view(request, pk):
    animal = get_object_or_404(Animal, id=pk) 
    form = AnimalForm(request.POST or None, instance=animal)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('animals'))
    return render(request, "animals/update_view.html", {'form': form})

def delete_view(request, pk):
    animal = get_object_or_404(Animal, id=pk)
    animal.delete()
    return HttpResponseRedirect("/")

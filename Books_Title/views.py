from django.shortcuts import render
from django.contrib.postgres.search import *
from django.contrib.postgres.operations import  *
from .models import *
from .forms import *
from .populatedata import *

# Create your views here.
def BookSearch(request): 
    form = SearchField()

    if request.method == "POST":
        form = SearchField(request.POST)
        if form.is_valid():
            # populating()
            query = form.cleaned_data.get('searchinput')
            mango = Books.objects.annotate(search=SearchVector('book_name', 'authorname'),).filter(search=query)
            apple = Books.objects.annotate(similarity=TrigramSimilarity('authorname', query) + TrigramSimilarity('book_name', query),).filter(similarity__gt=0.1) .order_by('-similarity')
            print(mango)
            print(apple)

            

    return render(request, "BookSearch.html", {'form': form})






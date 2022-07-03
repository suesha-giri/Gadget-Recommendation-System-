from django.shortcuts import render
from .models import Smartphone
from django.contrib.auth.models import User
from homepage import recommender
from homepage import popularity
from . import recommender 
from . import popularity
from django.db.models import Case, When


# Create your views here.
def home(request): 

    if request.user.is_authenticated:
        current_user = request.user.id
        predicted_items=recommender.User_item_score2(current_user)
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(predicted_items)]) 
        mob = Smartphone.objects.filter(pk__in=predicted_items).order_by(preserved)

    elif not request.user.is_authenticated:
        pk_list=popularity.popularity_recommendation()
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(pk_list)]) 
        mob = Smartphone.objects.filter(pk__in=pk_list).order_by(preserved)
          
    return render(request,'index.html', {'mob':mob})


def search(request):
    if request.method == 'POST':
        searched=request.POST["searched"]
        gadgets=Smartphone.objects.filter(name__icontains =searched)
        
        return render(request, 'search_results.html',{'searched':searched, 'gadgets':gadgets})
            
    else:
        return render(request, 'search_results.html')

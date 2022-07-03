from django.contrib import messages
from django.shortcuts import redirect, render
from homepage.models import Smartphone, SmartphoneDetails
from subpages.models import Comment
from homepage import recommender
from homepage import popularity
from subpages.forms import CommentForm
from django.urls import reverse
from django.db.models import Case, When
# Create your views here.

def smartwatch(request):
    return render(request,'smartwatch.html')


def laptop(request):
    return render(request,'laptops.html')


def smartphone(request):
     
    if request.user.is_authenticated:
        current_user=request.user.id
        predicted_items=recommender.User_item_score2(current_user)
        preserved=Case(*[When(pk=pk, then=pos) for pos,pk in enumerate(predicted_items)])
        mob=Smartphone.objects.filter(pk__in=predicted_items).order_by(preserved)

    elif not request.user.is_authenticated:
        pk_list=popularity.popularity_recommendation()
        preserved=Case(*[When(pk=pk, then=pos) for pos,pk in enumerate(pk_list)])
        mob=Smartphone.objects.filter(pk__in=pk_list).order_by(preserved)

    return render(request,'smartphones.html',{'mob':mob})


def specification(request,id=None):
    form=CommentForm()   
    mob1=SmartphoneDetails.objects.get(pk=id)
    reviews=Comment.objects.filter(smartphone_id=id, status='True')

    return render(request,'specs.html',{'mob1':mob1,'form':form,'reviews':reviews})


def addComment(request, id=None):
    form=CommentForm()
    print(id)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            data=Comment()
            data.comment=form.cleaned_data['comment']
            data.rate=form.cleaned_data['rate']
            data.smartphone_id=id
            current_user=request.user
            data.user_id=current_user.id
            data.save()
            messages.success(request,"Your review has been added successfully ")
            return redirect(reverse('specification',args=[id]))
    
    return redirect(reverse('specification',args=[id]))
 

  


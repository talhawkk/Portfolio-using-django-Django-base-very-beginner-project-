from django.shortcuts import render

# Create your views here.
def home(request):
    name="Talha ABbas"
    p1="portfoli website"
    p2="game"
    djdic={"name":name,"pp1":p1,"pp2":p2}
    return render(request,'home/home.html',djdic)
from django.shortcuts import render
def show_main(request):
    context = {
        'app': 'I WEAR SOCCER',
        'name': 'Naila Khadijah',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
# Create your views here.

from shop.models import Categoryy
def menu_links(request):
    c=Categoryy.objects.all()
    return {'links':c}
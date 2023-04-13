from ninja import NinjaAPI
from ninja import Router
from library.models import Product
from library.models import BookAuth

Pr_Router = Router(tags=["Produc"])
Ath_Router = Router(tags=["book_Auth"])
book_Router = Router(tags=["Produc"])

# 1- Endpoint To Get All Available Books.
@Pr_Router.get("allbook")
def allbook(request):
    return Product.objects.all().filter(is_DrawTool=False)


#2- Endpoint To Get Book With ID.
@Pr_Router.get("bookid{id}")
def bookid(request, id: int):
    try:
        product = Product.objects.get(id=id)
        return {"ok"}
    except Product.DoesNotExist as e:
        return {"message": "product does not exist"}


#3- Endpoint To Get Auth With Specific Name.
@Ath_Router.get("authbyname{name}")
def authbyname(request, authname=None):
     try:
         auth= BookAuth.objects.get(name=authname)
         return {"ok"}
     except BookAuth.DoesNotExist as e:
         return {"message": "This Auth does not exist"}


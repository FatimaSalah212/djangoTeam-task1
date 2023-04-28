from ninja import NinjaAPI
from typing import List
from ninja import Router
from library.models import Product
from library.models import BookAuth
from library.schema import bookachema, authschema

Pr_Router = Router(tags=["Product"])
Ath_Router = Router(tags=["book_Auth"])
book_Router = Router(tags=["Product"])

# 1- Endpoint To Get All Available Books.
@Pr_Router.get("allbook",response=List[bookachema])
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

# 4- create api to create books
@Pr_Router.post("CreateBook", response={200: bookachema})
def createbook(request, Product: bookachema):
    product=Product.objects.create(**Product.dict())
    return product

# 5- create api to Update books
@Pr_Router.put("putBook", response={200: bookachema})
def updatebook(request, id:int, data: bookachema):
    try:
        product = Product.objects.get(id=id)
        for attribute, value in data.dict().items():
            setattr(product, attribute, value)
        product.save()
        return 200, product
    except Product.DoesNotExist as e:
        return {"message": "product does not exist"}

# # 6- create api to delete books
@Pr_Router.delete("CreateBook", response={200: bookachema})
def deletebook(request,id:int, data: bookachema):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return 200
    except Product.DoesNotExist as e:
        return {"message": "product does not exist"}

# 7- create api to create auth
@Ath_Router.post("CreateAuth", response={200: authschema})
def createauth(request, BookAuth: authschema):
    auth=BookAuth.objects.create(**BookAuth.dict())
    return auth

# 8- create api to Update auth
@Ath_Router.put("putAuth", response={200: authschema})
def updateauth(request, id:int, data: authschema):
    try:
        auth = BookAuth.objects.get(id=id)
        for attribute, value in data.dict().items():
            setattr(auth, attribute, value)
        auth.save()
        return 200, auth
    except BookAuth.DoesNotExist as e:
        return {"message": "Auth does not exist"}

# 9- create api to delete auth
@Ath_Router.delete("deleteAuth", response={200: authschema})
def deleteauth(request,id:int, data: authschema):
    try:
        auth = BookAuth.objects.get(id=id)
        auth.delete()
        return 200
    except BookAuth.DoesNotExist as e:
        return {"message": "product does not exist"}
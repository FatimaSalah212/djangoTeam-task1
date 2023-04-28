from ninja import Schema

class bookachema(Schema):
    name: str
    section:str
    price: str
    image:str
    language:str
    category:str
    is_active: bool
    is_rare:bool
    is_DrawTool:bool
    auth: str

class notFindSchema(Schema):
    message:str

class authschema(Schema):
    name: str
    email:str
    phone: str
    number_of_book:int
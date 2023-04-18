from django.db import models


# Create your models here.

class Section(models.TextChoices):
    BookStore = 'Book_Store', 'Book_Store'
    DrawSore = 'Draw_Store', 'Draw_Store'


class Product(models.Model):
    name = models.CharField(verbose_name='product_name', max_length=255)
    section = models.CharField('section', max_length=100, choices=Section.choices)
    price = models.FloatField(verbose_name='product_price', default=0.0)
    image = models.URLField('product_image', blank=True, null=True)

    # choices Data Field
    # The first element in each tuple is the actual value to be set on the model, 
    # and the second element is the human-readable name. For example:
    language = models.CharField(max_length=100, null=True, blank=True, choices=[
        ('AR', 'Arabic'),
        ('EN', 'English'),
        ('FR', 'Franch'),
    ]),
    category = models.CharField(max_length=100, null=True, blank=True, choices=[
        ('Scientific', 'Scientific'),
        ('Art', 'Art'),
        ('Historic', 'Historic'),
        ('Novels', 'Novels'),
        ('Fictional', 'Fictional'),
    ])

    # Here is Boolean Field 
    # A true/false field.
    is_active = models.BooleanField('is_active', default=True)
    is_rare = models.BooleanField('is_rare', default=False)
    is_DrawTool = models.BooleanField('is_book', default=False)
 auth = models.ForeignKey('BookAuth', null=True, blank=True, on_delete=models.SET_NULL, related_name='products')

    def __str__ (self):
        return f'{self.name}-{self.category}-{self.is_DrawTool}'


class BookAuth(models.Model):
    name = models.CharField('auth_name', max_length=100)
    email = models.EmailField('auth_email', max_length=254, null=True, blank=True)
    phone = models.CharField('auth_phone', max_length=100)
    number_of_book = models.IntegerField('number_of_book', default=0)
    def __str__(self):
        return f'{self.name}-{self.email}'

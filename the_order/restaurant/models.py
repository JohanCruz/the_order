from email.policy import default
from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='media/logo/')
    available = models.BooleanField()
    visible = models.BooleanField()

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='media/category/')
    restaurant = models.ForeignKey(Restaurant,on_delete = models.CASCADE )
    available = models.BooleanField()
    visible = models.BooleanField()
    class Meta:
        verbose_name_plural = "Categories"
    '''def __str__(self):
        return f"{self.name}"'''

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='media/product/')    
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    available = models.BooleanField()
    visible = models.BooleanField()
    def __str__(self):
        return f"{self.name}"
    

class Order(models.Model):
    Espera = 'Espera'
    Preparacion = 'Preparación'
    Finalizado = 'Finalizado'
    state_choices = [
        ('ESPERA', 'E'),
        ('PREPARACION', 'P'),
        ('FINALIZADO', 'F'),
    ]
    state = models.CharField(
        max_length=11,
        choices=state_choices,
        default='ESPERA',
    )
    def is_waiting(self):
        return self.state_choices in {self.ESPERA}
    
    def is_making(self):
        return self.state_choices in {self.PREPARACION}

    def is_ending(self):
        return self.state_choices in {self.FINALIZADO}
        
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    product = models.ManyToManyField(Product, related_name='models', through='ProductOrder')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=1)
    description = models.TextField( default=1)
    def __str__(self):
        return self.name + self.created_date.strftime("%m/%d/%Y, %H:%M:%S")

class ProductOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    carry_off = models.BooleanField(default=False)
    description = models.TextField()
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.order}, {self.product}"
    
    
    



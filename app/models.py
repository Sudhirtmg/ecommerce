from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.
class Slider(models.Model):
    DISCOUNT_DEALS={
        ('HOT DEALS','HOT_DEALS'),
        ('NEW ARRIVAL','NEW ARRIVAL'),
        ('FULLY DISCOUNT','FULLY_DISCOUNT')

    }
    Image=models.ImageField(upload_to='media/slider_imgs')
    Discount_Deals=models.CharField(choices=DISCOUNT_DEALS,max_length=200)
    Sale=models.IntegerField()
    Brand_name=models.CharField(max_length=200)
    Discount=models.IntegerField()

    def __str__(self):
        return self.Brand_name
    
class Banner(models.Model):
    DISCOUNT_DEALS={
        ('HOT DEALS','HOT_DEALS'),
        ('NEW ARRIVAL','NEW ARRIVAL'),
        ('FULLY DISCOUNT','FULLY_DISCOUNT')

    }
    Image=models.ImageField(upload_to='media/slider_imgs')
    Discount_Deals=models.CharField(choices=DISCOUNT_DEALS,max_length=200)
    Quote=models.CharField(max_length=200)
    Discount=models.IntegerField()
    def __str__(self):
        return self.Quote
    
class Main_Category(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Category(models.Model):
   main_category=models.ForeignKey(Main_Category,on_delete=models.CASCADE)
   name=models.CharField(max_length=200)
   def __str__(self):
       return self.main_category.name+'-------'+self.name
class Sub_Category(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.category.main_category.name+'-----'+self.category.name+'------'+self.name
class Section(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Product(models.Model):
    Product_Quantity=models.IntegerField()
    Product_Availability=models.IntegerField()
    Product_Image=models.CharField(max_length=200)
    Product_Name=models.CharField(max_length=200)
    Product_Informations=RichTextField()
    Product_Price=models.IntegerField()
    Product_Discount=models.IntegerField()
    Product_Descriptions=RichTextField()
    Tags=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    section=models.ForeignKey(Section,on_delete=models.DO_NOTHING)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.Product_Name
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("product_detail", kwargs={'slug': self.slug})

    class Meta:
        db_table = "app_Product"

def create_slug(instance, new_slug=None):
    slug = slugify(instance.Product_Name)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, Product)
    
class Product_Image(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    Image_Url=models.CharField(max_length=200)

class Additional_Information(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    Specifications=models.CharField(max_length=200)
    Details=models.CharField(max_length=200)




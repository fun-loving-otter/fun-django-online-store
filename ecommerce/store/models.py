from django.db import models

from django.urls import reverse


#1.category, shorts, shoes, pants etc., all unique
class Category(models.Model):

    name=models.CharField(max_length=250,db_index=True)                                                                 #db index to make looking for it faster

    slug=models.SlugField(max_length=250,unique=True)                              # slugs if remain MUST BE USED       #unique cause only one category for every product

    class Meta:
        verbose_name_plural = 'categories'                                                                              #django by default adds an s to category name


    def __str__(self):
        return self.name
#2.(returns name from class in a clear form)

#dynamic links for categories
    def get_absolute_url(self):

        return reverse('list-category',args=[self.slug])



class Product(models.Model):
    #linking category and product through a foreign key, will add category to products

    category = models.ForeignKey(Category, related_name='product',on_delete=models.CASCADE, null=True)

    title=models.CharField(max_length=250)

    brand=models.CharField(max_length=250,default='un-branded')

    description= models.TextField(blank=True)                                                   #blank denotes an optional field

    slug=models.SlugField(max_length=255)                                                       #to make urls more user-friendly and readable and unique

    price=models.DecimalField(max_digits=5,decimal_places=2)                                     #product price

    image = models.ImageField(upload_to='images/')                                              #upon uploading an image will create an image subfolder in media (pillow rqd)

    tags = models.ManyToManyField('Tag', related_name='product_tags', blank=True)                #MANY TO MANY RELATIONSHIP with tags,acting as an intermediary


    class Meta:
        verbose_name_plural = 'products'                                                       #django by default adds an s to category name


    def __str__(self):
        return self.title                                                                        #(products referenced by their correct title instead of product1, or product2)


#dynamic links for products
    def get_absolute_url(self):

        return reverse('product-info',args=[self.slug])


class Tag(models.Model):                                                                                                # Many to many relationship with Products category
    tag_name = models.CharField(max_length=128)
    tag_slug = models.SlugField(max_length=255)                                                                         # BEST SELLERS, NEW ARRIVALS

    def __str__(self):
        return self.tag_name

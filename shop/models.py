from django.db import models



class Brand(models.Model):
    brand_name = models.CharField(max_length=250,
                                  )
    def __str__(self):
        return self.brand_name
    

class Size(models.Model):
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.size
    
class Colors(models.Model):
    color_name = models.CharField(max_length=50)

    def __str__(self):
        return self.color_name
    
class Clothes(models.Model):
    title = models.CharField(max_length=250)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    size = models.ManyToManyField(Size)
    color = models.ManyToManyField(Colors)
    image1 = models.ImageField(upload_to='product/',
                               blank=True,
                               null=True,)
    image2 = models.ImageField(upload_to='product/',
                               blank=True,
                               null=True,)
    image3 = models.ImageField(upload_to='product/',
                               blank=True,
                               null=True,)
    description = models.TextField()
    created_date = models.DateTimeField(
        auto_now_add=True,
    )
    def __str__(self):
        return self.title



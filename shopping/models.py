from django.db import models

class category(models.Model):
    Name=models.CharField(max_length=100)
    def __str__(self):
        return self.Name

class sub_category(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE, null=True)
    Sub_Name=models.CharField(max_length=100)
    def __str__(self):
        return self.Sub_Name

class products(models.Model):
    sub_category = models.ForeignKey(sub_category, on_delete=models.CASCADE, null=True)
    Name=models.CharField(max_length=100)
    price=models.FloatField()
    Description=models.TextField()
    img1=models.FileField(null=True)
    img2 = models.FileField(null=True)
    img3 = models.FileField(null=True)
    Descount = models.CharField(max_length=100)
    Quantity=models.IntegerField()
    size=models.CharField(max_length=500)
    color=models.CharField(max_length=600)
    def __str__(self):
        return self.Name
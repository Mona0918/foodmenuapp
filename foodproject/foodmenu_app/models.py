from django.db import models

class ItemModel(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1240w,f_auto,q_auto:best/streams/2014/May/140501/2D274905752676-setting860.png")

    def __str__(self):
        return self.item_name

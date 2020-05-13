from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# ************* details about deleting objects of this model************
# if u delete object of community its post will also be deleted
# if u delete object of post only the post itself will be deleted
# if u delete admin of community then community and its post **will not be deleted**
# the admin will set to blank for that community

class community(models.Model):
    name = models.CharField(max_length = 255,blank=False,null=False)
    desc = models.TextField(blank=True)
    admin = models.ForeignKey(User,on_delete=models.SET_NULL,related_name='admin',null=True)
    followed_by = models.ManyToManyField(User,blank = True)
    slug = models.SlugField(default='')

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class post(models.Model):
    community = models.ForeignKey(community,on_delete=models.CASCADE)
    post_img = models.ImageField(upload_to='static/images/post_img',null= True,blank =True)
    post_desc = models.TextField(blank=True)
    created_at = models.DateTimeField()



# Create your models here.
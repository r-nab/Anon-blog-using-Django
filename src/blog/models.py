from django.db import models
from django.db.models.signals import pre_save


def upload_loc(instance, filename):
    return "post_media/"+instance.uid+"_"+filename


class Post(models.Model):
    Choices = (
        ('Science','Science'),
        ('Technology','Technology'),
        ('Arts','Arts'),
        ('News','News'),
        ('Event','Event'),
        ('Music','Music'),
    )
    uid = models.CharField(max_length=7, primary_key=True)
    title = models.CharField(max_length=120)
    myurl = models.CharField(unique=True, max_length=60)
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to=upload_loc,
        width_field='imgwidth',
        height_field='imgheight'
        )
    imgwidth = models.IntegerField(default=0)
    imgheight = models.IntegerField(default=0)    
    content = models.TextField()
    tag = models.CharField(max_length=15, choices=Choices, default='Science')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "blog/post=%s" %(self.myurl)
    class Meta:
        ordering = ['-timestamp']

def mk_url_friendly(instance):
    s = instance.title
    new = ''
    for i in s[:50]:
        if ord(i) <= 122 and ord(i) >= 97 or ord(i) <= 90 and ord(i) >= 65 or ord(i) <= 57 and ord(i) >= 48 or ord(i) == 45 or ord(i) == 95 or ord(i) == 32:
            if ord(i) == 32:
                i = '_'
                new = new + i
            else:
                new = new + i
    return new

def pre_save_friendly_url(sender, instance, *args, **kwargs):
    new_url = mk_url_friendly(instance)
    existing = Post.objects.filter(myurl=new_url).exists()
    if existing:
        new_url = new_url+'-'+instance.uid
    instance.myurl = new_url     


pre_save.connect(pre_save_friendly_url, sender=Post)    
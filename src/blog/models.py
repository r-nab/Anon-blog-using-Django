from django.db import models

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
    content = models.TextField()
    tag = models.CharField(max_length=15, choices=Choices, default='Science')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "blog/post_%s" %(self.id)
    class Meta:
        ordering = ['-timestamp']

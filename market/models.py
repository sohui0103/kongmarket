from django.db import models

class Blog(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False) 
    title = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    body = models.TextField()
    image = models.ImageField(upload_to='image/', default='')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
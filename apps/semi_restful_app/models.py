from django.db import models
from datetime import datetime, timedelta
# Create your models here.

class ShowManager (models.Manager):
    def validate(self, form):
        errors = []
        if len(form['title']) < 1:
            errors.append("Title  must not be blank.")
        
        if len(form['network']) < 1:
             errors.append("Network must not be blank.")
        
        if len(form['description']) < 1:
             errors.append("Description must not be blank.")
        try:
            # if this doesn't work, it will throw an error
            # if there's an error we'll use the except block
            release_date = datetime.strptime(form['release_date'], '%Y-%m-%d')
            now = datetime.now()
            if release_date > now:
                errors.append("Release Date must be in the past.")
        except:
            # date input works in chrome and takes this pattern
            # the date input sends a different pattern back, hence the strptime formatting
            errors.append("release_date must be a valid date in MM/DD/YYYY format.")
        
        return errors
    
    def easy_show_create (self, form):
        show = Show.objects.create(
            title = form['title'],
            network = form['network'],
            release_date = form['release_date'],
            description = form['description'],
        )
        return show.id
        
    def easy_show_update (self, form, show_id):
        show = Show.objects.filter(id=show_id)
        show.title = form['title'],
        show.network = form['network'],
        show.release_date = form['release_date'],
        show.description = form['description'],
        show.save()
        
        
class Show(models.Model):
    title = models.CharField(max_length=30)
    network = models.CharField(max_length=30)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __repr__(self):
        return f"<Show id:{self.id}>"

    def __str__(self):
        return f"<Show id:{self.id}>"
from django.db import models
from django.contrib.auth.models import User

class UserLink (models.Model):
  from_user = models.ForeignKey(User, related_name='fromuser')
  to_user = models.ForeignKey(User, related_name='touser')
  date_added = models.DateField()
 
  def save(self, *args, **kwargs):
    if self.from_user == self.to_user:
      return
    else:
      super(UserLink, self).save(*args, **kwargs)
       
  def __unicode__(self):
    return self.from_user.username + " is following " + self.to_user.username
  
  class Meta:
    unique_together = ("from_user", "to_user")
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver


from django.contrib.auth.models import User
from .models import Profile

# @receiver(post_save,sender=Profile)    
def createProfile(sender,instance,created,**kwargs):
      # print("profile saved")
      # print("Instance: ",instance)
      # print("Created: ",created)
      print("creating a new profile for the newly created user")
      if created:
            user =instance
            profile = Profile.objects.create(
                  user=user,
                  username=user.username,
                  email=user.email,
                  name=user.first_name,
            )

#@receiver(post_delete,sender=Profile) 
def deleteUser(sender,instance,**kwargs):
      # code to delete the user when the profile is deleted
      user = instance.user
      user.delete()
      print("Deleting user")

post_save.connect(createProfile,sender=User)
post_delete.connect(deleteUser,sender=Profile)
from django.db import models

from django.conf import settings


# make sure this model is cofigured in the settings file of the project
# User = settings.AUTH_USER_MODEL


# class Post(models.Model):

#     description = models.CharField(max_length=500)
#     image = models.ImageField(upload_to="post/")
#     category = models.CharField()

#     poster = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="posts"
#     )


# # request is created when the user hits the send request button
# class Request(models.Model):

#     sender = models.ForeignKey(User, on_delete=models.CASCADE,)
#     receiver = models.ForeignKey(User, on_delete=models.CASCADE)

#     is_sent = models.BooleanField()


# # Notification is a collection of requests
# # a read and accepted request can be deleted from the database

# class Notifications(models.Model):

#     receiver = models.ForeignKey(User)

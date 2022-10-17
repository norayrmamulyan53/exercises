from django.db import models


class Member(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=200)
    passwd = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.fname} {self.lname}"

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"



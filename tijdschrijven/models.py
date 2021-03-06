from django.db import models
from django.contrib.auth.models import User


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings #https://learndjango.com/tutorials/django-best-practices-referencing-user-model


class Project(models.Model):
    Titel = models.CharField(max_length=88, null=True)
    ProjectTemplateID = models.ForeignKey('ProjectTemplate', on_delete=models.RESTRICT)
    Omschrijving = models.CharField(max_length=256, null=True)
    ParentID = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='subproject')
    AanmakerID = models.IntegerField(null=True)
    AanmaakDatum = models.DateField(auto_now_add=True)
    MutatieDatum = models.DateField(auto_now=True)
    GeldigVan = models.DateField()
    GeldigTot = models.DateField()
    Actief = models.BooleanField()
    Personen = models.ManyToManyField('Persoon', through='Abonnement')

    def __str__(self):
        """String for representing the Model object."""
        return self.Titel
    class Meta:
        verbose_name_plural = "projecten"


class Persoon(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Projecten = models.ManyToManyField(Project, through='Abonnement')

    class Meta:
        verbose_name_plural = "personen"

    def __str__(self):
        """String for representing the Model object."""
        return self.user.username


# @receiver(post_save, sender=User)
# def create_user_persoon(sender, instance, created, **kwargs):
#     if created:
#         Persoon.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_persoon(sender, instance, **kwargs):
#     instance.persoon.save()


class Abonnement(models.Model):
    ProjectID = models.ForeignKey(Project, on_delete=models.CASCADE)
    PersoonID = models.ForeignKey(Persoon, on_delete=models.CASCADE) 
    OriginalObjectID = models.IntegerField()
    AanmaakDatum = models.DateField(auto_now_add=True)
    Zichtbaarheid = models.BooleanField()

    class Meta:
        verbose_name_plural = "abonnementen"


class AccountSetting(models.Model):
    PersoonID = models.ForeignKey(User, on_delete=models.CASCADE)

    ACCOOUNTITEMS = (
        (1, 'Dienstverband'),
    )

    AccountItem = models.SmallIntegerField(
        choices=ACCOOUNTITEMS,
        blank=True,
        default=1,
        help_text='Acoount item',
    )
    Setting = models.IntegerField(null=True)
    AanmaakDatum = models.DateField(auto_now_add=True)
    GeldigVan = models.DateField()
    GeldigTot = models.DateField()   

    def __str__(self):
        """String for representing the Model object."""
        return self.AccountItem


class ProjectTemplate(models.Model):
    Titel = models.CharField(max_length=128)
    Omschrijving = models.CharField(max_length=256)

    def __str__(self):
        """String for representing the Model object."""
        return self.Titel


class GeschrevenTijd(models.Model):
    AbonnementID = models.ForeignKey('Abonnement', on_delete=models.CASCADE)
    AanmaakDatum = models.DateField(auto_now_add=True)
    Datum = models.DateField()
    TijdsDuur = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name_plural = "geschreven tijd"

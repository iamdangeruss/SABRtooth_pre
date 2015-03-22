from django.db import models

# Create your models here.
class Master(models.Model):
    playerid = models.CharField(db_column='playerID', primary_key=True, max_length=10)  # Field name made lowercase.
    birthyear = models.IntegerField(db_column='birthYear', blank=True, null=True)  # Field name made lowercase.
    birthmonth = models.IntegerField(db_column='birthMonth', blank=True, null=True)  # Field name made lowercase.
    birthday = models.IntegerField(db_column='birthDay', blank=True, null=True)  # Field name made lowercase.
    birthcountry = models.CharField(db_column='birthCountry', max_length=50, blank=True)  # Field name made lowercase.
    birthstate = models.CharField(db_column='birthState', max_length=2, blank=True)  # Field name made lowercase.
    birthcity = models.CharField(db_column='birthCity', max_length=50, blank=True)  # Field name made lowercase.
    deathyear = models.IntegerField(db_column='deathYear', blank=True, null=True)  # Field name made lowercase.
    deathmonth = models.IntegerField(db_column='deathMonth', blank=True, null=True)  # Field name made lowercase.
    deathday = models.IntegerField(db_column='deathDay', blank=True, null=True)  # Field name made lowercase.
    deathcountry = models.CharField(db_column='deathCountry', max_length=50, blank=True)  # Field name made lowercase.
    deathstate = models.CharField(db_column='deathState', max_length=2, blank=True)  # Field name made lowercase.
    deathcity = models.CharField(db_column='deathCity', max_length=50, blank=True)  # Field name made lowercase.
    namefirst = models.CharField(db_column='nameFirst', max_length=50, blank=True)  # Field name made lowercase.
    namelast = models.CharField(db_column='nameLast', max_length=50, blank=True)  # Field name made lowercase.
    namegiven = models.CharField(db_column='nameGiven', max_length=255, blank=True)  # Field name made lowercase.
    weight = models.IntegerField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    bats = models.CharField(max_length=1, blank=True)
    throws = models.CharField(max_length=1, blank=True)
    debut = models.DateTimeField(blank=True, null=True)
    finalgame = models.DateTimeField(db_column='finalGame', blank=True, null=True)  # Field name made lowercase.
    retroid = models.CharField(db_column='retroID', max_length=9, blank=True)  # Field name made lowercase.
    bbrefid = models.CharField(db_column='bbrefID', max_length=9, blank=True)  # Field name made lowercase.

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.playerid
        
    class Meta:
        managed = False
        db_table = 'Master'
        
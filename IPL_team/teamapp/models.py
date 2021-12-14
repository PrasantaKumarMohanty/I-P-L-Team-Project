from django.db import models

# Create your models here.

class Team(models.Model):
	t_name = models.CharField(max_length=100, null=True, blank=True)
	t_icon = models.FileField(upload_to='media/ticon/', null=True)
	t_player_count = models.IntegerField(null=True, blank=True)
	t_top_bat = models.CharField(max_length=500, null=True, blank=True)
	t_top_bowl = models.CharField(max_length=500, null=True, blank=True)
	t_won_count = models.IntegerField(null=True, blank=True)

class Player(models.Model):
	p_name = models.CharField(max_length=100, null=True, blank=True)
	p_photo = models.FileField(upload_to='media/photo/', null=True)
	p_team = models.CharField(max_length=500, null=True, blank=True)
	p_price = models.CharField(max_length=500, null=True, blank=True)
	p_play_status = models.CharField(max_length=500, null=True, blank=True)
	t_role = models.CharField(max_length=500, null=True, blank=True)


			



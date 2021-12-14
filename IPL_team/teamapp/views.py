from django.shortcuts import render, HttpResponse
from teamapp.models import Team, Player
from django.contrib import messages
from teamapp.forms import teamform
from django.core import serializers
import json
# Create your views here.

def getRandomString(stringLength=10):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))

def teamdisplay(request):
	results=Team.objects.all()
	return render(request, "index.html", {"Team":results})

def search(request):
	query=request.GET['query']
	#search=Team.objects.all()
	search=Team.objects.filter(t_name__icontains=query)
	srch_rslt={"search":search}
	return render(request,"search.html", srch_rslt)
	#return HttpResponse('This is search')

def teamInsert(request):
	if request.method=="POST":
		if request.POST.get('t_name') or request.POST.get('t_icon') or request.POST.get('t_player_count') or request.POST.get('t_top_bat') or request.POST.get('t_top_bowl') or request.POST.get('t_won_count'):
			saveteam=Team()
			saveteam.t_name=request.POST.get('t_name')
			saveteam.t_name=request.POST.get('t_name')
			saveteam.t_icon=request.FILES['t_icon']
			saveteam.t_player_count=request.POST.get('t_player_count')
			saveteam.t_top_bat=request.POST.get('t_top_bat')
			saveteam.t_top_bowl=request.POST.get('t_top_bowl')
			saveteam.t_won_count=request.POST.get('t_won_count')
			saveteam.save()
			messages.success(request,"The team "+saveteam.t_name+" is added successfully...!")
			return render(request,"t_create.html")
		else:
			return HttpResponse("Not getting values")
	else:
		return render(request,"t_create.html")



def teamedit(request,id):
	getteamdetails=Team.objects.get(id=id)
	return render(request,"edit.html",{"Team":getteamdetails})

def teamupdate(request,id):
	teamupdate=Team.objects.get(id=id)
	form=teamform(request.POST,instance=teamupdate)
	if form.is_valid():
		form.save()
		messages.success(request,"Update successfully...!")
		return render(request,"edit.html",{"Team":teamupdate})

def teamdel(request,id):
	delteam=Team.objects.get(id=id)
	delteam.delete()
	results=Team.objects.all()
	return render(request, "index.html", {"Team":results})

def teamdetails(request,id):
	teamdetails=Team.objects.get(id=id)
	print("teamdetails",request)
	query_set=Team.objects.filter(id=id)
	query_set=serializers.serialize('json',query_set)
	team_icon=json.loads(query_set)
	print(team_icon[0]['fields']['t_icon'])
	team_icon='http://localhost:8000/'+team_icon[0]['fields']['t_icon']
	print(team_icon)
	allplayers=Player.objects.filter(p_team=id)
	return render(request,"t_details.html",{"Team":teamdetails,"allplayers":allplayers,"team_icon":team_icon})
	# print('allp',allplayers)
	# query_set=Player.objects.filter(id=id)
	# query_set=serializers.serialize('json',allplayers)
	# p_icon=json.loads(query_set)
	# print('p-icon',p_icon)
	# print('all player image',p_icon[0]['fields']['p_photo'])
	# player_icon=[]
	# for i in p_icon:
	# 	player_icon.append('http://localhost:8000/'+p_icon[i]['fields']['p_photo'])
	# p_icon='http://localhost:8000/'+p_icon[0]['fields']['p_photo']
	# print(p_icon)
	# print("allplayers",allplayers[0])
	

def addplayer(request):
	if request.method=="POST":
		if request.POST.get('p_name') or request.POST.get('p_photo') or request.POST.get('p_team') or request.POST.get('p_price') or request.POST.get('p_play_status') or request.POST.get('t_role'):
			saveplayer=Player()
			print(request.POST.get('p_team'))
			query_set=Team.objects.filter(t_name=request.POST.get('p_team'))
			query_set=serializers.serialize('json',query_set)
			team_id=json.loads(query_set)
			team_id=team_id[0]['pk']
			saveplayer.p_name=request.POST.get('p_name')
			saveplayer.p_photo=request.FILES['p_photo']
			saveplayer.p_team=team_id
			saveplayer.p_price=request.POST.get('p_price')
			saveplayer.p_play_status=request.POST.get('p_play_status')
			saveplayer.t_role=request.POST.get('t_role')
			saveplayer.save()
			messages.success(request,"The Player "+saveplayer.p_name+" is added successfully...!")
			return render(request,"create_player.html")
		else:
			return HttpResponse("Not getting values")
	else:
		team_name=Team.objects.values('t_name').order_by('id')
		print(team_name)
		t_list=[]
		for course in team_name:
			print(course['t_name'])
			t_list.append(course['t_name'])
		context={'team_list':t_list}
		return render(request,"create_player.html",context)

def playerdetails(request,id):
	playerdetails=Player.objects.get(id=id)
	query_set=Player.objects.filter(id=id)
	query_set=serializers.serialize('json',query_set)
	p_icons=json.loads(query_set)
	# print(p_icon)
	p_icon='http://localhost:8000/'+p_icons[0]['fields']['p_photo']
	print(p_icon)
	# id=p_icon[0]['fields']['p_team']
	query_set=Team.objects.filter(id=int(p_icons[0]['fields']['p_team']))
	query_set=serializers.serialize('json',query_set)
	team_data=json.loads(query_set)
	print(team_data)
	team_name=team_data[0]['fields']['t_name']

	return render(request, "player_profile.html", {"Player":playerdetails,"p_icon":p_icon,"team_name":team_name})


def p_del(request,id):
	delplayer=Player.objects.get(id=id)
	delplayer.delete()
	results=Player.objects.all()
	return render(request, "t_details.html", {"Player":results})
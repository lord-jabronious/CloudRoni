from django.http import Http404
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from django.template import loader

from .models import Team, UserPlayer

def index(request):
    teams_list = Team.objects.order_by('-created_date')[:10]
    context = {
		'teams_list': teams_list,
	}
    return render(request, 'teams/index.html', context)

def team(request, team_id):
	team = get_object_or_404(Team, pk=team_id)
	return render(request, 'teams/detail.html', {'team': team}) 

def detail(request, team_id):
	response = "Here is a team %s!"
	return HttpResponse(response % team_id)

def players(request, team_id, player_id):
	player = get_object_or_404(UserPlayer, pk=player_id)
	team = get_object_or_404(Team, pk=team_id)
	context = {
		'player': player,
		'team': team
	}
	return render(request, 'players/index.html', context)
	#return HttpResponse("Here is a player {} from team # {}".format(player_id, team_id))
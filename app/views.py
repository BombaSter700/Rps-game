from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Player, Result

import random
import logging

log = logging.getLogger(__name__)

def home(request):
    if request.method == 'POST':
        playername = request.POST.get('name')
        if User.objects.filter(username__iexact=playername):
            messages.warning(request, 'This name is already taken. Please try another one.')
            return HttpResponseRedirect(request.path_info)

        create_user = User.objects.create(first_name=playername, username=playername)
        create_player = Player.objects.create(name=playername, user=create_user)
        return redirect('start_game')

    return render(request, 'index.html')


def game(request):
    gameList = ['rock', 'paper', 'scissor']
    bot_action = random.choice(gameList)
    user = Player.objects.all().last()

    if request.method == 'POST':
        user_answer = request.POST.get('name')
        status = "Tie"
        message = ""

        if user_answer == bot_action:
            message = "It's a tie!"
        elif user_answer == "rock" and bot_action == "scissors":
            status = "Win"
            message = "Rock smashes scissors! You win!"
        elif user_answer == "paper" and bot_action == "rock":
            status = "Win"
            message = "Paper covers rock! You win!"
        elif user_answer == "scissors" and bot_action == "paper":
            status = "Win"
            message = "Scissors cuts paper! You win!"
        else:
            status = "Lose"
            message = f"{bot_action.capitalize()} beats {user_answer}! You lose."

        Result.objects.create(player=user, bot_move=bot_action, user_move=user_answer, status=status)
        messages.add_message(request, messages.INFO if status == "Tie" else messages.SUCCESS if status == "Win" else messages.ERROR, message)

    return render(request, 'game.html', {'user': user})


def result(request):
    res = Result.objects.all().order_by('-id')
    context = {'res': res}
    return render(request, 'result.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Player, Result
import random

def home(request):
    if request.method == 'POST':
        playername = request.POST.get('name')
        if User.objects.filter(username__iexact=playername):
            messages.warning(request, 'This name is already taken. Please try another one.')
            return redirect('home')

        create_user = User.objects.create(first_name=playername, username=playername)
        create_player = Player.objects.create(name=playername, user=create_user)
        return redirect('start_game')

    return render(request, 'index.html')

def game(request):
    gameList = ['rock', 'paper', 'scissor']
    bot_action = random.choice(gameList)
    user = Player.objects.last()

    if request.method == 'POST':
        user_answer = request.POST.get('name')
        status = "Tie"

        if user_answer == bot_action:
            message = "It's a tie!"
        elif (user_answer == "rock" and bot_action == "scissors") or \
             (user_answer == "paper" and bot_action == "rock") or \
             (user_answer == "scissors" and bot_action == "paper"):
            status = "Win"
            message = "You win!"
        else:
            status = "Lose"
            message = f"You lose. {bot_action.capitalize()} beats {user_answer}."

        result = Result.objects.create(player=user, bot_move=bot_action, user_move=user_answer, status=status)

        # Check for series
        last_results = Result.objects.filter(player=user).order_by('-id')[:4]
        if len(last_results) == 4 and all(r.status == "Win" for r in last_results):
            for r in last_results:
                r.series = True
                r.save()

        messages.success(request, message if status == "Win" else message)

    return render(request, 'game.html', {'user': user})

def result(request):
    res = Result.objects.all().order_by('-id')
    return render(request, 'result.html', {'res': res})

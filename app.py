from flask import Flask, render_template, request, redirect, url_for
import random
import time

app = Flask(__name__)

choices = ['rock', 'paper', 'scissors']
emoji = {'rock': '🪨', 'paper': '📄', 'scissors': '✂️'}

def winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

memes_win = [
    "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2FtamFidDk0NTE3MTAxaWY4enZyMmxiNGZ3dHplNmI5cWR0a2ZocyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/10UeedrT5MIfPG/giphy.gif",  # Example funny meme
    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3MyZ2lzbTZ2enlnNmVyeTA5bTczZTZjcHF5YnVwdm9rbWU1YW8xeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YTtqB2j5EN7IA/giphy.gif"
]

memes_lose = [
    "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMG9hdWFpbDhmdmJybjhzN2t0emswd29qYzV2M3IzODVpZ2RmOHBnZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JUSwkiO1Eh5K43ruN0/giphy.gif",  # Example game over meme
    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3RoejQ5dnF2dHJ1dXp5am5pMXFzYWZ2dzEzZGZ5bHZhb20wcDN1bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qtgkm1xVilBFWD63CT/giphy.gif"
]

@app.route("/", methods=['GET', 'POST'])
def user_choice():
    if request.method == "POST":
        user = request.form.get('choice')
        computer = random.choice(choices)
        result = winner(user, computer)

        # Choose meme
        if "win" in result.lower():
            meme = random.choice(memes_win)
        elif "lose" in result.lower():
            meme = random.choice(memes_lose)
        else:
            meme = None  # tie

        # Render battle directly instead of redirect
        return render_template("battle.html", user=user, computer=computer, result=result, emoji=emoji, meme=meme)
    return render_template("user.html", choices=choices, emoji=emoji)

@app.route("/battle")
def battle():
    user = request.args.get('user')
    computer = request.args.get('computer')
    result = request.args.get('result')
    return render_template("battle.html", user=user, computer=computer, result=result, emoji=emoji)

if __name__ == "__main__":
    app.run(debug=True)
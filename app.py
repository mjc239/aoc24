from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from datetime import timedelta
import os

from aoc24.utils import solve_puzzle
from aoc24.forms import SolvePuzzleForm

app = Flask(__name__, 
            template_folder="app/templates", 
            static_folder='app/static')

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)

# Configure a secret key for CSRF protection
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'backup-key')
csrf = CSRFProtect(app)

# Configure Flask-Limiter
limiter = Limiter(get_remote_address, 
                  app=app, 
                  default_limits=["200 per day", "60 per hour"])

@app.route('/')
def index():
    """Render the homepage with links to each puzzle day."""
    return render_template('index.html')

@app.route('/day/<int:day>', methods=['GET', 'POST'])
@limiter.limit("5 per minute", methods=["POST"])
def puzzle_day(day):
    """Render each day's puzzle page and process the solution."""

    form = SolvePuzzleForm()
    solution = None

    if form.validate_on_submit():
        # Retrieve the user input
        user_input = form.user_input.data  

        # Load the correct function based on the day
        try:
            solution = solve_puzzle(day, user_input)
        except NotImplementedError:
            solution = 'Puzzle solution not yet implemented!'


    return render_template(f'dayX.html', form=form, solution=solution, day=day)

if __name__ == '__main__':
    app.run(debug=True)

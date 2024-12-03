from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired, Length, ValidationError

import re


def check_for_malicious_content(form, field):
    user_input = field.data

    # SQL injection patterns
    sql_keywords = r"(SELECT|INSERT|DELETE|UPDATE|DROP|UNION|\bOR\b)"

    # XSS patterns
    xss_patterns = r"(<script|<img|<iframe|<a|<div|<object|<embed|onload|onerror|onclick|alert|document\.cookie|eval|innerHTML|src)"

    # Command injection patterns
    command_injection_patterns = r"(rm|mv|cp|cat|ls|sudo|chmod|ping|wget|curl|uname)"

    # Path traversal patterns
    path_traversal_patterns = r"(/etc/passwd|C:\\Windows|/var/www)"

    # Obfuscation patterns
    obfuscation_patterns = r"(&#x|%[0-9a-fA-F]{2}|\\x[0-9a-fA-F]{2})"

    # Check each pattern
    if re.search(sql_keywords, user_input, re.IGNORECASE):
        raise ValidationError("SQL keywords detected in input.")
    if re.search(xss_patterns, user_input, re.IGNORECASE):
        raise ValidationError("Potentially unsafe HTML or JavaScript content detected.")
    if re.search(command_injection_patterns, user_input, re.IGNORECASE):
        raise ValidationError("Potentially unsafe command detected in input.")
    if re.search(path_traversal_patterns, user_input, re.IGNORECASE):
        raise ValidationError("Potentially unsafe file path detected.")
    if re.search(obfuscation_patterns, user_input):
        raise ValidationError("Potentially unsafe encoding detected in input.")


def load_test_data(day):
    with open(f"tests/data/test_day{day}.txt", "r") as f:
        test_input = f.read()
    return test_input


class SolvePuzzleForm(FlaskForm):

    user_input = TextAreaField(
        "Enter Puzzle Input",
        validators=[
            DataRequired(),
            Length(min=1, max=50000, message="Puzzle input too long."),
            check_for_malicious_content,
        ],
    )

    solve_part = RadioField(
        "Solve Part",
        choices=[(1, "Part 1"), (2, "Part 2")],
        validators=[DataRequired()],
    )

    submit = SubmitField("Solve Puzzle")

    def __init__(self, day, *args, **kwargs):
        super(SolvePuzzleForm, self).__init__(*args, **kwargs)
        self.day = day
        self.test_input = load_test_data(self.day)

        # Set the default value dynamically
        self.user_input.data = self.test_input

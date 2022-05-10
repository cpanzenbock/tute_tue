from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, EqualTo, Email


class DestinationForm(FlaskForm):
    name = StringField('Country', validators=[InputRequired(), Length(min=1)])
    description = TextAreaField('Description', validators=[InputRequired()])
    image = StringField('Cover Image', validators=[InputRequired()])
    currency = StringField('Currency', validators=[InputRequired()])
    submit = SubmitField("Create")

# User login


class LoginForm(FlaskForm):
    user_name = StringField("User Name", validators=[
                            InputRequired('Enter user name')])
    password = PasswordField("Password", validators=[
                             InputRequired('Enter user password')])
    submit = SubmitField("Login")

# User register


class RegisterForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[
                           Email("Please enter a valid email", check_deliverability=True)])

    # linking two fields - password should be equal to data entered in confirm
    password = PasswordField("Password", validators=[InputRequired(),
                                                     EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    # submit button
    submit = SubmitField("Register")


class CommentForm(FlaskForm):
    text = TextAreaField('Comment', [InputRequired(), Length(1)])
    submit = SubmitField('Create')

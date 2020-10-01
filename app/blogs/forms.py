from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    title = StringField('Blog Title', validators=[Required()])
    blog = TextAreaField('Create a Blog...')
    submit = SubmitField('submit')

class CommentsForm(FlaskForm):

    comment= TextAreaField('make comments', validators=[Required()])
    submit = SubmitField('Submit')

class SubscriptionForm(FlaskForm):

    email= TextAreaField('Enter your Email', validators=[Required()])
    submit = SubmitField('Submit')

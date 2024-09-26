from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, URL
# from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()], render_kw={'autofocus': True})
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()], default="https://imgs.search.brave.com/BW__i2u-_aUDX7WcqOc0ZZIrdXUDN73s-jcnwRqSN8k/rs:fit:1024:704:1/g:ce/aHR0cHM6Ly9zdGF0/aWMwMS5ueXQuY29t/L2ltYWdlcy8yMDEx/LzAxLzE0L2FydHMv/MTRNT1ZJTkctc3Bh/bi9NT1ZJTkctanVt/Ym8uanBn")
    # body = CKEditorField("Blog Content", validators=[DataRequired()])
    body = TextAreaField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Post", render_kw={'class':'btn btn-primary btn-sm','style':'font-size:80%'})


# RegisterForm to register new users
class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], render_kw={'autofocus': True})
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField("Sign Up")

# LoginForm to login existing users
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()], render_kw={'autofocus': True})
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField("Login")

# CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    comment = TextAreaField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit", render_kw={'class':'btn btn-primary btn-sm','style':'font-size:80%'})
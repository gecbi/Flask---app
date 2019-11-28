from flask_wtf import FlaskForm
from wtfforms import StringField, SubmitField, TextAreaField
from wtf.validators import DataRequirered

class BlogPostForm(FlaskForm):
    title = StringField('Title', validators = [DataRequirered()])
    text = TextAreaField('Text', validators = [DataRequirered()])
    submit = SubmitField("Post")
    #ksdbfksdjhfkj

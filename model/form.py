from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField ,IntegerField
from wtforms.validators import InputRequired, NumberRange 

class PredictForm(FlaskForm):
    age = IntegerField(' age', validators=[InputRequired(), NumberRange(min=1,max=100)])
    Gender = StringField('Gender', validators=[InputRequired()])
    self_employed = StringField('self_employed ', validators=[InputRequired()])
    family_history = StringField('family_history', validators=[InputRequired()])
    work_interfere = StringField('work_interfere', validators=[InputRequired()])
    no_employees= StringField('no_employees', validators=[InputRequired()])
    remote_work= StringField('remote_work', validators=[InputRequired()])
    tech_company = StringField('tech_company ', validators=[InputRequired()])
    benefits = StringField('benefits', validators=[InputRequired()])
    care_options = StringField('care_options', validators=[InputRequired()])
    wellness_program = StringField('wellness_program', validators=[InputRequired()])
    seek_help = StringField('seek_help', validators=[InputRequired()])
    anonymity = StringField('anonymity', validators=[InputRequired()])
    leave = StringField('leave', validators=[InputRequired()])
    mental_health_consequence = StringField('mental_health_consequence', validators=[InputRequired()])
    phys_health_consequence = StringField('phys_health_consequence ', validators=[InputRequired()])
    coworkers = StringField('coworkers', validators=[InputRequired()])
    supervisor = StringField('supervisor', validators=[InputRequired()])
    mental_health_interview = StringField('mental_health_interview', validators=[InputRequired()])
    phys_health_interview = StringField('phys_health_interview', validators=[InputRequired()])
    mental_vs_physical= StringField('mental_vs_physical', validators=[InputRequired()])
    obs_consequence= StringField('obs_consequenc', validators=[InputRequired()])
    submit = SubmitField('Predict')
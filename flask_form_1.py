from flask import Flask, render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from bs4 import BeautifulSoup
import requests
from wtforms.fields import DateField
import json
import matplotlib.pyplot as plt
from io import BytesIO
import urllib.parse
import base64
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from  chat_bot import *


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


class InfoForm(FlaskForm):
    link = StringField("https://petition.parliament.uk/")
    submit = SubmitField('Let parse it')

class InfoForm2(FlaskForm):

    link2 = StringField("https://faucetpay.io/page/faucet-list/")
    submit = SubmitField('Let parse it')

class DatePicker(FlaskForm):
    dStart = DateField('Start date', format='%Y-%m-%d')
    dEnd = DateField('End date', format='%Y-%m-%d')

class Currency(FlaskForm):
    valuta = StringField('Pick currency')

class UsersInfo(FlaskForm):
    name = StringField('', validators=[DataRequired(message='Name is required')])
    surname = StringField('Enter your surname:', validators=[DataRequired(message='Surname is required')])
    age = StringField('Enter your age:', validators=[DataRequired(message='Age is required')])
    submit = SubmitField('Add user')
    delete = SubmitField('Delete user')

class ChatForm(FlaskForm):
    question = StringField("")
    submit = SubmitField('Submit')

# create table for page SQlite
class Users(db.Model):

    __tablename__='users'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text)
    surname=db.Column(db.Text)
    age=db.Column(db.Integer)

    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
 # view of rows of the table       
    def __repr__(self):
        return f"Name,surname and age: {self.name},{self.surname},{self.age}"

@app.route('/')
def index():

    return render_template('index.html') 

@app.route('/graphs')
def graphs():

    return render_template('graphs.html') 

@app.route('/ml', methods=['GET', 'POST'])
def ml():
    
    form = ChatForm()

    userText = None
   
    if form.validate_on_submit():
        userText = form.question.data
        form.question.data = ''

    else:
        return render_template('ml.html', form=form)

    return render_template('ml.html', form=form, answer=get_bot_response(userText)) 


# view of table with small sqlite crud
@app.route('/sq_lite', methods=['GET', 'POST'])
def sq_lite():
    
    form = UsersInfo()

    if form.validate_on_submit():
# crate and add user
        if form.submit.data:
            new_user = Users(name = form.name.data,
            surname = form.surname.data,
            age = form.age.data)

            db.session.add(new_user)
            db.session.commit()
# delete user from the table
        if form.delete.data:
            name = form.name.data
            del_user = Users.query.filter(Users.name == name).first()

            db.session.delete(del_user)
            db.session.commit()

    return render_template('sq_lite.html', form=form, users=list())
# query tosqlite to display all users in the table
def list():
    users = Users.query.all()
    return users

# view with form of choosing dates and currency to plot
@app.route('/api_out', methods=['GET', 'POST'])
def api_out():
    form = DatePicker()
    colours = ['USD', 'EUR', 'PLN', 'GBP']
    zaput={}
    resultval=[]
# choose dates and currency and send request to api in json
    if form.validate_on_submit():
        start_date=form.dStart.data.strftime('%Y%m%d')
        end_date=form.dEnd.data.strftime('%Y%m%d')
        # return ({'st':start_date,'ed':end_date,'val':test()})
        zaput.update({'st':start_date,'ed':end_date,'val':test()})
        resultval=list(zaput.values())
    else:
        return render_template('api out.html', form=form, colours=colours)
    return render_template('api out.html', form=form, colours=colours,mygraph=grafik_val(resultval))
# pick currency from the select
def test():
    select = request.form.get('valcodes')
    return(str(select))
# takes a list of values[date,date,currency] and send request to api, after receiving answer to make plot out that info 
def grafik_val(k):
    # api url for request 
    url = f'https://bank.gov.ua/NBU_Exchange/exchange_site?start={k[0]}&end={k[1]}&valcode={k[2]}&sort=exchangedate&order=asc&json'
    response = requests.get(url)

    # retrive response in json format
    data = response.json()
    # from json data create a first list with dates and second list with currency rates for plot
    rates=[]
    exchangedates=[]
    rates = list(map(lambda i: i.get('rate'), data))
    exchangedates=list(map(lambda i: i.get('exchangedate'), data))

    # Put dates on the x-axis
    x = exchangedates
    # Put exchange rates on the y-axis
    y = rates
    # Specify the width and height of a figure in unit inches
    fig = plt.figure(figsize=(15,6))
    # Rotate the date ticks on the x-axis by degrees
    plt.xticks(rotation=90)
    # Set title on the axis
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Exchange Rates', fontsize=12)
    # Plot the data
    plt.plot(x,y)
    # in memory img
    img = BytesIO()
    plt.savefig(img, format='png')
    # plt.close()
    img.seek(0)
    # convert data in different binary formats to a string of ASCII characters to send to html page
    return urllib.parse.quote(base64.b64encode(img.read()).decode())
    
    
# func for first parsing input
def pars(url=None):
    
    if url in [False,None,'']:
        pass
    else:
        headers = {'User-Agent': "Edge/12.246"}
        page = requests.get(url,headers=headers)
        table=[]
        table2=[]
        allNews =[]
        allNews2 = []

        soup = BeautifulSoup(page.content, "html.parser")

        allNews = soup.findAll('blockquote', attrs={'class':['pull-quote']})
        for i in allNews:
            table.append(i.find('p').text)

        allNews2 = soup.findAll('p', attrs={'class':['intro']})
        for i in allNews2[:3]:
            table2.append(i.text)
          
        return [j+'\n - '+k for j,k in zip(table,table2)]
            
# func for second parsing input
def pars2(url2=None):
    
    if url2 in [False,None,'']:
        pass
    else:
        headers = {'User-Agent': "Edge/12.246"}
        page = requests.get(url2,headers=headers)
        allNews=[]
        table2=[]

        soup = BeautifulSoup(page.content, "html.parser")

        allNews = soup.findAll('i', attrs={'class':'far fa-star'})

        names=[]
        for y in allNews:
            table2.append(y.find_next('td')) # names of firms
        for b in table2:
            names.append(b.text)

        table3=[]
        for y in table2:
            table3.append(y.find_next('td')) # price 
        Total_Paid_this_week=[]
        for b in table3:
            Total_Paid_this_week.append(b.text)   
       
        table4=[]
        for y in table3:
            table4.append(y.find_next('td')) #   
        Total_Paid_Today=[]    
        for y in table3:
            Total_Paid_Today.append(y.text) #  
                  
        table5=[]
        for y in table4:
            table5.append(y.find_next('td')) # 
        Total_U_Paid_Today=[]    
        for y in table5:
            Total_U_Paid_Today.append(y.text) #  
            
        Upvotes=[]    
        for y in table5:
            Upvotes.append(y.find_next('td').text) # 

        final=[]
        for j,k,h,t in zip(names,Total_Paid_this_week,Total_Paid_Today,Total_U_Paid_Today):
            final.append(j+' - '+k+' - '+h+' - '+t)
            
        return final  
# show forms with parsing sites
@app.route('/parser', methods=['GET', 'POST'])
def parser():

    link = False
    link2 = False

    form = InfoForm()
    form2 = InfoForm2()
    
    if form.validate_on_submit():

        link = form.link.data   
        form.link.data = '' 
        
    if form2.validate_on_submit():
        
        link2 = form2.link2.data 
        form2.link2.data = ''         
       
    return render_template('flask form 1.html',link=link,link2=link2, form=form,form2=form2, output1=pars(link),output2=pars2(link2))

    
if __name__=='__main__':
    app.run(debug=True)
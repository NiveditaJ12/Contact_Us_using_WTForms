from flask import Flask, render_template
from forms import ContactForm


app = Flask(__name__)
app.secret_key = 'mycontactform'

@app.route('/', methods = ['GET','POST'])
def index():
    cform = ContactForm()
    if cform.validate_on_submit():
        print(f'Name:{cform.name.data}, Email: {cform.email.data}, Message:{cform.message.data}')
    else:
        print('Invalid Credentials')
    return render_template('contact.html', form=cform)
    
if __name__ == '__main__':
    app.run(debug=True)
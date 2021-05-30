from flask import Flask,render_template, url_for , request , redirect 

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQL_DATABASE_URI']= 'sqlite:///root.db'

db=SQLAlchemy(app)

class Task(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    fname=db.Column(db.String(50), nullable=False)
    lname=db.Column(db.String(50), nullable=False)
    email=db.Column(db.String(200), nullable=False)
    msg=db.Column(db.String(400), nullable=False)
    
def __tsl__(self):
    return '<Entry%r>' $self.id

from app import db
db.create_all


@app.route('/', methods=['POST','GET'])
def index():
        if request.method=='POST':
            entry_fname=request.form['fname']
            new_entry=Task(fname=entry_fname)
            try:
                db.session.add(new_entry)
                db.session.commit()
                return redirect('/')
            except:
                    return "Error"

        else:   
            entries=Task.query.order_by(Task.fname.added).all()
            return render_template ('contacts.html', entries=entries) 

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete=Task.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/contacts')
    except:
        return "Error deleting contact"    


@app.route("/home")
def home():
    return render_template(index.html)

@app.route("/contacts")
def contacts():
    return render_template(contacts.html)

    if __name__ =="__main__":
         app.run(debug=True)



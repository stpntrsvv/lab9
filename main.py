from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask('Furniture store')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project1.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(300))
    term = db.Column(db.Integer)

    def __repr__(self):
        return f'Company{self.id}. {self.company_name} - {self.term} months.'


@app.route('/')
def main():
    companies = Company.query.all()
    return render_template('index.html', companies_list=companies)


@app.route('/add', methods=['POST'])
def addCompany():
    data = request.json
    company = Company(**data)
    db.session.add(company)
    db.session.commit()

    # id_last = products[-1]['id']
    # id_new = id_last + 1
    # data['id'] = id_new
    # products.append(data)
    return 'OK'



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
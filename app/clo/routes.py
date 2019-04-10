from app.clo import bp
from flask import render_template, flash, jsonify
from flask_login import current_user, login_required
from app.models import Clo
from app.clo.forms import CreateCloForm, DeleteCloForm, ReadCloForm, UpdateCloForm
from app import db

@bp.route('/index', methods=['GET', 'POST'])
def index():
    clos = Clo.query.all()
    print (clos)
    return render_template('clo/index.html', clos=clos)



@bp.route('/create', methods=['GET', 'POST'])
def create():
    form = CreateCloForm()
    if form.validate_on_submit():
        clo = Clo(general = form.cloGeneral.data, specific = form.cloSpecific.data)
        db.session.add(clo)
        db.session.commit()
        flash("CLOCreated!")
    return render_template('clo/create.html', title="CLO Create", form=form)



@bp.route('/read/<id>', methods=['GET', 'POST'])
def read(id):
    form = ReadCloForm()
    if form.validate_on_submit():
        clo = Clo.query.filter_by(id = int(form.cloID.data)).one()
        #print(clos)
        flash("CLO Read!")
    return render_template('/clo/read.html', title="CLO Read", form=form)



@bp.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    form = UpdateCloForm()
    if form.validate_on_submit():
        clo = Clo.query.filter_by(id = int(form.cloID.data)).one()
        if form.cloGeneral.data != '':
            clo.general = form.cloGeneral.data
        if form.cloSpecific.data != '':
            clo.specific = form.cloSpecific.data
        db.session.commit()
        flash("CLO Updated!")
    return render_template('/clo/update.html', title="CLO Update", form=form)



@bp.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    form = DeleteCloForm()
    if form.validate_on_submit():
        clo = Clo.query.filter_by(id = int(form.cloID.data)).one()
        db.session.delete(clo)
        db.session.commit()
        flash("CLO removed! " + form.cloID.data)
    return render_template('/clo/delete.html', title="CLO Delete", form=form)

from flask import Blueprint, render_template, redirect, url_for, request
from .models import Destination, Comment
from .forms import DestinationForm, CommentForm
from . import db

# Use of blue print to group routes,
# name - first argument is the blue print name
# import name - second argument - helps identify the root url for it
bp = Blueprint('destination', __name__, url_prefix='/destinations')


@bp.route('/create', methods=['GET', 'POST'])
def create():
    print('Method type: ', request.method)
    form = DestinationForm()
    if form.validate_on_submit():
        destination = Destination(name=form.name.data,
                                  description=form.description.data,
                                  image=form.image.data,
                                  currency=form.currency.data)
        # add the object to the db session
        db.session.add(destination)
        # commit to the database
        db.session.commit()
        # Always end with redirect when form is valid
        return redirect(url_for('destination.create'))
    return render_template('destinations/create.html', form=form)


# @bp.route('/<id>')
# def any_dest(id):
#     return redirect(url_for('destination.show'))


@bp.route('/<id>')
def show(id):
    destination = Destination.query.filter_by(name=id).first()
    comment_form = CommentForm()
    return render_template('destinations/show.html', destination=destination, form=comment_form)


@bp.route('/<id>/comment', methods=['GET', 'POST'])
def comment(id):
    # here the form is created  form = CommentForm()
    form = CommentForm()
    if form.validate_on_submit():  # this is true only in case of POST method
        print("The following comment has been posted:", form.text.data)
    # notice the signature of url_for
    return redirect(url_for('destination.any_dest', id=id))


def get_destination():
    # creating the description of Brazil
    b_desc = """Brazil is considered an advanced emerging economy.
   It has the ninth largest GDP in the world by nominal, and eight by PPP measures. 
   It is one of the world\'s major breadbaskets, being the largest producer of coffee for the last 150 years."""
    # an image location
    image_loc = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFyC8pBJI2AAHLpAVih41_yWx2xxLleTtdshAdk1HOZQd9ZM8-Ag'
    destination = Destination('Brazil', b_desc, image_loc, '10 R$')
    # a comment
    comment = Comment(
        "Sam", "Visited during the olympics, was great", '2019-11-12 11:00:00')
    destination.set_comments(comment)
    comment = Comment("Bill", "free food!", '2019-11-12 11:00:00')
    destination.set_comments(comment)
    comment = Comment("Sally", "free face masks!", '2019-11-12 11:00:00')
    destination.set_comments(comment)
    return destination

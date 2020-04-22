from flask import render_template
from app import app

@app.errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 erro page
    '''
    return render_template('fourOwfour.html'), 404
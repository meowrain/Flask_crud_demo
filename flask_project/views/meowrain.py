from flask import Blueprint

meowrains = Blueprint('meowrain',__name__)
 
@meowrains.route('/about')
def about():
    return '''
    <h2>Here is meowrain</h2>
    '''
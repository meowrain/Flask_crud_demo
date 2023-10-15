from flask_project import create_app
from flask_project import *
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
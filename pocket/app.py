import os
from flask import Flask
from flask_restplus import Namespace


from pocket.resources.products import ProductView


basedir = os.path.abspath(os.path.dirname(__file__))

nsp = Namespace('product', description='something')
nsp.add_resource(ProductView, '/')


def create_db(app, db):
    if not os.path.isfile(os.path.join(basedir, 'db.sqlite')):
        with app.app_context():
            db.create_all()


def create_app():
    app = Flask(__name__)


    # Database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')  # noqa
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from pocket import db, ma, api
    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)
    api.add_namespace(nsp)

    create_db(app, db)

    return app


def create_context_debug():
    app = create_app()
    app.app_context().push()


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)

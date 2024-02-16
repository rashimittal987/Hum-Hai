from flask import Flask


def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='grdfj flkykgdyfghcugyfvhboifrhfikds/'
    from .views import views
    from.auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/auth/')
    return app
#6 2 15 9 18 11 18 15 5 2 7 7
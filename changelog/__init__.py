"""Main entry point
"""
from pyramid.config import Configurator

from pyramid.security import Allow, Authenticated

from sqlalchemy import engine_from_config, event
from sqlalchemy.orm import scoped_session, sessionmaker

from pyramid_beaker import session_factory_from_settings

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy


from .models.models import ( DBSession, Base)
from .security import (groupfinder, LookupUser)

class Root(object):
    __acl__ = [
        (Allow, Authenticated, 'user'),
        (Allow, 'g:admin', 'admin'),
    ]

    def __init__(self, request):
	pass

def _execute_pragma_on_connect(dbapi_con, con_record):
        dbapi_con.execute('pragma foreign_keys=ON')

def GetDB(request):
  return DBSession

  def cleanup(request):
    session.close()
  request.add_finished_callback(clceanup)

  return session

def main(global_config, **settings):
    NotSoSecret='CIeUz0RK8fjRq1wJSrID' 
    authn_policy = AuthTktAuthenticationPolicy(NotSoSecret,callback=groupfinder, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()

    engine = engine_from_config(settings, 'sqlalchemy.')
    event.listen(engine, 'connect', _execute_pragma_on_connect)
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings, root_factory=Root)
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy) 
    config.include('velruse.providers.google_oauth2')
    session_factory = session_factory_from_settings(settings)
    config.set_session_factory(session_factory)
    config.add_google_oauth2_login_from_settings(prefix='velruse.google.')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('logout', '/logout')
    config.add_route('ListChangelogs', '/changelogs')
    config.add_route('GetChangelog', '/changelog/{id}')
    config.add_route('home', '/')
    config.scan("changelog.views")

    config.add_request_method(LookupUser, 'user', reify=True)
    config.add_request_method(GetDB, 'db', reify=True)


    return config.make_wsgi_app()

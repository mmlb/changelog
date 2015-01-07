import pyramid.session
from pyramid.response import Response
from pyramid.view import view_config
import json
import pdb
from sqlalchemy.orm.exc import (
	NoResultFound
)

from changelog.models.models import DBSession
from changelog.models.models import UserModel

from pyramid.httpexceptions import HTTPFound, HTTPForbidden

from pyramid.security import remember, forget

@view_config(
  context='velruse.AuthenticationComplete',
  renderer='flower:templates/AuthComplete.mako',
)
def login_complete_view(request):
  context = request.context
  result = {
    'provider_type': context.provider_type,
    'provider_name': context.provider_name,
    'profile': context.profile,
    'credentials': context.credentials,
  }
  email = context.profile['verifiedEmail']
  try:
    User = request.db.query(UserModel).filter(UserModel.email==email).one()
  except NoResultFound, e:
    User = UserModel()
    User.email = email
    User.AccessLevel = 1
    request.db.add(User)
    request.db.flush()

  if hasattr(request.session,'goingto'):
    loc = request.session['goingto']
  else:
    loc = request.route_url('ListChangelogs', _query=(('next', request.path),))

  headers = remember(request, User.email)
  return HTTPFound(location=loc, headers=headers)





  return {'result':json.dumps(result, indent=4)}


@view_config(
  context='velruse.AuthenticationDenied',
  renderer='myapp:templates/LoginFailure.mako'
)
def login_denied_view(request):
  return { 'result': 'denied' }


@view_config(route_name='logout')
def logout_view(request):
  headers = forget(request)
  loc = request.route_url('home', _query=(('next', request.path),))
  return HTTPFound(location=loc,headers=headers)

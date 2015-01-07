from pyramid.response import Response
from pyramid.view import view_config
from pyramid.security import authenticated_userid
from velruse import login_url

@view_config(route_name='home', renderer='changelog:templates/home.mak')
def ViewHome(request):
    logged_in=authenticated_userid(request)
    loginurl = login_url(request, 'google')
    return {"loginurl": loginurl,"logged_in":logged_in,"logouturl": request.route_url('logout')}


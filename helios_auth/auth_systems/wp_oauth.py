"""
WordPress OAuth Authentication
Compatible with WP OAuth Server plugin

"""

import httplib2
from django.conf import settings
from django.core.mail import send_mail
from oauth2client.client import OAuth2WebServerFlow

from helios_auth import utils
import json

# some parameters to indicate that status updating is not possible
STATUS_UPDATES = False

# display tweaks
LOGIN_MESSAGE = "Log in with my WordPress Account"

def get_flow(redirect_url=None):
  x =  OAuth2WebServerFlow(client_id=settings.WP_OAUTH_CLIENT_ID,
            client_secret=settings.WP_OAUTH_CLIENT_SECRET,
            scope='basic',
            redirect_uri=redirect_url,
            auth_uri=settings.WP_OAUTH_ROOT_URI+'/authorize',
            token_uri=settings.WP_OAUTH_ROOT_URI+'/token',
            revoke_uri=settings.WP_OAUTH_ROOT_URI+'/destroy')
  return x

def get_auth_url(request, redirect_url):
  flow = get_flow(redirect_url)

  request.session['wp-oauth-redirect-url'] = redirect_url
  return flow.step1_get_authorize_url()

def get_user_info_after_auth(request):
  flow = get_flow(request.session['wp-oauth-redirect-url'])

  if 'code' not in request.GET:
    return None
  
  code = request.GET['code']
  credentials = flow.step2_exchange(code)

  # get the nice name
  http = httplib2.Http(".cache")
  http = credentials.authorize(http)
  (resp_headers, content) = http.request(settings.WP_OAUTH_ROOT_URI+'/me', "GET")

  response = json.loads(content.decode())

  name = response['display_name']
  email = response['user_email']
  user_login = response['user_login']
  
  return {'type' : 'wp_oauth', 'user_id': user_login, 'name': name , 'info': {'email': email}, 'token':{}}
    
def do_logout(user):
  """
  logout of WP
  """
  return None
  
def update_status(token, message):
  """
  simple update
  """
  pass

def send_message(user_id, name, user_info, subject, body):
  """
  send email to WP users.
  """
  send_mail(subject, body, settings.SERVER_EMAIL, ["%s <%s>" % (name, user_info['email'])], fail_silently=False)
  
def check_constraint(constraint, user_info):
  """
  for eligibility
  """
  pass


#
# Election Creation
#

def can_create_election(user_id, user_info):
  return True

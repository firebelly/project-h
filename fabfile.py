from fabric.api import *
import os

env.hosts = ['projecthdesign.org']
env.user = 'projecth'
env.path = '~/Sites/project-h'
env.remotepath = '/home/projecth/webapps/projecth_redirecdtion'
env.git_branch = 'master'
env.warn_only = True
env.remote_protocol = 'http'

def build():
  local('npx gulp --production')

def deploy():
  update()

def update():
  with cd(env.remotepath):
    run('git pull origin {0}'.format(env.git_branch))

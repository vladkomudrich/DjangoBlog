import os
import time

from fabric.api import run, env, cd, roles, sudo

env.roledefs['production'] = ['']

def production_env():
    env.use_ssh_config = True
    env.key_filename = [os.path.join(os.environ['HOME'], '.ssh', 'id_rsa')]
    env.user = ''
    env.host_string = ''
    env.project_root = '/path/to/app'
    env.python = '/path/to/python'
    env.pip = '/path/to/pip'
    env.uwsgi = '/path/to/uwsgi'

@roles('production')
def deploy():
    production_env()
    with cd(env.project_root):
        run('git pull origin master')
        run('{pip} install -Ur requirements.txt'.format(**env))
        run('{python} manage.py makemigrations'.format(**env))
        run('{python} manage.py migrate'.format(**env))
        run('{python} manage.py collectstatic --noinput'.format(**env))
        restart()

@roles('production')
def git_pull():
    production_env()
    with cd(env.project_root):
        run('git pull origin master')

@roles('production')
def git_fetch():
    production_env()
    with cd(env.project_root):
        run('git fetch')

@roles('production')
def git_merge():
    production_env()
    with cd(env.project_root):
        run('git merge')

@roles('production')
def start():
    production_env()
    with cd(env.project_root):
        run('{uwsgi} uwsgi/uwsgi.ini'.format(**env))

@roles('production')
def stop():
    production_env()
    run('killall -9 uwsgi', quiet=True)

@roles('production')
def restart():
    stop()
    time.sleep(2)
    start()

@roles('production')
def nginx_restart():
    production_env()
    sudo('/usr/sbin/nginx -s reload')

@roles('production')
def create_user():
    production_env()
    with cd(env.project_root):
        run('{python} manage.py createsuperuser'.format(**env))
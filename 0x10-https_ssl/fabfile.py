"""
Configures load balancer for ssl
"""
from fabric.api import env, run

env.host_string = '54.175.26.198'
env.hosts = ['54.175.26.198', 'bla']
env.user = 'ubuntu'


def setup_ssl():
    if not run('sudo apt-get -y update'):
        return False
    if not run('sudo apt-get -y install snapd'):
        return False

    run('sudo apt-get -y remove certbot')

    if not run('sudo snap install --classic certbot'):
        return False

    if not run('sudo ln -s /snap/bin/certbot /usr/bin/certbot'):
        return False
    if not run('sudo certbot certonly --standalone'):
        return False
    return True


setup_ssl()

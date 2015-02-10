from fabric.api import task  # , env

# import the fabric tasks and templates from cotton
from cotton.fabfile import set_env, project, postfix, iojs, util

# load application-specific settings from this module
set_env('cotton_settings')


@task
def init():
    """
    Initialize the app deployment
    """
    project.create()
    iojs.install()
    postfix.install()


@task
def ship():
    """
    Deploy the current branch to production
    """
    project.git_push()
    iojs.install_dependencies()
    util.upload_template_and_reload('nginx')

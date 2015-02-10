from fabric.api import task  # , env

# import the fabric tasks and templates from cotton
from cotton.fabfile import set_env, system, project, mysql, postfix, iojs

# load application-specific settings from this module
set_env('cotton_settings')


@task
def init():
    """
    Initialize the app deployment
    """
    project.create_project()
    iojs.install()
    postfix.install()


@task
def ship():
    """
    Deploy the current branch to production
    """
    system.git_push()
    iojs.install_dependencies()
    system.upload_template_and_reload('nginx')

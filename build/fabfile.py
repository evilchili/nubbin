from fabric.api import task  # , env

# import the fabric tasks and templates from cotton
import cotton.fabfile as cotton

# load application-specific settings from this module
cotton.set_fabric_env('cotton_settings')


@task
def init():
    """
    Initialize the app deployment
    """
    cotton.create_project()
    cotton.install_iojs()


@task
def ship():
    """
    Deploy the current branch to production
    """
    cotton.git_push()
    cotton.install_iojs_dependencies()
    cotton.upload_template_and_reload('nginx')

import click


@click.command()
@click.argument('name')
def cli(name):
    """
    Run flake8 to analyze your code base.

    :param skip_init: Skip checking __init__.py files
    :param path: Test coverage path
    :return: Subprocess call result
    """

    cmd = click.echo("Hi " + name)
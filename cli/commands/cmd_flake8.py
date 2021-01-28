import subprocess

import click

@click.command()
@click.option('--skip-init/--no-skip-init', default=True,
            help='skip __initt__.py fies?')
@click.argument('path', default='snakeeyes')
def cli(skip_init, path):
    """
    Run flake8 to analyze code base.

    :param skip_init: Skip checking __init__.py files
    :param path: flake8 coverage path
    :return: subprocess call result
    """
    flake8_flag_exclude=''

    if skip_init:
        flake8_flag_exclude = '--exclude __init__.py'

    cmd = 'flake8 {0}{1}'.format(path, flake8_flag_exclude)
    return subprocess.call(cmd, shell=True)
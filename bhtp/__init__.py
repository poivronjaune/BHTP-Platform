# __init__.py
import click
from bhtp import messages
from bhtp.cli import config, actions

@click.group(invoke_without_command=True)
@click.version_option()
@click.pass_context
def cli(ctx) -> None:
    if ctx.invoked_subcommand is None:
        messages.welcome()
        ctx.exit()
    
cli.add_command(config.config)
cli.add_command(actions.first)

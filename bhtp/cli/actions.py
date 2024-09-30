# actions.py
import click

@click.command(name='first')
@click.pass_context
def first(ctx):
    '''Show first command message'''
    click.echo(f"BHTP-CLI first command")


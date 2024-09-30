import click

def welcome():
    click.echo(f"BHTP-CLI: Brothers Hobby Trading Platform, 'bhtp --help' for commands")

def bad_config_file():
    click.echo(
            click.style('Error:', fg='red') + 
            f' Bad config file, use "config create to fix it..."'
        )

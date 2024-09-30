# cli_config.py
import click
import os
import json
from bhtp import messages

# Default Click configuration paths for some OS Plaforms
### LINUX : ~/.config/bhtp/
### macOS : ~/Library/Application Support/bhtp/
### Windows: %APPDATA%\bhtp\
CONFIG_DIR = os.path.join(click.get_app_dir("bhtp"))
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)
    
def save_config(config):
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

def validate_and_create_path(data_path):
    # Check if the path is absolute or relative, and expand it to full path
    full_path = os.path.abspath(os.path.expanduser(data_path))

    # Check if the path already exists
    if not os.path.exists(full_path):
        try:
            # Create the directory
            os.makedirs(full_path)
            click.echo(f"Directory {full_path} created.")
        except Exception as e:
            raise click.ClickException(f"Failed to create directory: {str(e)}")
    elif not os.path.isdir(full_path):
        # If it exists but is not a directory, raise an error
        raise click.ClickException(f"{full_path} exists but is not a directory.")
    
    return full_path


@click.group()
def config():
    """Manage BHTP configuration."""
    pass        

@config.command()
@click.option('--username', prompt=True, help="Your username.")
@click.option('--email', prompt=True, help="Your email address.")
@click.option('--data', prompt=True, help="Preferred local datastorage path, use ./DATA")
def set(username, email, data):
    """Set the username and email."""
    data_path = validate_and_create_path(data)

    config_data = load_config()
    config_data['username'] = username
    config_data['email'] = email
    config_data['datastore'] = data_path
    save_config(config_data)
    click.echo("Configuration updated!")

@config.command()
def show():
    """Show the current configuration."""
    config_data = load_config()
    if not config_data:
        click.echo("No configuration found.")
    else:
        click.echo(f"Username: {config_data.get('username', 'Not set')}")
        click.echo(f"Email: {config_data.get('email', 'Not set')}")

@config.command()
def path():
    """Show default location of configuration file"""
    not_created = not os.path.exists(CONFIG_FILE)
    click.echo(f"Config path: {CONFIG_DIR}, {'Not created yet'*not_created}")

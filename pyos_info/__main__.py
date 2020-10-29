import click

from . import get_os_info


@click.command(name="show_info", help="Show OS Information")
@click.help_option("-h", "--help")
def show_info():
    info = get_os_info()
    for k, v in info.items():
        print(click.style(k, fg="green", bold=True), ":", click.style(v, fg="white"))


if __name__ == "__main__":
    cli()
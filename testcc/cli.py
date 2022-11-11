"""Console script for testcc."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("testcc")
    click.echo("=" * len("testcc"))
    click.echo("Skeleton project created by Cookiecutter PyPackage")


if __name__ == "__main__":
    main()  # pragma: no cover

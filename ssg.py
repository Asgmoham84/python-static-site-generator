import typer
from ssg.site import Site


def main(source="cpntent", dest="dist"):
    config = {"source": source, "dest": dest}
    site = Site(source=config["source"], dest=config["dest"])
    site.build()


typer.run(main)

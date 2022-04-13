import typer
from ssg.site import Site
import ssg.parsers

def main(source="cpntent", dest="dist"):
    config = {"source": source, "dest": dest, "parsers":[ssg.parsers.ResourceParser()]}
    site = Site(source=config["source"], dest=config["dest"])
    site.build()

typer.run(main)

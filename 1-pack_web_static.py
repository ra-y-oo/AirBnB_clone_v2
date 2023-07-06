from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """

    # Create the versions folder if it doesn't exist
    local("mkdir -p versions")

    # Generate the timestamp for the archive name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Define the archive name
    archive_name = "web_static_{}.tgz".format(timestamp)

    # Compress the web_static folder into a .tgz archive
    result = local("tar -cvzf versions/{} web_static".format(archive_name))

    if result.succeeded:
        # Return the path to the generated archive
        return "versions/{}".format(archive_name)
    else:
        return None

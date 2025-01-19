import shutil
import nox


@nox.session
def clean(session):
    """Remove build artifacts and cache."""
    paths = ["build", "dist", "configuration_enforcer.egg-info", "__pycache__"]
    for path in paths:
        shutil.rmtree(path, ignore_errors=True)
    session.log("Cleaned build artifacts!")

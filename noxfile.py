import nox

PYPROJECT = nox.project.load_toml("pyproject.toml")
PYTHON_VERSIONS = nox.project.python_versions(PYPROJECT, max_version="3.13")

nox.options.default_venv_backend = "uv"
nox.options.reuse_venv = "yes"


@nox.session(python=PYTHON_VERSIONS)
def tests(session: nox.Session) -> None:
    session.install(".", "pytest")
    session.run("pytest")

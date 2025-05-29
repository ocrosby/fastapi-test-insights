from invoke.tasks import task
from invoke.context import Context

@task(aliases=["r"])
def run(c: Context) -> None:
    """Run the FastAPI app locally."""
    c.run("uvicorn app.main:app --reload")

@task(aliases=["t"])
def test(c: Context) -> None:
    """Run tests with Allure output."""
    c.run("pytest --alluredir=allure-results")

@task(aliases=["s"])
def serve(c: Context) -> None:
    """Serve the Allure report."""
    c.run("allure serve allure-results")


@task(aliases=["f"])
def format_code(c: Context) -> None:
    """Format code with autoflake, isort, and black."""
    # Remove unused imports and unused variables
    c.run("autoflake --in-place --remove-unused-variables --remove-all-unused-imports --recursive app tests")

    # Sort imports and format code
    c.run("isort app tests")
    c.run("black app tests")

@task(pre=[format_code], aliases=["l"])
def lint(c: Context) -> None:
    """Run static analysis checks."""
    c.run("flake8 app tests")
    c.run("pylint app tests")
    c.run("black --check app tests")
    c.run("isort --check-only app tests")

@task(aliases=["i"])
def install(c: Context) -> None:
    """Install dependencies."""
    c.run("flit install --deps=develop --symlink")

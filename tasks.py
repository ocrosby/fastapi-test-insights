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

@task(aliases=["l"])
def lint(c: Context) -> None:
    """Run flake8 for linting."""
    c.run("flake8 app tests")

@task(aliases=["f"])
def format_code(c: Context) -> None:
    """Format code with black."""
    c.run("black app tests")

@task(aliases=["i"])
def install(c: Context) -> None:
    """Install dependencies."""
    c.run("flit install --deps=develop --symlink")



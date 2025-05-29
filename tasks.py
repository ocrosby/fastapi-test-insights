from invoke import task

@task(aliases=["r"])
def run(c):
    """Run the FastAPI app locally."""
    c.run("uvicorn app.main:app --reload")

@task(aliases=["t"])
def test(c):
    """Run tests with Allure output."""
    c.run("pytest --alluredir=allure-results")

@task(aliases=["s"])
def serve(c):
    """Serve the Allure report."""
    c.run("allure serve allure-results")

@task(aliases=["l"])
def lint(c):
    """Run flake8 for linting."""
    c.run("flake8 app tests")

@task(aliases=["f"])
def format_code(c):
    """Format code with black."""
    c.run("black app tests")

@task(aliases=["i"])
def install(c):
    """Install dependencies."""
    c.run("flit install --deps=develop --symlink")



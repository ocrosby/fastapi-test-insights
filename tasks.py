from invoke import task

@task
def run(c):
    """Run the FastAPI app locally."""
    c.run("uvicorn app.main:app --reload")

@task
def test(c):
    """Run tests with Allure output."""
    c.run("pytest --alluredir=allure-results")

@task
def report(c):
    """Serve the Allure report."""
    c.run("allure serve allure-results")

@task
def lint(c):
    """Run flake8 for linting."""
    c.run("flake8 app tests")

@task
def format(c):
    """Format code with black."""
    c.run("black app tests")

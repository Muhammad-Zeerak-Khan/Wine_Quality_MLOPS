import setuptools

with open("README.md" , "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Wine_Quality_MLOPS"
AUTHOR_NAME = "Muhammad Zeerak Khan"
SRC_REPO = "Wine_Quality_Classification"
AUTHOR_EMAIL = "zeerak1994@outlook.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="An ML Classification Project with MLOPS tools",
    long_description=long_description,
    url = f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls = {"Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues"},
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
    )
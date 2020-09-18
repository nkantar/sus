import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sus",
    version="1.0.0",
    author="Nik Kantar",
    author_email="nik@nkantar.com",
    description="Really simple static website URL shortener",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/nkantar/sus",
    packages=setuptools.find_packages(),
    scripts=["src/sus.py"],
)

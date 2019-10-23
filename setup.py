import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="microblog",
    version="1.0.0",
    url="https://blog.miguelgrinberg.com",
    license="MIT",
    maintainer="Miguel Grinberg",
    maintainer_email="miguel.grinberg@gmail.com",
    description="Flask Mega Tutorial.",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask"],
    extras_require={"test": ["pytest", "coverage"]},
)

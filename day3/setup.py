from setuptools import setup, find_packages
setup(
    name="snapshot",
    packages=find_packages(),
    include_package_data=True,
    scripts=[],
    version="0.1b",
    author="Aliaksandr Dakutovich",
    author_email="Aliaksandr_Dakutovich@epam.com",
    description="some testing app",
    license="MIT",
    install_requires=["psutil"]
)

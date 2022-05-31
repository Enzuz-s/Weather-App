import setuptools

with open("README.MD", "r", encoding="utf-8") as fh:
    long_description = fh.read())

setuptools.setup(
    name="Weather-app-Enzuz-s"
    version="1.0"
    author="Enzuz-s",
    description="A small Weather App",
    url="https://github.com/Enzuz-s/Weather-App",
    project_urls={
        "Bug Tracker": "https://github.com/Enzuz-s/Weather-App/issues",
    },

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">3.10",
)
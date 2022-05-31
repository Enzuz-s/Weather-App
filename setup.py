import setuptools

with open("README.md", "r", encoding="utf-8") as a:
    long_description = a.read()

setuptools.setup(
    name="Weather-app-Enzuz-s",
    version="1.1",
    author="Enzuz-s",
    description="A small Weather App",
    url="https://github.com/Enzuz-s/Weather-App",
    long_description=long_description,
    project_urls={
        "Bug Tracker": "https://github.com/Enzuz-s/Weather-App/issues",
    },

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">3.10",
)

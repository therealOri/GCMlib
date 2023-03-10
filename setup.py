import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GCMlib",
    version="1.0.3",
    author="therealOri",
    license="GPL-3.0",
    install_requires=[
        "alive-progress==2.4.1",
        "pycryptodome==3.17",
        "argon2-cffi==21.3.0"
    ],
    author_email="therealOri@duck.com",
    description="A minimalistic and simple encryption library. For encrypting data using AES GCM mode.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/therealOri/GCMlib",
)

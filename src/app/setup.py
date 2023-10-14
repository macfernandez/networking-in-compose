from setuptools import setup, find_packages


setup(
    name="app",
    version="0.0.1",
    packages=find_packages(),
    description="UTC converter app",
    url="https://github.com/macfernandez/networking-in-compose",
    author="Macarena Fernández Urquiza",
    author_email="m.fernandezurquiza@gmail.com",
    install_requires=[
        "fastapi",
        "uvicorn"
    ],
    extras_require={},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ]
)
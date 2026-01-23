from setuptools import setup, find_packages # pyright: ignore[reportMissingModuleSource]

setup(
    name="desilang",
    version="1.0.2",
    author="Avinash Walton",
    author_email="avinashwalton@gmail.com",  
    description="A Hinglish programming language for Indians 🇮🇳",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/avinashwalton/DesiLang",  
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'desilang=desilang.main:main',  # Ye command line tool banata hai
        ],
    },
)
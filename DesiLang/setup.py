from setuptools import setup, find_packages # pyright: ignore[reportMissingModuleSource]

setup(
    name="desilang",
    version="1.2.0",
    author="Avinash Walton",
    author_email="avinashwalton@gmail.com",
    description="India's first Hinglish programming language for Data Science 🇮🇳",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/avinashwalton/DesiLang",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Interpreters",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Natural Language :: Hindi",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "matplotlib>=3.4.0",
        "scikit-learn>=0.24.0",
    ],
    entry_points={
        'console_scripts': [
            'desilang=desilang.main:main',  # Terminal command: desilang file.desi
        ],
    },
    keywords=[
        "hinglish", "hindi", "programming-language",
        "interpreter", "data-science", "india", "desilang"
    ],
    project_urls={
        "Bug Tracker": "https://github.com/avinashwalton/DesiLang/issues",
        "PlayGround": "https://avinashwalton.github.io/DesiLang",
        "Source Code": "https://github.com/avinashwalton/DesiLang",
    },
)

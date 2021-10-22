from setuptools import setup, find_packages

import air_tracer


setup(
    name="air_tracer",
    packages=find_packages(exclude=["tests"]),
    version=air_tracer.__version__,
    description="Utilities to trace air",
    author="Vlad Prud",
    author_email="vladislav.prud@gmail.com",
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        "anyio==3.3.3",
        "appnope==0.1.2",
        "argcomplete==1.12.3",
        "argon2-cffi==21.1.0",
        "attrs==21.2.0",
        "Babel==2.9.1",
        "backcall==0.2.0",
        "bleach==4.1.0",
        "certifi==2021.10.8",
        "cffi==1.15.0",
        "charset-normalizer==2.0.7",
        "click==8.0.3",
        "click-plugins==1.1.1",
        "cligj==0.7.2",
        "convertdate==2.3.2",
        "cycler==0.10.0",
        "debugpy==1.5.0",
        "decorator==5.1.0",
        "defusedxml==0.7.1",
        "entrypoints==0.3",
        "et-xmlfile==1.1.0",
        "Fiona==1.8.20",
        "geopandas==0.10.1",
        "hijri-converter==2.2.2",
        "holidays==0.11.3.1",
        "idna==3.3",
        "importlib-metadata==4.8.1",
        "ipykernel==6.4.1",
        "ipython==7.28.0",
        "ipython-genutils==0.2.0",
        "jedi==0.18.0",
        "Jinja2==3.0.2",
        "joblib==1.1.0",
        "json5==0.9.6",
        "jsonschema==4.1.0",
        "jupyter-client==7.0.6",
        "jupyter-core==4.8.1",
        "jupyter-server==1.11.1",
        "jupyterlab==3.1.18",
        "jupyterlab-pygments==0.1.2",
        "jupyterlab-server==2.8.2",
        "kiwisolver==1.3.2",
        "korean-lunar-calendar==0.2.1",
        "lightgbm==3.3.0",
        "MarkupSafe==2.0.1",
        "matplotlib==3.4.3",
        "matplotlib-inline==0.1.3",
        "mistune==0.8.4",
        "munch==2.5.0",
        "nbclassic==0.3.2",
        "nbclient==0.5.4",
        "nbconvert==6.2.0",
        "nbformat==5.1.3",
        "nest-asyncio==1.5.1",
        "notebook==6.4.4",
        "numpy==1.21.2",
        "openpyxl==3.0.9",
        "packaging==21.0",
        "pandas==1.3.3",
        "pandocfilters==1.5.0",
        "parso==0.8.2",
        "pexpect==4.8.0",
        "pickleshare==0.7.5",
        "Pillow==8.3.2",
        "plotly==5.3.1",
        "prometheus-client==0.11.0",
        "prompt-toolkit==3.0.20",
        "ptyprocess==0.7.0",
        "pycparser==2.20",
        "Pygments==2.10.0",
        "PyMeeus==0.5.11",
        "pyparsing==2.4.7",
        "pyproj==3.2.1",
        "pyrsistent==0.18.0",
        "python-dateutil==2.8.2",
        "pytz==2021.3",
        "pyzmq==22.3.0",
        "requests==2.26.0",
        "requests-unixsocket==0.2.0",
        "scikit-learn==1.0",
        "scipy==1.7.1",
        "Send2Trash==1.8.0",
        "Shapely==1.7.1",
        "six==1.16.0",
        "sklearn==0.0",
        "sniffio==1.2.0",
        "tenacity==8.0.1",
        "terminado==0.12.1",
        "testpath==0.5.0",
        "threadpoolctl==3.0.0",
        "tornado==6.1",
        "tqdm==4.62.3",
        "traitlets==5.1.0",
        "typing-extensions==3.10.0.2",
        "urllib3==1.26.7",
        "wcwidth==0.2.5",
        "webencodings==0.5.1",
        "websocket-client==1.2.1",
        "zipp==3.6.0"
    ],
    python_requires='>=3.8',
)

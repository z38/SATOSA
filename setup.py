"""
setup.py
"""

from setuptools import setup, find_packages

setup(
    name='SATOSA',
    version='3.1.0',
    description='Protocol proxy (SAML/OIDC).',
    author='DIRG',
    author_email='dirg@its.umu.se',
    license='Apache 2.0',
    url='https://github.com/its-dirg/SATOSA',
    packages=find_packages('src/'),
    package_dir={'': 'src'},
    install_requires=[
        "oic>=0.8.4.0",
        "pyop==1.0.0",
        "pyjwkest==1.1.5",
        "pysaml2==4.0.3",
        "requests",
        "PyYAML",
        "gunicorn",
        "Werkzeug",
        "click"
    ],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.4",
    ],
    entry_points={
        "console_scripts": ["satosa-saml-metadata=satosa.scripts.satosa_saml_metadata:construct_saml_metadata"]
    }
)

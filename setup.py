from setuptools import setup

setup(
    name='tokyo-stock-exchange',
    version='1.0.0',
    description='A Python library for accessing Tokyo Stock Exchange data.',
    author='AKB428',
    author_email='',
    packages=['tokyo_stock_exchange'],
    install_requires=[
        # Add any dependencies your library needs
        "pandas", "os"
    ],
)

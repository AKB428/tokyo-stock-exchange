from setuptools import setup

setup(
    name='tokyo-stock-exchange',
    version='1.0.0',
    description='A Python library for accessing Tokyo Stock Exchange data.',
    author='AKB428',
    author_email='',
    packages=['tokyo_stock_exchange'],
    package_data={'tokyo_stock_exchange': ['tse.csv', 'tse20240229.csv']},
    install_requires=[
        # Add any dependencies your library needs
        "pandas"
    ],
)

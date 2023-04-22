from setuptools import setup

setup(
    name='walletgen',
    version='1.0',
    author='Grantley Cullar',
    description='A library of simple bitcoin wallet generators',
    url='https://github.com/gospacedev/walletgen',
    install_requires=[
        'bitcoin',
        'Mnemonic',
        'bip32utils'
    ],
)

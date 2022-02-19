from distutils.core import setup

VERSION = "0.1.0"

setup(
    name='aiocovidapi',
    packages=['aiocovidapi'],
    version=VERSION,
    description='An asynchronous COVID-19 statistics API wrapper',
    author='Kyuunex',
    author_email='kyuunex@protonmail.ch',
    url='https://github.com/Kyuunex/aiocovidapi',
    download_url=f'https://github.com/Kyuunex/aiocovidapi/tarball/{VERSION}',
    keywords=['covid', 'api'],
    classifiers=[],
    install_requires=['aiohttp'],
)

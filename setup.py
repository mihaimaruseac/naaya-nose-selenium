from setuptools import setup, find_packages

setup(
    name='naaya-nose-selenium',
    version='0.1',
    author='Mihai Maruseac (mihai.maruseac@gmail.com)',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['WebOb', 'nose'],
)


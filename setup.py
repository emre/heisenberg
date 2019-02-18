from setuptools import setup, find_packages

setup(
    name='heisenberg',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/emre/heisenberg',
    license='MIT',
    author='Emre Yilmaz',
    author_email='mail@emreyilmaz.me',
    description='A Python library to interact with the drugwars online game',
    entry_points={
        'console_scripts': [
            'heisenberg = heisenberg.shell:run_shell',
        ],
    },
    install_requires=["steem"],
)

from setuptools import setup

setup(
    name = 'test',
    version = '1.0.0',
    url = 'https://github.com/kniwase/pip_test.git',
    description = 'Test',
    install_requires = ['setuptools', 'numpy'],
    packages = ["Test"],
    entry_points = {
        'console_scripts': [
            'test_print = Test.test:test'
        ]
    }
)
import setuptools

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setuptools.setup(
    name='Python email sender',
    version='1.0',
    author='rylt3x',
    description='Makes able you to send email via python code simply',
    url='https://github.com/rylt3x/email_sender',
    long_description=long_description
)
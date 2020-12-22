import re

from setuptools import find_packages, setup

name = 'classifierpy'
owner = 'rghx'

with open(f'{name}/__init__.py') as f:
    version = re.search(r'([0-9].[0-9].[0-9])', f.read()).group(1)

with open('README.md') as f:
    readme = f.read()

setup(
    name=name,
    version=version,
    license='BSD 3',
    description='classification algorithms',
    long_description=readme,
    long_description_content_type='text/markdown',
    author=owner.capitalize(),
    url=f'https://github.com/{owner}/{name}',
    download_url=f'https://github.com/{owner}/{name}/archive/v{version}.zip',
    project_urls={
        'Code': f'https://github.com/{owner}/{name}',
        'Issue tracker': f'https://github.com/{owner}/{name}/issues',
    },
    packages=find_packages(),
    install_requires=['sklearn', 'numpy'],
    python_requires='>=3.8',
    zip_safe=False,
    classifiers=[
        'Development Status :: Beta',
        'Intended Audience :: Researchers',
        'Topic :: Artificial Intelligence',
        'License :: BSD 3 License',
        'Programming Language :: Python :: 3'
    ],
)

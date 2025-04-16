from setuptools import setup, find_packages

setup(
    name='colablib',
    version='0.1.8',
    packages=find_packages(),
    install_requires=[
        'safetensors',
        'requests',
        'tqdm',
        'PyYAML',
        'gdown',
        'toml',
        'rarfile',
        'xmltodict',
        'py7zr==0.22.0'
    ],
)

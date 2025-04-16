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
        'pillow==11.2.1',
        'pydantic==2.11.3',
        'py7zr==0.22.0'
    ],
)

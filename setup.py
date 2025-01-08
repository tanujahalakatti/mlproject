from setuptools import find_packages, setup
from typing import List, Any

HYPEN_E_DOT: str = '-e .'


def get_requirements(file_path: str) -> List[str]:
    """
    this function will return the list of requirements
    :param file_path:
    :return:
    """
    requirements: list[Any] = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        for req in requirements:
            requirements.append(req.replace("\n", ""))

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='tanujahalakatti',
    packages=find_packages(),
    # install_requires=get_requirements('requirements.txt')
    install_requires=[
        'pandas',
        'numpy',
        'seaborn']
)

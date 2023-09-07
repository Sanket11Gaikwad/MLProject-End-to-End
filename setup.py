from setuptools import find_packages,setup
from typing import List

def get_requirments(file_path:str)->List[str]:
    '''
    this function will return the list of requirment.txt
    '''
    requirements=[]
    
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.replace('\n', " ") for req in requirements]
        
    return requirements

setup(
name= 'MLProject',
version='0.0.1',
author='Sanket',
author_email='gaikwad93sanket@gmail.com',
packages=find_packages(),
install_requires=get_requirments('requirment.txt')
)
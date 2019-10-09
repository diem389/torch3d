import glob
from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension, CUDA_HOME

requirements = [
    'h5py',
    'numpy',
    'torch',
    'torchvision'
]

__version__ = '0.1.0'

ext_modules = []
if CUDA_HOME is not None:
    sources = []
    sources += glob.glob('torch3d/csrc/*.cpp')
    sources += glob.glob('torch3d/csrc/cuda/*.cu')
    ext_modules = [
        CUDAExtension(
            'torch3d._C',
            sources=sources
        )
    ]

setup(
    name='torch3d',
    version=__version__,
    description='Datasets and network architectures for 3D deep learning in PyTorch',
    author='Quang-Hieu Pham',
    author_email='pqhieu1192@gmail.com',
    url='https://github.com/pqhieu/torch3d',
    install_requires=requirements,
    ext_modules=ext_modules,
    cmdclass={'build_ext': BuildExtension},
    packages=find_packages()
)
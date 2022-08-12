from setuptools import find_packages, setup

setup(
    name='zwsp-steg-py',
    version=__import__('zwsp_steg').__version__,
    description='Zero-Width Space Steganography, encodes/decodes hidden messages as non printable/readable characters.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Benjamin Mickler',
    author_email='ben@benmickler.com',
    url='https://github.com/BenjaminMickler/zwsp-steg-py',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
    ],
)

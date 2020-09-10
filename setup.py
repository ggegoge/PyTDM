from setuptools import setup #, find_packages,

with open("README.md", 'r') as f:
	long_description = f.read()
	
setup(
    name='pytdm',
	url='https://github.com/test0wanie/PyTDM',
	version='0.0.4',
    description='Pytońska treść do mowy – Polish text to speech',
	long_description=long_description,
    long_description_content_type="text/markdown",
    author='test0wanie',
	author_email='test0wanie@protonmail.com',
    packages=['pytdm'],
	install_requires=['pyttsx3'],
    license='MIT',
	classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
		"Development Status :: 2 - Pre-Alpha",
    ],
    python_requires='>=3.6',
)

#4th way is wheeel file
#we copied setup readme and searchprogram in release3
#cd release3
#pip install wheel
#python setup.py bdist_wheel
#5th way is window installer
#cd ..
#python setup.py bdist_msi it will create window installer
#after installing go to python38 then open scripts, u will see a file named search program'



import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="search-pkg-sss",  # Replace with your own username
    version="0.0.1",
    author="Shyam",
    scripts=['searchProgram.py'],
    author_email="shyamsaravanan@deloitte.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shyamsaravanan/nexwave",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

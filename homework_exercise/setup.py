import setuptools

setuptools.setup(
    name="homework_exercise",
    version="0.1",

    packages=setuptools.find_packages(
        where='src',
        include=['homework_exercise*','data_file.json'],
    ),
    package_data={"":["data_file.json"]},
    package_dir={"": "src"}
    #py_modules=["pit", "pandas","numpy","statistics"] # use when you would like to include modules to python package
)

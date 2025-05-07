from setuptools import setup, find_packages

setup(
    name="edu_pad",
    version="0.0.1",
    author="Alejandro Cadavid",
    author_email="acu.123@hotmail.com",
    description="tarea analisis de datos # 1",
    py_modules=["actividad_1", "actividad_2"],
    install_requires=[
        "pandas",
        "openpyxl",
        "requests",
        "beautifulsoup4"
    ]
)

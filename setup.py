from setuptools import setup, find_packages

setup(
    name='lexi_game_engine',            # Nazwa Twojego modułu
    version='0.1.0',                   # Wersja modułu
    description='A simple 3D game engine in Python',
    long_description=open('README.md').read(),  # Opis (długi) z pliku README
    long_description_content_type='text/markdown',
    author='Alluringlambpl',
    author_email='fboost247@gmail.com',
    url='notyet',  # Link do repozytorium (np. GitHub)
    packages=find_packages(),         # Automatycznie znajdź wszystkie pakiety
    install_requires=[                # Zależności, jeśli są
        'keyboard',                    # Jeśli używasz `keyboard`, dodaj tutaj
    ],
    classifiers=[                     # Klasyfikatory dla PyPI
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',           # Wersja Pythona
)

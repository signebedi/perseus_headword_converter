from setuptools import setup, find_packages

setup(
    name='beta_conv',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',  # Make sure to include any other dependencies your project might have
    ],
    entry_points='''
        [console_scripts]
        beta_conv=beta_conv.__main__:greek_to_beta_code
    ''',
    author='Sig Janoska-Bedi',
    author_email='signe@atreeus.com',
    description='A simple CLI tool to convert Greek words to Beta Code.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/signebedi/perseus_headword_converter',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='cli greek beta_code converter',
    python_requires='>=3.10',
)

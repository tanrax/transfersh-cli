from setuptools import setup
setup(
  name = 'transfersh-cli',
  py_modules=['transfersh'],
  version = '1.1.0',
  python_requires='>3.6',
  description = 'Client to upload files to the transfer.sh service',
  author = 'Andros Fenollosa',
  author_email = 'andros@fenollosa.email',
  url = 'https://github.com/tanrax/transfersh-cli',
  keywords = ['transfer', 'upload', 'client'],
  classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
  ),
  install_requires=[
        'Click>=6.7',
        'pyperclip>=1.6.4',
        'requests>=2.19.1'
  ],
  entry_points='''
      [console_scripts]
      transfersh=transfersh:transfersh_cli
  '''
)

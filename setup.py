from setuptools import setup

setup(
    name="transfersh-cli",
    py_modules=["transfersh"],
    version="1.2.0",
    python_requires=">3.6",
    description="Client to upload files to the transfer.sh service",
    author="Andros Fenollosa",
    author_email="andros@fenollosa.email",
    url="https://github.com/tanrax/transfersh-cli",
    keywords=["transfer", "upload", "client"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "click==8.1.7",
        "progressbar2==4.2.0",
        "pyperclip==1.0.0",
        "requests==2.31.0",
        "requests-toolbelt==",
        "tqdm==4.66.1",
    ],
    entry_points="""
      [console_scripts]
      transfersh=transfersh:transfersh_cli
  """,
)

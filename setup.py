import setuptools

setuptools.setup(
    name="swc-registry",
    version="0.0.2",
    url="https://github.com/SmartContractSecurity/SWC-registry-python",
    author="SmartContractSecurity",
    author_email="ersul4ik@gmail.com",
    description="Python library for accessing SWC-registry content.",
    long_description=open("README.rst").read(),
    packages=["swc_registry"],
    include_package_data=True,
    install_requires=["requests==2.20.1"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)

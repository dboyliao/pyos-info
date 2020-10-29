from setuptools import find_packages, setup

setup(
    name="os-info",
    packages=find_packages(),
    author="dboyliao",
    author_email="qmalliao@gmail.com",
    entry_points={
        "console_scripts": ["os-info=os_info.__main__:show_info"],
    },
    install_requires=["click"],
    extras_require={"dev": ["black", "isort", "flake8"]},
)
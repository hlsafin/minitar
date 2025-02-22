from setuptools import setup

packages = ['minatar', 'minatar.environments']

entry_points = {
    'gym.envs': ['MinAtar=minatar.gym:register_envs']
}

setup(
    name='MinAtar',
    version='1.0.15',
    description='A miniaturized version of the Arcade Learning Environment.',
    url='https://github.com/kenjyoung/MinAtar',
    author='Kenny Young',
    author_email='kjyoung@ualberta.ca',
    license='GPL',
    packages=packages,
    entry_points=entry_points,
    python_requires=">=3.7"  # This line allows installation on Python 3.7 and above.
)

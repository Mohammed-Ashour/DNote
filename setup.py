from setuptools import setup

setup(name='notes',
      version='0.1',
      description='A program used to manage your notes and organize them across your machine.',
      url='',
      author='Mohammed Ashour',
      author_email='m.aly.ashour@gmail.com',
      license='MIT',
      install_requires=[
          'tabulate',
          'argparse',
      ],
      packages=['.'],
      scripts=['notes.py','config.json'],
      include_package_data=True,
      zip_safe=False,
      entry_points={
    'console_scripts': [ 
        'notes = notes:main' 
    ] 
})





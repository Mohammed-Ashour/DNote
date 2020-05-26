from setuptools import setup

setup(name='notes',
      version='0.1',
      description='A program used to manage your notes and organize them across your machine.',
      url='https://github.com/Mohammed-Ashour/Notes_Management_System',
      author='Mohammed Ashour',
      author_email='m.aly.ashour@gmail.com',
      license='MIT',
      install_requires=[
          'tabulate',
          'argparse',
      ],
      packages=['.'],
      data_files=["config.json"],
      scripts=[],
      include_package_data=True,
      zip_safe=False,
      entry_points={
    'console_scripts': [ 
        'notes = notes:main' 
    ] 
}
)





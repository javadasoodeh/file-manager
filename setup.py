from setuptools import setup

requires = [
    'pyramid', 'pyramid_storage', 'pillow', 'peewee', 'configparser'
]

setup(name='FileManager',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = FileManager:main
      """,
      author_email='javadasoodeh73@gmail.com',
      author='Javad Asoodeh',
      description="This service is uploading",
      version="0.1.0"
      )

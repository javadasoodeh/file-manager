from setuptools import setup

requires = [
    'pyramid', 'pyramid_storage', 'pillow', 'peewee', 'configparser',
      'pyMySQL', 'mysql-connector-python', 'pdfkit', 'weasyprint', 'tornado'
]

setup(name='FileManager',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = FileManager:main
      """,
      author_email='javadasoodeh73@gmail.com',
      author='Javad Asoodeh',
      description="File Manager Service",
      version="1.0.0"
      )

from setuptools import setup, find_packages

version = '1.3.3.dev0'

setup(name='plone.app.ldap',
      version=version,
      description="LDAP control panel for Plone 4.1 and higher",
      long_description=(open("README.rst").read() + "\n" +
                        open("CHANGES.rst").read()),
      classifiers=[
          "Framework :: Plone",
          "Framework :: Plone :: 4.1",
          "Framework :: Plone :: 4.2",
          "Framework :: Plone :: 4.3",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: System :: Systems Administration :: Authentication/Directory :: LDAP",
          ],
      keywords='plone ldap',
      author='Wichert Akkerman - Simplon',
      author_email='wichert@simplon.biz',
      maintainer='Kevin Teague',
      maintainer_email='kevin@bud.ca',
      url='http://pypi.python.org/pypi/plone.app.ldap',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone', 'plone.app'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'plone.memoize',
          'Products.CMFCore',
          'Products.GenericSetup',
          'Products.PloneLDAP',
          'python-ldap',
          'setuptools',
          'zope.component',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.lifecycleevent',
          'zope.schema',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

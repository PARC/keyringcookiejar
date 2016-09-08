from setuptools import setup
setup(
  name = 'keyringcookiejar',
  packages = ['keyringcookiejar'], # this must be the same as the name above
  version = '0.1',
  description = 'Store cookies using the keyring package',
  author = 'Tom Maher',
  author_email = 'tmaher@pw0n.me',
  url = 'https://github.com/PARC/keyringcookiejar',
  install_requires =['keyring']
)

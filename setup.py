from setuptools import setup, find_packages
from chatovod import VERSION


setup(
    name='django-chatovod',
    version=".".join(map(str, VERSION)),
    description='Chatovod  - chat widget for Django.',
    keywords="django chat chatovod",
    long_description=open('README.rst').read(),
    author="GoTLiuM InSPiRiT",
    author_email='gotlium@gmail.com',
    url='http://github.com/gotlium/django-chatovod',
    packages=find_packages(exclude=['demo']),
    include_package_data=True,
    package_data={
        'chatovod': [
            'templates/chatovod/*.html',
        ],
    },
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)

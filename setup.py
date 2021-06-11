from setuptools import setup, Extension, find_packages

requirements_noversion = [
'nltk',
'numpy',
'openpyxl',
'pandas',
'parsedatetime',
'parsel',
'passlib',
'Pillow',
'plotly',
'pymongo',
'pyperclip',
'psycopg2-binary',
'requests',
'SQLAlchemy',
'urllib3',
'seaborn',
]
setup(
	# Meta information
	name				= 'news_raker',
	version				= '0.0.1',
	author				= 'Supratik Chatterjee',
	author_email		= 'chatterjee.supratik@tcs.com',
	# license			= '2-clause BSD',
	url					= 'https://github.com/supratikchatterjee16/workbench',
	description			= 'I rake your news',
	keywords			= ['python news scraping web rake raker'],
	install_requires	= requirements_noversion,
	# build information
	py_modules			= ['news_raker'],
	packages			= find_packages(),
	package_dir			= {'news_raker' : './news_raker'},
	include_package_data= True,
	package_data		= {'news_raker' : [
								'data/*',
								'data/*/*',
								'data/*/*/*',
								'data/*/*/*/*',
								'data/*/*/*/*/*',
								'data/*/*/*/*/*/*',
								]},

	zip_safe			= True,
	# https://stackoverflow.com/questions/14399534/reference-requirements-txt-for-the-install-requires-kwarg-in-setuptools-setup-py
	entry_points		= {'console_scripts' : ['news_raker = news_raker:run'],},
	# ext_modules			= [bjoern_extension],
	classifiers			= [
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
	],
)

#!/usr/bin/python3
from distutils.core import setup

setup(
	name='update_tool_python',
	version='1.0',
	description='A tool to assist with APT updates',
	author='Shane Ozouf',
	packages=['update_tool_python', 'update_tool_python/common',
			'update_tool_python/check_for_updates', 'update_tool_python/updater'],
	data_files=[('/usr/local/share/update_tool_python/data',
			['update_tool_python/common/data/updates.txt',
				'update_tool_python/common/data/zeroUpdates.txt'])],
	scripts=['check-for-updates', 'updater']
)

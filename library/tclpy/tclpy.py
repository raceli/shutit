"""ShutIt module. See http://shutit.tk
"""
#Copyright (C) 2014 OpenBet Limited
#
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is furnished
#to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
#FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
#COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
#IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
#CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from shutit_module import ShutItModule

class tclpy(ShutItModule):

	def is_installed(self,shutit):
		return False

	def build(self,shutit):
		shutit.install('tcl-dev')
		shutit.install('python-dev')
		shutit.install('git')
		shutit.install('make')
		shutit.install('gcc')
		shutit.send('pushd /opt')
		shutit.send('git clone https://github.com/aidanhs/libtclpy.git')
		shutit.send('pushd libtclpy')
		shutit.send('make')
		# TODO: make install?
		shutit.send('cp libtclpy* /lib')
		shutit.send('popd')
		shutit.send('popd')
		return True

	#def get_config(self,shutit):
	#    return True

	#def check_ready(self,shutit):
	#    return True
	
	#def start(self,shutit):
	#    return True

	#def stop(self,shutit):
	#    return True

	#def finalize(self,shutit):
	#    return True

	#def remove(self,shutit):
	#    return True

	#def test(self,shutit):
	#    return True

def module():
	return tclpy(
		'shutit.tk.tclpy.tclpy', 782914092.0125235135315,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


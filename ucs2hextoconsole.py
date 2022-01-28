#!/usr/bin/env python3
#
# Usage :
#
# $ python3 ./ucs2hextoconsole.py "062706440633064406270645002006390644064a06430645"
# السلام عليكم
# $
#
# May peace be upon you | As-salamu Alaikum | السلام عليكم
#

import binascii, sys
import pdb

if len( sys.argv ) != 2:
	print( "Missing parameter. Please supply the hex string as a parameter" )
	sys.exit( 1 )
 
text=sys.argv[ 1 ]

try:
	print( binascii.unhexlify( text ).decode( 'utf-16-be' ) )
except:
	print( "Some problem parsing hex string. Try again and make sure you don't have any missing character" )

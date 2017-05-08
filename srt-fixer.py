
import sys
import re
import argparse


parser = argparse.ArgumentParser( description = 'Offset srt subtitles.')
# add mandatory (positional) arguments
parser.add_argument("fname",help="input srt file name")
parser.add_argument("offset",type=float,help="subtitle offset in seconds to apply (can be fractional)")

# parse arguments
args = parser.parse_args()

with open(args.fname,newline='') as ifp:	
	for line in ifp:
		match = re.search(r'^(\d+:\d+:\d+,\d+)\s+--\>\s+(\d+:\d+:\d+,\d+)', line)
                if match:
                    sys.write("%s --> %s\n" % (
                        offset_time(options.offset, match.group(1)),
                        offset_time(options.offset, match.group(2))
		    )
else:
		
	       	sys.stdout.write(line)

		//`if options.overwrite:
		shutil.move(out_filename, options.srt_file.name)


#βιβλιοθήκες
import sys
import re
import argparse


parser = argparse.ArgumentParser( description = 'Offset srt subtitles.')
# add mandatory (positional) arguments
parser.add_argument("fname",help="input srt file name")
parser.add_argument("offset",type=float,help="subtitle offset in seconds to apply (can be fractional)")

# parse arguments
args = parser.parse_args()

with open(args.fname,newline='') as ifp: #άνοιγμα του αρχείου srt	
	for line in ifp:
		line = line.strip()	
		match = re.search(r'^(\d+:\d+:\d+,\d+)\s+--\>\s+(\d+:\d+:\d+,\d+)', line)
                if match:
                    sys.write("%s --> %s\n" % (
                        offset_time(options.offset, match.group(1)),
                        offset_time(options.offset, match.group(2))
		    )


def parse_time(time): #αναγνωρίζουμε τον χρόνο σε ώρες,λεπτά,δευτερόλεπτα,κλάσματα δευτερολέπτου
 hour, minute, second = time.split(':') #ώρες : λεπτά : δευτερόλεπτα
 hour, minute = int(hour), int(minute)	#οι ώρες και τα λεπτά
 second_parts = second.split(',')# λεπτά,δευτερόλεπτα
 second = int(second_parts[0])	#τα δευτερόλεπτα αποθηκεύονται σε έναν μονοδιάστατο πίνακα
 milisecond = int(second_parts[1] # τα κλάσματα των δευτερολέπτων σε άλλο
 return [hour, minute, second, milisecond] #λίστα επιστροφής
		  
#χρόνος με τα offset
def offset(time):
 time[1] += (time[2] + offset) / 60 #αρχικός χρόνος 
 time[2] = (time[2] + offset) % 60 #ο χρόνος που προστείθεται σε seconds
 return time #επιστροφή του χρόνου.	
 
sys.stdout.write(newline , out) #μπορεί να γίνει και με shutil αν μπορούσαμε να χρησιμοποιήσουμε αυτήν την βιβλιοθήκη
		  

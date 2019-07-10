#!/usr/bin/env bash

RCFILE=$HOME/.bashrc

function compatDelete {
	echo "You have an older version of SUDO present. Please remove it from $RCFILE to be able to update to the new version."
	exit 0
}

function deleteOld {
	if [ $( grep "SUDO - shout at bash" "$RCFILE" | wc -l ) -eq 0 ]; then
	       	echo "No current installation found"
		return
        fi

	cp "$RCFILE" "$RCFILE.old"

	# Check for old versions
	if [ $( grep "end SUDO" "$RCFILE" | wc -l ) -eq 0 ]; then
		compatDelete
		exit 0
	fi

	echo "Searching for recent installation..."

	awk -v rcfile="$RCFILE" 'BEGIN{f=0}
	{
	    match($0,"# SUDO - shout at bash")
	    if(RSTART){
		print substr($0,1,RSTART-1)
		f=1
		next
	    }
	    match($0,"# end SUDO")
	    if(RSTART){
		$0=substr($0,RSTART+10)
		f=0
	    }
	}
	f==0{print > rcfile}
	' "$RCFILE"
}

deleteOld

echo "Installing..."

cat ./SUDO >> "$RCFILE"
echo '
Now run:      source ' $RCFILE '
'

exit 0


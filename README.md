# SUDO
Order bash to do things by shouting.

## How-to

Typing `sudo chmod +x foo.sh` is so boring, isn't it? You really want to `chmod` that file, so let bash know about it. Be assertive:

	CHMOD +x foo.sh

That way, bash knows you mean business. Plus, you save yourself three keypresses if you use caps lock, or four(!) if you use shift.

### Other features

You can ~yell~ type `SUDO` to get bash to run the last command you wrote with sudo prefixed. After all, forgetting sudo can be very frustrating;
you need to let your anger out somehow. A typical usage looks like this:

	$ mkdir /bar
	mkdir: cannot create directory ‘/bar’: Permission denied
	$ SUDO
	[sudo] password for user: 
	$ /bar
	bash: /bar: Is a directory
	$ :)

## Installation

Run `install.py`, follow instructions (requires Python 3). Running this script will also allow you to update to new versions.

Note: this will append to your `~/.bashrc`. A backup of your `~/.bashrc` is kept at `~/.bashrc.old` if anything goes catastrophically wrong.

Warning: never run scripts without checking them and being certain that they are not malicious.

## Acknowledgements

Thanks to [@rpprroger](https://github.com/rpprroger) for the idea. I just implemented the idea, badly.

  

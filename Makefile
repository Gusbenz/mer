.PHONY: install clean

cwd = $(shell pwd)
install_path = /usr/local/bin/mer

install:
	ln -s $(cwd)/mer.py $(install_path)

clean:
	rm $(install_path)

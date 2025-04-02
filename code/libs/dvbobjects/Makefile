all:
	echo "Bulding python package with setuptools module"
	python3 setup.py build

install:
	sudo python3 setup.py install

clean:
	python3 setup.py clean
	rm -rf build/*

-include $(wildcard *.d) dummy
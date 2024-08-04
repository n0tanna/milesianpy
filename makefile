.PHONY: build

all: clean build push clean

setup:
	pip install wheel twine

clean:
	rm -rf build dist milesianpy.egg-info

build:
	python -m build

push:
	@twine upload --verbose  --skip-existing dist/*

commit:
	git commit -am "$(MESSAGE)"

patch:
	$(MAKE) commit
	git tag -a $(shell semver bump patch $(shell git describe)) -m "$(MESSAGE)"
	$(MAKE) all
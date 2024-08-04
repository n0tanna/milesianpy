.PHONY: build

all: build publish clean

setup:
	pip install -U pip build twine

clean:
	rm -rf build dist milesianpy.egg-info

build:
	python -m build

publish:
	@twine upload --verbose  --skip-existing dist/*

commit:
	git commit -am "$(MESSAGE)"

patch:
	$(MAKE) commit
	git tag -a $(shell semver bump patch $(shell git describe)) -m "$(MESSAGE)"
	$(MAKE) all
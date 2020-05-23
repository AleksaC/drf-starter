# drf-starter

[![license](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/AleksaC/drf-starter/blob/master/LICENSE)
[![drf-starter](https://circleci.com/gh/AleksaC/drf-starter.svg?style=svg)](https://circleci.com/gh/AleksaC/drf-starter)
[![Coverage Status](https://coveralls.io/repos/github/AleksaC/drf-starter/badge.svg?branch=master&t=sEMXG5)](https://coveralls.io/github/AleksaC/drf-starter?branch=master)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/AleksaC/drf-starter/blob/master/.pre-commit-config.yaml)

## About 📖

This repository contains [Django Rest Framework](https://github.com/encode/django-rest-framework/tree/master)
boilerplate I use as a starting point for building most of my REST APIs.

### Architecture 📏
While I'm vaguely familiar with many design patterns and approaches to building
software I do not strictly adhere to any of them. I follow best practices for
obvious stuff and do what makes sense to me for the less obvious stuff.

### Code style 💅
I'm mostly sticking to PEP8 guidelines and Django style guide. The tools I use
for maintaining the style are black, flake8 and isort. I've set up pre-commit
hooks that make sure all the rules are followed on each commit. This is also a
part of the CI pipeline.

### Dependencies
I like keeping the number of dependencies in my project as low as possible.
However django has rich ecosystem of high-quality, well-maintained third party
apps with few dependencies themselves which makes them pretty safe to use.
[Dependabot](https://dependabot.com/) is in charge of keeping all the
dependencies up to date.

### Testing 👩‍🔬
I prefer using `pytest` on my other projects, but I haven't found enough
compelling reasons to use it over django's built-in testing system. Since from
my experience a project that doesn't start out with a decent test coverage
rarely ever reaches it I tried to provide test for everything that I thought
should be tested. Tests are included in CI. To run them locally use:
```shell script
./runtests.sh
```

## Future improvements

I'm currently building a templating engine for Python projects and I'll use it
for this project (I could've used cookiecutter but there are several problems
with it which my engine will solve). I'm testing out azure pipelines and may use
them in future instead of CircleCI. I'm also working on a few drf projects so
all relevant improvements in those projects will also be integrated here.

## Say hi 🙋‍♂️
- [Personal website](https://aleksac.me)
- <a target="_blank" href="http://twitter.com/aleksa_c_"><img alt='Twitter followers' src="https://img.shields.io/twitter/follow/aleksa_c_.svg?style=social"></a>
- aleksacukovic1@gmail.com

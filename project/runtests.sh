#!/usr/bin/env bash
set -eou pipefail

coverage run manage.py test --settings=server.settings.test --keepdb

if [[ -v COVERALLS_REPO_TOKEN ]]; then
    coveralls
fi

coverage report

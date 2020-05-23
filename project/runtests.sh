#!/usr/bin/env bash
set -eou pipefail

coverage run manage.py test --settings=server.settings.test --keepdb && coverage report

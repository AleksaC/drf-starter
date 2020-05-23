This directory will be populated by translations (`.po` files) after running
```
python manage.py makessages
```

To compile `.po` files into `.mo` files, optimized for use by `gettext` run
```
python manage.py compilemessages
```

`.mo` files should be excluded from version control.

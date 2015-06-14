# IROLiNK

[![Build Status](https://travis-ci.org/irolink/irolink-app.svg?branch=master)](https://travis-ci.org/irolink/irolink-app)
[![Coverage Status](https://coveralls.io/repos/irolink/irolink-app/badge.svg?branch=master)](https://coveralls.io/r/irolink/irolink-app?branch=master)


## Contribution

### Translations

    $ mkdir -p src/translations/
    $ pybabel extract -F babel.cfg -o messages.pot src
    $ pybabel init -i messages.pot -d src/translations -l ja
    $ pybabel compile -d src/translations
    $ pybabel update -i messages.pot -d src/translations



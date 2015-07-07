# IROLiNK

[![Build Status](https://travis-ci.org/irolink/irolink-app.svg?branch=master)](https://travis-ci.org/irolink/irolink-app)
[![Coverage Status](https://coveralls.io/repos/irolink/irolink-app/badge.svg?branch=master)](https://coveralls.io/r/irolink/irolink-app?branch=master)

Linking the various colors. IROLiNK is IRO + LiNK (IRO is the "color" in Japanese). - http://iro.link


## Translations

    $ mkdir -p src/translations/
    $ pybabel extract -F babel.cfg -o messages.pot src
    $ pybabel init -i messages.pot -d src/translations -l ja
    $ pybabel compile -d src/translations
    $ pybabel update -i messages.pot -d src/translations


## Contribution

1. Fork it ( http://github.com/irolink/irolink-app/fork )
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request

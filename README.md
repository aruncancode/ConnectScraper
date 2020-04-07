# Connect Scraper

Made by @urwrstkn8mare and @aruncancode.

## Use pipenv

1. [Install pipenv package](https://pipenv.pypa.io/en/latest/install/#installing-pipenv)
2. `cd` into the repository. (eg. `cd connect-api`)
3. run `pipenv install --dev`.

## Instructions

1. Follow the instructions to use pipenv.
2. Create a copy of the [sensitiveInfoTemplate.json](sensitiveInfoTemplate.json) file in the [tests](tests/) folder.
3. Rename the copy to [sensitveInfo.json](tests/sensitiveInfo.json)
4. Replace the `username` and `password` values with your username and password.
5. Run the [test.py](tests/test.py) with `pipenv run test`

_NOTE: You can run python files with `pipenv run python <python file>`!_

## Todo

- [x] Login to connect.
- [x] Get the html of a page.
- [x] Get the javascript in the page to run. @urwrstkn8mare and @aruncancode are working on this
- [x] Parse it. @aruncancode is working on this
- [x] Create SQL database to store userdata @aruncancode is working on this
- [ ] Perodic GET requests to connect and update dateabse @aruncancode is working on this
- [ ] Discord integration @both are workong on this

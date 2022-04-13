# search-trafficfine-chromedriver
This project is a selenium instance for search traffic fine from webpage. The app execute from heroku infrastructure with buildpacks chromedriver and chrome app.

## Install in Heroku:
1. Get a Heroku account
2. Create a new application
2. Set the enviroment variables in Heroku app:  (Heroku Dashboard > Settings > Config Vars > Reveal Config Vars)  
    - Not change values:
        - GOOGLE_CHROME_PATH = /app/.apt/usr/bin/google-chrome
        - CHROMEDRIVER_PATH = /app/.chromedriver/bin/chromedriver

    - Your define the values: 
        - CARPLATE_EXAMPLE = 033FKP
        - SEARCH_HOUR = 00
        - SEARCH_MINUTES = 00
        - TZ = America/Guatemala 
        (search the own Time Zone in https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)  

3. Install a builpacks: (Heroku Dashboard > Settings > Buildpacks > Add builpack)
    - python environment: 
        select heroku/python in the buildpack panel (it's include a pip and set enviroment defined in runtime.txt).
    - Chromedriver for selenium  
    https://github.com/heroku/heroku-buildpack-chromedriver.git  
    - Executable Chrome app  
    https://github.com/heroku/heroku-buildpack-google-chrome.git  

4. Install Heroku cli (https://devcenter.heroku.com/articles/heroku-cli) and login.
```bash
heroku login
```

5. Enable Free Dynos (Not require paid, 500 hours free and sleep each 30 minutos without use). In this case is 'clock', but there are more options (web, worker and clock)
```bash
heroku ps:scale clock=1 --app search-trafficfine-chromedriver
```

4. Deploy App (Heroku Dashboard > Deploy)


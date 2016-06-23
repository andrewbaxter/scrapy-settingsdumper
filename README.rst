Logs effective settings at both the crawler and spider level.  Make sure LOG_LEVEL is set to DEBUG.

Installation
############

Run::

   pip install git+https://github.com/andrewbaxter/scrapy-settingsdumper

Add this line to ``settings.py``::

   EXTENSIONS = {
       'settingsdumper.SettingsLogging': 100
   }


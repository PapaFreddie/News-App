
# News-App
## By Fred Papa

## Description
News-App is a web application that displays a list of various news sources. On choosing a news source, it will preview the top news articles of the day. Clicking a news article therefore, will redirect the user to read it fully from the news source. This is achieved by using the News API.

## User Stories
The user would like to: 
* To see various news sources and select the ones I prefer
* To see all the news articles from that news source
* To see the image, description and time the news article was created.
* To click on an article and read it fully from the news source.


## Installation / Setup instruction

#### The application requires the following installations to operate 
* python3.10.2
* pip

#### Cloning

* Open Terminal {Ctrl+Alt+T}

* git clone ```https://github.com/PapaFreddie/News-App.git```

* cd News-App

* $ python -m venv virtual (install virtual environment)
* $ source virtual/bin/activate
* $ python -m pip install -r requirements.txt (install all dependencies)
* Inside the manage.py module change the config_name parameter from 'production' to 'development' ie 
  app = create_app('production') should be app = create_app('development')
* $ ./start.sh


## Technologies Used

* python3.10.2
* Flask framework

## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

Email: fredpapah20@gmail.com
Tel: +254111728374

### License
**(MIT License)**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Copyright (c) 2022 **Fred Papa**
  
# tunescraper
List new music releases scraped from websites

## Installation
### Linux installation
python3 -m venv venv
source venv/bin/activate
sudo pip install -r requirements.txt

install chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb

## Setup
.env file must be present in root folder with the following variable. 
Check committed .env_example for the variables.
Spotify app credentials can be obtained from [Spotify developer's site](https://developer.spotify.com/documentation/web-api/concepts/apps)

## Usage example
python tunescraper.py


## Project milestones
* 1.0 : get a list of released albums from last week release page of [albumoftheyear.org](https://www.albumoftheyear.org/releases/this-week/)
  * List album title and author
  * From the release of same date or first date before 
* 2.0 : for each album of the release and for each artist provide a link to spotify page 
* 3.0 : use data from spotify to implement filter based on album's genre
* 4.0 : implement GUI (tbd local app o website)





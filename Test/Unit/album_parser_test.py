import unittest

from bs4 import BeautifulSoup

from App.locators.page_locators import PageLocators
from App.parsers.album_parser import AlbumParser


class AlbumParserTest(unittest.TestCase):
    def test_album(self):

        expected_album = {'author': 'Jamie xx', 'title': 'In Waves', 'type': 'album'}

        album_section = '''<div id="centerContent">
<div class="flexContainer">
    <div class="wideLeft">
    <div class="albumBlock five small" data-type>
<div class="image mustHear"><a href="/album/976637-jamie-xx-in-waves.php">
        <div class="mustHear"><i class="fas fa-star"></i></div>
        <img class="lazyload" src="https://cdn.albumoftheyear.org/images/clear.gif" data-src="https://cdn2.albumoftheyear.org/200x/album/976637-in-waves_195712.jpg" alt="Jamie xx - In Waves" data-srcset="https://cdn2.albumoftheyear.org/400x/album/976637-in-waves_195712.jpg 2x" /></a>
</div><a href="/artist/1813-jamie-xx/">
    <div class="artistTitle">Jamie xx</div>
</a><a href="/album/976637-jamie-xx-in-waves.php">
    <div class="albumTitle">In Waves</div>
</a>
<div class="ratingRowContainer">
</div></div></div></div></div>'''

        soup = BeautifulSoup(album_section, 'html.parser')
        album_section = soup.select_one(PageLocators.ALBUMS)

        album_parser = AlbumParser()
        album_parser.set_album_section(album_section)

        self.assertEqual(expected_album, album_parser.album)

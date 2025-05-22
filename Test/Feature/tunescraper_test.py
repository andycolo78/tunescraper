import os
import unittest
import subprocess

from unittest.mock import MagicMock
from unittest.mock import patch
import sys
from io import StringIO

import pytest
from dotenv import load_dotenv

from Test.Lib.mock_metadata_client import MockMetadataClient
from Test.Lib.mock_requests_client import MockRequestsClient

from dependency_injector import providers

from alembic.config import Config
from alembic import command






def mock_request_client_response() -> dict:
    url = 'https://www.albumoftheyear.org/releases/this-week/'
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Dataset",
                             "test_get_releases_from_single_page.html")
    with open(file_path, 'r') as file:
        page = file.read()

    return {url: page}


def mock_albums_metadata() -> list:
    return [
        {'album_type': 'album', 'total_tracks': 12,
         'available_markets': ['AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK',
                               'DO', 'DE', 'EC', 'EE', 'SV', 'FI', 'FR', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'IE',
                               'IT', 'LV', 'LT', 'LU', 'MY', 'MT', 'MX', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE',
                               'PH', 'PL', 'PT', 'SG', 'SK', 'ES', 'SE', 'CH', 'TW', 'TR', 'UY', 'US', 'GB', 'AD',
                               'LI', 'MC', 'ID', 'JP', 'TH', 'VN', 'RO', 'IL', 'ZA', 'SA', 'AE', 'BH', 'QA', 'OM',
                               'KW', 'EG', 'MA', 'DZ', 'TN', 'LB', 'JO', 'PS', 'IN', 'BY', 'KZ', 'MD', 'UA', 'AL',
                               'BA', 'HR', 'ME', 'MK', 'RS', 'SI', 'KR', 'BD', 'PK', 'LK', 'GH', 'KE', 'NG', 'TZ',
                               'UG', 'AG', 'AM', 'BS', 'BB', 'BZ', 'BT', 'BW', 'BF', 'CV', 'CW', 'DM', 'FJ', 'GM',
                               'GE', 'GD', 'GW', 'GY', 'HT', 'JM', 'KI', 'LS', 'LR', 'MW', 'MV', 'ML', 'MH', 'FM',
                               'NA', 'NR', 'NE', 'PW', 'PG', 'PR', 'WS', 'SM', 'ST', 'SN', 'SC', 'SL', 'SB', 'KN',
                               'LC', 'VC', 'SR', 'TL', 'TO', 'TT', 'TV', 'VU', 'AZ', 'BN', 'BI', 'KH', 'CM', 'TD',
                               'KM', 'GQ', 'SZ', 'GA', 'GN', 'KG', 'LA', 'MO', 'MR', 'MN', 'NP', 'RW', 'TG', 'UZ',
                               'ZW', 'BJ', 'MG', 'MU', 'MZ', 'AO', 'CI', 'DJ', 'ZM', 'CD', 'CG', 'IQ', 'LY', 'TJ',
                               'VE', 'ET', 'XK'],
         'external_urls': {'spotify': 'https://open.spotify.com/album/57MSBg5pBQZH5bfLVDmeuP'},
         'href': 'https://api.spotify.com/v1/albums/57MSBg5pBQZH5bfLVDmeuP', 'id': '57MSBg5pBQZH5bfLVDmeuP',
         'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b2733126a95bb7ed4146a80c7fc6',
                     'width': 640},
                    {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e023126a95bb7ed4146a80c7fc6',
                     'width': 300},
                    {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d000048513126a95bb7ed4146a80c7fc6',
                     'width': 64}], 'name': 'In Waves', 'release_date': '2024-09-20',
         'release_date_precision': 'day', 'type': 'album', 'uri': 'spotify:album:57MSBg5pBQZH5bfLVDmeuP',
         'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/7A0awCXkE1FtSU8B0qwOJQ'},
                      'href': 'https://api.spotify.com/v1/artists/7A0awCXkE1FtSU8B0qwOJQ',
                      'id': '7A0awCXkE1FtSU8B0qwOJQ', 'name': 'Jamie xx', 'type': 'artist',
                      'uri': 'spotify:artist:7A0awCXkE1FtSU8B0qwOJQ'}]},
        {'album_type': 'album', 'total_tracks': 15,
         'available_markets': ['AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK',
                               'DO', 'DE', 'EC', 'EE', 'SV', 'FI', 'FR', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'IE',
                               'IT', 'LV', 'LT', 'LU', 'MY', 'MT', 'MX', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE',
                               'PH', 'PL', 'PT', 'SG', 'SK', 'ES', 'SE', 'CH', 'TW', 'TR', 'UY', 'US', 'GB', 'AD',
                               'LI', 'MC', 'ID', 'JP', 'TH', 'VN', 'RO', 'IL', 'ZA', 'SA', 'AE', 'BH', 'QA', 'OM',
                               'KW', 'EG', 'MA', 'DZ', 'TN', 'LB', 'JO', 'PS', 'IN', 'KZ', 'MD', 'UA', 'AL', 'BA',
                               'HR', 'ME', 'MK', 'RS', 'SI', 'KR', 'BD', 'PK', 'LK', 'GH', 'KE', 'NG', 'TZ', 'UG',
                               'AG', 'AM', 'BS', 'BB', 'BZ', 'BT', 'BW', 'BF', 'CV', 'CW', 'DM', 'FJ', 'GM', 'GE',
                               'GD', 'GW', 'GY', 'HT', 'JM', 'KI', 'LS', 'LR', 'MW', 'MV', 'ML', 'MH', 'FM', 'NA',
                               'NR', 'NE', 'PW', 'PG', 'WS', 'SM', 'ST', 'SN', 'SC', 'SL', 'SB', 'KN', 'LC', 'VC',
                               'SR', 'TL', 'TO', 'TT', 'TV', 'VU', 'AZ', 'BN', 'BI', 'KH', 'CM', 'TD', 'KM', 'GQ',
                               'SZ', 'GA', 'GN', 'KG', 'LA', 'MO', 'MR', 'MN', 'NP', 'RW', 'TG', 'UZ', 'ZW', 'BJ',
                               'MG', 'MU', 'MZ', 'AO', 'CI', 'DJ', 'ZM', 'CD', 'CG', 'IQ', 'LY', 'TJ', 'VE', 'ET',
                               'XK'],
         'external_urls': {'spotify': 'https://open.spotify.com/album/5Xd0KCzb0EJtPbUEiyxYVH'},
         'href': 'https://api.spotify.com/v1/albums/5Xd0KCzb0EJtPbUEiyxYVH', 'id': '5Xd0KCzb0EJtPbUEiyxYVH',
         'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273ddac71a12622bdc7e9d3e795',
                     'width': 640},
                    {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02ddac71a12622bdc7e9d3e795',
                     'width': 300},
                    {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851ddac71a12622bdc7e9d3e795',
                     'width': 64}], 'name': '143', 'release_date': '2024-12-20', 'release_date_precision': 'day',
         'type': 'album', 'uri': 'spotify:album:5Xd0KCzb0EJtPbUEiyxYVH', 'artists': [
            {'external_urls': {'spotify': 'https://open.spotify.com/artist/6jJ0s89eD6GaHleKKya26X'},
             'href': 'https://api.spotify.com/v1/artists/6jJ0s89eD6GaHleKKya26X', 'id': '6jJ0s89eD6GaHleKKya26X',
             'name': 'Katy Perry', 'type': 'artist', 'uri': 'spotify:artist:6jJ0s89eD6GaHleKKya26X'}]},
        {'album_type': 'album', 'total_tracks': 17,
         'available_markets': ['AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK',
                               'DO', 'DE', 'EC', 'EE', 'SV', 'FI', 'FR', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'IE',
                               'IT', 'LV', 'LT', 'LU', 'MY', 'MT', 'MX', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE',
                               'PH', 'PL', 'PT', 'SG', 'SK', 'ES', 'SE', 'CH', 'TW', 'TR', 'UY', 'US', 'GB', 'AD',
                               'LI', 'MC', 'ID', 'JP', 'TH', 'VN', 'RO', 'IL', 'ZA', 'SA', 'AE', 'BH', 'QA', 'OM',
                               'KW', 'EG', 'MA', 'DZ', 'TN', 'LB', 'JO', 'PS', 'IN', 'BY', 'KZ', 'MD', 'UA', 'AL',
                               'BA', 'HR', 'ME', 'MK', 'RS', 'SI', 'KR', 'BD', 'PK', 'LK', 'GH', 'KE', 'NG', 'TZ',
                               'UG', 'AG', 'AM', 'BS', 'BB', 'BZ', 'BT', 'BW', 'BF', 'CV', 'CW', 'DM', 'FJ', 'GM',
                               'GE', 'GD', 'GW', 'GY', 'HT', 'JM', 'KI', 'LS', 'LR', 'MW', 'MV', 'ML', 'MH', 'FM',
                               'NA', 'NR', 'NE', 'PW', 'PG', 'PR', 'WS', 'SM', 'ST', 'SN', 'SC', 'SL', 'SB', 'KN',
                               'LC', 'VC', 'SR', 'TL', 'TO', 'TT', 'TV', 'VU', 'AZ', 'BN', 'BI', 'KH', 'CM', 'TD',
                               'KM', 'GQ', 'SZ', 'GA', 'GN', 'KG', 'LA', 'MO', 'MR', 'MN', 'NP', 'RW', 'TG', 'UZ',
                               'ZW', 'BJ', 'MG', 'MU', 'MZ', 'AO', 'CI', 'DJ', 'ZM', 'CD', 'CG', 'IQ', 'LY', 'TJ',
                               'VE', 'ET', 'XK'],
         'external_urls': {'spotify': 'https://open.spotify.com/album/4Zoxsc06EUHRf5GrJPJZ54'},
         'href': 'https://api.spotify.com/v1/albums/4Zoxsc06EUHRf5GrJPJZ54', 'id': '4Zoxsc06EUHRf5GrJPJZ54',
         'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b27376c5a1960013e9203bcd6cd5',
                     'width': 640},
                    {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e0276c5a1960013e9203bcd6cd5',
                     'width': 300},
                    {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d0000485176c5a1960013e9203bcd6cd5',
                     'width': 64}], 'name': 'MIXTAPE PLUTO', 'release_date': '2024-09-20',
         'release_date_precision': 'day', 'type': 'album', 'uri': 'spotify:album:4Zoxsc06EUHRf5GrJPJZ54',
         'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1RyvyyTE3xzB2ZywiAwp0i'},
                      'href': 'https://api.spotify.com/v1/artists/1RyvyyTE3xzB2ZywiAwp0i',
                      'id': '1RyvyyTE3xzB2ZywiAwp0i', 'name': 'Future', 'type': 'artist',
                      'uri': 'spotify:artist:1RyvyyTE3xzB2ZywiAwp0i'}]},
        {'album_type': 'album', 'total_tracks': 10,
         'available_markets': ['AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK',
                               'DO', 'DE', 'EC', 'EE', 'SV', 'FI', 'FR', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'IE',
                               'IT', 'LV', 'LT', 'LU', 'MY', 'MT', 'MX', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE',
                               'PH', 'PL', 'PT', 'SG', 'SK', 'ES', 'SE', 'CH', 'TW', 'TR', 'UY', 'US', 'GB', 'AD',
                               'LI', 'MC', 'ID', 'JP', 'TH', 'VN', 'RO', 'IL', 'ZA', 'SA', 'AE', 'BH', 'QA', 'OM',
                               'KW', 'EG', 'MA', 'DZ', 'TN', 'LB', 'JO', 'PS', 'IN', 'BY', 'KZ', 'MD', 'UA', 'AL',
                               'BA', 'HR', 'ME', 'MK', 'RS', 'SI', 'KR', 'BD', 'PK', 'LK', 'GH', 'KE', 'NG', 'TZ',
                               'UG', 'AG', 'AM', 'BS', 'BB', 'BZ', 'BT', 'BW', 'BF', 'CV', 'CW', 'DM', 'FJ', 'GM',
                               'GE', 'GD', 'GW', 'GY', 'HT', 'JM', 'KI', 'LS', 'LR', 'MW', 'MV', 'ML', 'MH', 'FM',
                               'NA', 'NR', 'NE', 'PW', 'PG', 'PR', 'WS', 'SM', 'ST', 'SN', 'SC', 'SL', 'SB', 'KN',
                               'LC', 'VC', 'SR', 'TL', 'TO', 'TT', 'TV', 'VU', 'AZ', 'BN', 'BI', 'KH', 'CM', 'TD',
                               'KM', 'GQ', 'SZ', 'GA', 'GN', 'KG', 'LA', 'MO', 'MR', 'MN', 'NP', 'RW', 'TG', 'UZ',
                               'ZW', 'BJ', 'MG', 'MU', 'MZ', 'AO', 'CI', 'DJ', 'ZM', 'CD', 'CG', 'IQ', 'LY', 'TJ',
                               'VE', 'ET', 'XK'],
         'external_urls': {'spotify': 'https://open.spotify.com/album/7h0Y4HcaDsuLnXeYmvY7ai'},
         'href': 'https://api.spotify.com/v1/albums/7h0Y4HcaDsuLnXeYmvY7ai', 'id': '7h0Y4HcaDsuLnXeYmvY7ai',
         'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273ee5737c5a60216441f49e376',
                     'width': 640},
                    {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02ee5737c5a60216441f49e376',
                     'width': 300},
                    {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851ee5737c5a60216441f49e376',
                     'width': 64}], 'name': 'Like All Before You', 'release_date': '2024-09-20',
         'release_date_precision': 'day', 'type': 'album', 'uri': 'spotify:album:7h0Y4HcaDsuLnXeYmvY7ai',
         'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/4nUBBtLtzqZGpdiynTJbYJ'},
                      'href': 'https://api.spotify.com/v1/artists/4nUBBtLtzqZGpdiynTJbYJ',
                      'id': '4nUBBtLtzqZGpdiynTJbYJ', 'name': 'The Voidz', 'type': 'artist',
                      'uri': 'spotify:artist:4nUBBtLtzqZGpdiynTJbYJ'}]},
        {'album_type': 'album', 'total_tracks': 8,
         'available_markets': ['AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK',
                               'DO', 'DE', 'EC', 'EE', 'SV', 'FI', 'FR', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'IE',
                               'IT', 'LV', 'LT', 'LU', 'MY', 'MT', 'MX', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE',
                               'PH', 'PL', 'PT', 'SG', 'SK', 'ES', 'SE', 'CH', 'TW', 'TR', 'UY', 'US', 'GB', 'AD',
                               'LI', 'MC', 'ID', 'JP', 'TH', 'VN', 'RO', 'IL', 'ZA', 'SA', 'AE', 'BH', 'QA', 'OM',
                               'KW', 'EG', 'MA', 'DZ', 'TN', 'LB', 'JO', 'PS', 'IN', 'BY', 'KZ', 'MD', 'UA', 'AL',
                               'BA', 'HR', 'ME', 'MK', 'RS', 'SI', 'KR', 'BD', 'PK', 'LK', 'GH', 'KE', 'NG', 'TZ',
                               'UG', 'AG', 'AM', 'BS', 'BB', 'BZ', 'BT', 'BW', 'BF', 'CV', 'CW', 'DM', 'FJ', 'GM',
                               'GE', 'GD', 'GW', 'GY', 'HT', 'JM', 'KI', 'LS', 'LR', 'MW', 'MV', 'ML', 'MH', 'FM',
                               'NA', 'NR', 'NE', 'PW', 'PG', 'PR', 'WS', 'SM', 'ST', 'SN', 'SC', 'SL', 'SB', 'KN',
                               'LC', 'VC', 'SR', 'TL', 'TO', 'TT', 'TV', 'VU', 'AZ', 'BN', 'BI', 'KH', 'CM', 'TD',
                               'KM', 'GQ', 'SZ', 'GA', 'GN', 'KG', 'LA', 'MO', 'MR', 'MN', 'NP', 'RW', 'TG', 'UZ',
                               'ZW', 'BJ', 'MG', 'MU', 'MZ', 'AO', 'CI', 'DJ', 'ZM', 'CD', 'CG', 'IQ', 'LY', 'TJ',
                               'VE', 'ET', 'XK'],
         'external_urls': {'spotify': 'https://open.spotify.com/album/3EzeDYzLp9bcuK162KVDMp'},
         'href': 'https://api.spotify.com/v1/albums/3EzeDYzLp9bcuK162KVDMp', 'id': '3EzeDYzLp9bcuK162KVDMp',
         'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273d47b3c75a1a3f223036be64c',
                     'width': 640},
                    {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02d47b3c75a1a3f223036be64c',
                     'width': 300},
                    {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851d47b3c75a1a3f223036be64c',
                     'width': 64}], 'name': 'The Genuine Articulate', 'release_date': '2024-09-20',
         'release_date_precision': 'day', 'type': 'album', 'uri': 'spotify:album:3EzeDYzLp9bcuK162KVDMp',
         'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0eVyjRhzZKke2KFYTcDkeu'},
                      'href': 'https://api.spotify.com/v1/artists/0eVyjRhzZKke2KFYTcDkeu',
                      'id': '0eVyjRhzZKke2KFYTcDkeu', 'name': 'The Alchemist', 'type': 'artist',
                      'uri': 'spotify:artist:0eVyjRhzZKke2KFYTcDkeu'}]}

    ]


def mock_artists_metadata() -> list:
    return [
        {'external_urls': {'spotify': 'https://open.spotify.com/artist/4rj3KWaLAnuxgtMMkypZhf'},
         'followers': {'href': None, 'total': 14807}, 'genres': ['italian pop'],
         'href': 'https://api.spotify.com/v1/artists/4rj3KWaLAnuxgtMMkypZhf', 'id': '4rj3KWaLAnuxgtMMkypZhf',
         'images': [{'url': 'https://i.scdn.co/image/ab6761610000e5eb6a03515ae09c37bd80cc99a8', 'height': 640,
                     'width': 640},
                    {'url': 'https://i.scdn.co/image/ab676161000051746a03515ae09c37bd80cc99a8', 'height': 320,
                     'width': 320},
                    {'url': 'https://i.scdn.co/image/ab6761610000f1786a03515ae09c37bd80cc99a8', 'height': 160,
                     'width': 160}], 'name': 'Jamie xx', 'popularity': 74, 'type': 'artist',
         'uri': 'spotify:artist:4rj3KWaLAnuxgtMMkypZhf'},
        {'external_urls': {'spotify': 'https://open.spotify.com/artist/6jJ0s89eD6GaHleKKya26X'},
         'followers': {'href': None, 'total': 35670205}, 'genres': ['pop'],
         'href': 'https://api.spotify.com/v1/artists/6jJ0s89eD6GaHleKKya26X', 'id': '6jJ0s89eD6GaHleKKya26X',
         'images': [{'url': 'https://i.scdn.co/image/ab6761610000e5eb0988562f78810e47a6e3325f', 'height': 640,
                     'width': 640},
                    {'url': 'https://i.scdn.co/image/ab676161000051740988562f78810e47a6e3325f', 'height': 320,
                     'width': 320},
                    {'url': 'https://i.scdn.co/image/ab6761610000f1780988562f78810e47a6e3325f', 'height': 160,
                     'width': 160}], 'name': 'Katy Perry', 'popularity': 87, 'type': 'artist',
         'uri': 'spotify:artist:6jJ0s89eD6GaHleKKya26X'},
        {'external_urls': {'spotify': 'https://open.spotify.com/artist/1RyvyyTE3xzB2ZywiAwp0i'},
         'followers': {'href': None, 'total': 20000243},
         'genres': ['atl hip hop', 'hip hop', 'rap', 'southern hip hop', 'trap'],
         'href': 'https://api.spotify.com/v1/artists/1RyvyyTE3xzB2ZywiAwp0i', 'id': '1RyvyyTE3xzB2ZywiAwp0i',
         'images': [{'url': 'https://i.scdn.co/image/ab6761610000e5eb7565b356bc9d9394eefa2ccb', 'height': 640,
                     'width': 640},
                    {'url': 'https://i.scdn.co/image/ab676161000051747565b356bc9d9394eefa2ccb', 'height': 320,
                     'width': 320},
                    {'url': 'https://i.scdn.co/image/ab6761610000f1787565b356bc9d9394eefa2ccb', 'height': 160,
                     'width': 160}], 'name': 'Future', 'popularity': 93, 'type': 'artist',
         'uri': 'spotify:artist:1RyvyyTE3xzB2ZywiAwp0i'},
        {'external_urls': {'spotify': 'https://open.spotify.com/artist/2rasxNiJk2a3rNeGFss3x5'},
         'followers': {'href': None, 'total': 14046}, 'genres': ['modern alternative rock'],
         'href': 'https://api.spotify.com/v1/artists/2rasxNiJk2a3rNeGFss3x5', 'id': '2rasxNiJk2a3rNeGFss3x5',
         'images': [{'url': 'https://i.scdn.co/image/ab6761610000e5ebe4f5ea24a1064015a57b9a0e', 'height': 640,
                     'width': 640},
                    {'url': 'https://i.scdn.co/image/ab67616100005174e4f5ea24a1064015a57b9a0e', 'height': 320,
                     'width': 320},
                    {'url': 'https://i.scdn.co/image/ab6761610000f178e4f5ea24a1064015a57b9a0e', 'height': 160,
                     'width': 160}], 'name': 'The Voidz', 'popularity': 44, 'type': 'artist',
         'uri': 'spotify:artist:2rasxNiJk2a3rNeGFss3x5'},
        {'external_urls': {'spotify': 'https://open.spotify.com/artist/4wEzanUDeA8SB82tGH8gc1'},
         'followers': {'href': None, 'total': 3}, 'genres': ['alternative hip hop', 'drumless hip hop', 'hip hop',
                                                             'instrumental hip hop', 'west coast rap'],
         'href': 'https://api.spotify.com/v1/artists/4wEzanUDeA8SB82tGH8gc1', 'id': '4wEzanUDeA8SB82tGH8gc1',
         'images': [{'url': 'https://i.scdn.co/image/ab67616d0000b27340bed0d26dd5fac71e9df080', 'height': 640,
                     'width': 640},
                    {'url': 'https://i.scdn.co/image/ab67616d00001e0240bed0d26dd5fac71e9df080', 'height': 300,
                     'width': 300},
                    {'url': 'https://i.scdn.co/image/ab67616d0000485140bed0d26dd5fac71e9df080', 'height': 64,
                     'width': 64}], 'name': 'The Alchemist', 'popularity': 0, 'type': 'artist',
         'uri': 'spotify:artist:4wEzanUDeA8SB82tGH8gc1'}
    ]

def get_expected_list() -> list:
    return ['Jamie xx', 'In Waves', 'Katy Perry', '143', 'Future', 'MIXTAPE PLUTO', 'The Voidz',
             'Like All Before You', 'The Alchemist', 'The Genuine Articulate']


def setup_db() :
    env_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "testing.env")
    load_dotenv(dotenv_path=env_file_path, override=True)

    from App.init.config import Config as Appconfig

    Appconfig.DB_DRIVER

    ini_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..","alembic.ini")

    alembic_cfg = Config(ini_file_path)
    migrations_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..","App","migrations")
    alembic_cfg.set_main_option("script_location", migrations_path)
    command.upgrade(alembic_cfg, "head")


class TunescraperTest(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    @patch.object(sys, "argv", ["tunescraper", "-o"])
    def test_output_option(self, stdout):
        from tunescraper import main
        from App.init.containers import ScraperContainer

        container = ScraperContainer()
        container.request_client.override(providers.Singleton(MockRequestsClient, mock_request_client_response()))
        container.metadata_client.override(providers.Singleton(MockMetadataClient, mock_albums_metadata(), mock_artists_metadata()))

        container.wire(modules=['tunescraper'])
        main()

        printed_message = stdout.getvalue().strip()

        self.assertTrue(all(found in printed_message for found in get_expected_list()))

    @pytest.mark.skip(reason="DB option to be implemented")
    @patch.object(sys, "argv", ["tunescraper", "-db"])
    def test_database_option(self):
        setup_db()
        from tunescraper import main
        from App.init.containers import ScraperContainer

        container = ScraperContainer()
        container.request_client.override(providers.Singleton(MockRequestsClient, mock_request_client_response()))
        container.metadata_client.override(
            providers.Singleton(MockMetadataClient, mock_albums_metadata(), mock_artists_metadata()))

        container.wire(modules=['tunescraper'])
        main()

        from App.init.database import engine

        with engine.connect() as connection:
            result = connection.execute("SELECT * FROM releases")
            releases = result.fetchall()

        self.assertTrue(releases)

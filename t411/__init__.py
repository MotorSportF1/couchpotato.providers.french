from .main import t411
from couchpotato.core.logger import CPLog

log = CPLog(__name__)

def autoload():
    log.debug('load success')
    return t411()

config = [{
    'name': 't411',
    'groups': [
        {
            'tab': 'searcher',
            'list': 'torrent_providers',
            'name': 'T411',
            'description': 'See <a href="https://t411.al">T411</a>',
            'icon': 'iVBORw0KGgoAAAANSUhEUgAAABsAAAAQCAMAAADQzfSkAAAB11BMVEUEAgQMgswcQmSMjpykzuwEJkw8UlzU5uwMZpQcKjwEEixUhqy85vyUtsRUvvQsSmzEysxEbpSsxtwENmTk8vwEUnwUHiR0hpyUwtQEBiQcUnwUKkQkcqwcNkwEGjys1uy81uT09vwEWowEKlRcXmxccoQEChyMnrS0ytw8XoQEdrRUkrx0qsykxtTM3uQEAhQELkzU6vwcMkwMFjxkgpzM7vyctszk+vyElpycxtS83vScoqw0hrQMJjwEFiwkUnxUfpwEPmQEUowEDjQsPlQMGjwMXpSEorwEBhR0nrys0uREUmQcYpTM6uyMuty8wswEOmSUxuQECiQ0eqQkPlwEHkTE1tz8/vwEXpxceoSMprS00txMYnwUcqzk6uwkMkRsgozs/vw0UmwMjtQMTnyk0uQEKkw8Umzc4uQEbqwkLjQEEjRcgqSUtsxcuuzM0tRUcoTk9vwMUoQcHiyUxtQUXowULkwkepQcNlQEGkSs2vS82uT8+vwEXpQELly0ztREZoxEhqRkepSkusTc7vwMKkxshpx8qsTE3uyUprQEerycprQEVpSEpsQ0VnTM8vzk/vy8xswEAhyElqScxtwEFjRUfqQEBhx0nsTM6vQEOmwECiwkMkxw1dROAAAAB3RJTUUH4QULDx8WPP+WBAAAAPtJREFUeJxjCIeCGhBQBOJwOGBAkatRBMqG16DIAUVnCk3ra5g2w0++RQSmlwEiU5XHKDNbUlLS2dm4zkdmml8NVA5oUp6MU1GR82xVQxVj8W7jYv7KDriZ7LH+6XU9s6U1FMT7FMyKhfwle0HmgvQpmqnkq9T1SJo1dasbzzGTBKKm8Bqovm5O60mznPjZy4TUJefkz57jP3saTF+4gGtYsXKEKns+i0axS/5s/nznGXD7auJVmbO7ZhUZmzHP5hcwDmF21UDIxZm0zu5ycq6cU+bKyjrLXrO9BuH38HBF92CtFCWOYO12FgVF9DALDzedEI4KGMJxA3LlABnYkeU4167DAAAAAElFTkSuQmCC',
            'wizard': True,
            'options': [
                {
                    'name': 'enabled',
                    'type': 'enabler',
                    'default': False,
                },
                {
                    'name': 'username',
                    'default': '',
                },
                {
                    'name': 'password',
                    'default': '',
                    'type': 'password',
                },
                {
                    'name': 'ignore_year',
                    'label': 'ignore year',
                    'default': 0,
                    'type': 'bool',
                    'description': 'Will ignore the year in the search results',
                },
                {
                    'name': 'seed_ratio',
                    'label': 'Seed ratio',
                    'type': 'float',
                    'default': 1,
                    'description': 'Will not be (re)moved until this seed ratio is met.',
                },
                {
                    'name': 'seed_time',
                    'label': 'Seed time',
                    'type': 'int',
                    'default': 40,
                    'description': 'Will not be (re)moved until this seed time (in hours) is met.',
                },
                {
                    'name': 'extra_score',
                    'advanced': True,
                    'label': 'Extra Score',
                    'type': 'int',
                    'default': 20,
                    'description': 'Starting score for each release found via this provider.',
                }
            ],
        },
    ],
}]

python-pointdns
===========

pointhq.com API client.

This module provides easy access to point zone & record management. For information about the services offered on Point see [the website](http://pointhq.com)
This module is based on a fork of [Richard Gray's](https://github.com/vortura/pointhq) pointhq module which is based on [Mike Yumatov's](https://github.com/yumike/pointhq) pointhq module
with the following additional modifications:

- Added support for Python3.x
- Retrieve zones by groups
- Record type validation

## Authentication

To access your Point account, you'll need to define your username & apitoken. The username is your email address and the apitoken is the API token which, can be found in My Account tab.

## Installation

Install ``pointdns`` with pip:

    $ pip install pointdns

or directly from GitHub

    $ pip install git+https://github.com/copper/python-pointdns.git

It will also install `requests` library.

## Usage example

* Create new `pointdns.Point` object:
```python
from pointdns import Point
point = Point(username='john@example.com', apitoken='secret-key')
```
* Play with zones::
```python
zones = point.zones.retrieve()
new_zone = point.zones.create(name='example.com')
```
```python
zone = point.zones(1).retrieve()
point.zones(1).update(group='Clients')
zones_group_clients = point.zones.retrieve(group='Clients')
point.zones(1).delete()
```
* Play with zone records::
```python
zone_records = point.zones(1).records.retrieve()
new_record = point.zones(1).records.create(
                name='example.com.', data='123.45.67.89', record_type='A')
```
```python
zone_record = point.zones(1).records(1).retrieve
point.zones(1).records(1).update(data='234.56.78.90')
point.zones(1).records(1).delete()
```
## Contributing

Feel free to fork, send pull requests or report bugs and issues on github.

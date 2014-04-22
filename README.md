python-pointdns
===============

pointhq.com API client.

This is pointdns module based on a fork of Richard Gray pointhq module which is based on Mike Yumatov's pointhq module
with the following additional modifications:

- Added support for Python3.x
- Retrieve zones by groups
- Record type validation


Installation
------------

Install ``pointdns`` with pip::

    $ pip install pointdns

It will also install ``requests`` library.

Usage example
-------------

1. Create new ``pointdns.Point`` object::

    import pointdns
    point = Point(username='john@example.com', apitoken='secret-key')

2. Play with zones::

    zones = point.zones.retrieve()
    new_zone = point.zones.create(name='example.com')

    zone = point.zones(1).retrieve()
    point.zones(1).update(group='Clients')
    zones_group_clients = point.zones.retrieve(group='Clients')
    point.zones(1).delete()

3. Play with zone records::

    zone_records = point.zones(1).records.retrieve()
    new_record = point.zones(1).records.create(name='example.com.', data='123.45.67.89', record_type='A')

    zone_record = point.zones(1).records(1).retrieve
    point.zones(1).records(1).update(data='234.56.78.90')
    point.zones(1).records(1).delete()

Contributing
------------

Feel free to fork, send pull requests or report bugs and issues on github.
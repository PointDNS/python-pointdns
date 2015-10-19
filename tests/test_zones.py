from __future__ import with_statement

import unittest2
from mock import Mock

from pointdns import Point
from pointdns import exceptions
from pointdns.helpers import Response


class ZoneTests(unittest2.TestCase):

    def setUp(self):
        self.auth = ('john@example.com', 'secret-key')
        self.request = Mock()
        self.point = Point(self.auth[0], self.auth[1], self.request)

    def test_collection_retrieve(self):
        self.request.return_value = Response(200, '[{"zone": {"id": 1}}]')
        zone = self.point.zones.retrieve()
        self.request.assert_called_once_with('get', '/zones', self.auth, None, {})
        self.assertEqual(zone, [{'zone': {'id': 1}}])

    def test_collection_retrieve_by_groups(self):
        self.request.return_value = Response(200, '[{"zone": {"id": 1}}]')
        zone = self.point.zones.retrieve(group='Clients')
        self.request.assert_called_once_with('get', '/zones', self.auth, None, {'group': 'Clients'})
        self.assertEqual(zone, [{'zone': {'id': 1}}])

    def test_collection_retrieve_failure(self):
        self.request.return_value = Response(201)
        with self.assertRaises(exceptions.UnknownError):
            self.point.zones.retrieve()

    def test_collection_create(self):
        self.request.return_value = Response(201, '{"zone": {"id": 1}}')
        zone = self.point.zones.create(name='example.com')
        self.request.assert_called_once_with('post', '/zones', self.auth, {
            'zone': {
                'name': 'example.com',
            },
        }, None)
        self.assertEqual(zone, {'zone': {'id': 1}})

    def test_collection_create_failure(self):
        self.request.return_value = Response(422, '["error message"]')
        with self.assertRaises(exceptions.UnprocessableEntityError):
            self.point.zones.create(name='example.com')

    def test_collection_create_unknown_failure(self):
        self.request.return_value = Response(200)
        with self.assertRaises(exceptions.UnknownError):
            self.point.zones.create(name='example.com')

    def test_member_retrieve(self):
        self.request.return_value = Response(200, '{"zone": {"id": 1}}')
        zone = self.point.zones(1).retrieve()
        self.request.assert_called_once_with('get', '/zones/1', self.auth, None, None)
        self.assertEqual(zone, {'zone': {'id': 1}})

    def test_member_retrieve_failure(self):
        self.request.return_value = Response(404)
        with self.assertRaises(exceptions.NotFoundError):
            self.point.zones(1).retrieve()

    def test_member_retrieve_unknown_failure(self):
        self.request.return_value = Response(201)
        with self.assertRaises(exceptions.UnknownError):
            self.point.zones(1).retrieve()

    def test_member_update(self):
        self.request.return_value = Response(202)
        self.assertIsNone(self.point.zones(1).update(group='clients'))
        self.request.assert_called_once_with('put', '/zones/1', self.auth, {
            'zone': {
                'group': 'clients',
            }
        }, None)

    def test_member_update_failure(self):
        self.request.return_value = Response(422, '["error message"]')
        with self.assertRaises(exceptions.UnprocessableEntityError):
            self.point.zones(1).update(group='clients')

    def test_member_update_unknown_failure(self):
        self.request.return_value = Response(404)
        with self.assertRaises(exceptions.UnknownError):
            self.point.zones(1).update(group='clients')

    def test_member_delete(self):
        self.request.return_value = Response(202)
        self.assertIsNone(self.point.zones(1).delete())
        self.request.assert_called_once_with('delete', '/zones/1', self.auth, None, None)

    def test_member_delete_failure(self):
        self.request.return_value = Response(409, '["error message"]')
        with self.assertRaises(exceptions.ConflictError):
            self.point.zones(1).delete()

    def test_member_delete_unknown_failure(self):
        self.request.return_value = Response(404)
        with self.assertRaises(exceptions.UnknownError):
            self.point.zones(1).delete()

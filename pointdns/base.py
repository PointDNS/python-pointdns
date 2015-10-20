import json

from functools import wraps
from . import exceptions


class BaseResource(object):

    name = None
    path_pattern = None
    record_types = [
        'A', 'CNAME', 'MX', 'TXT', 'SRV', 'AAAA', 'SSHFP', 'PTR', 'ALIAS']

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    @property
    def path(self):
        return self.path_pattern % self.kwargs

    def request(self, method, data=None, query_data=None):
        if data is not None:
            data = {self.name: data}
        return self.kwargs['request_func'](method, self.path, data, query_data)

    @classmethod
    def validate(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if 'record_type' in kwargs and \
                    kwargs['record_type'].upper() not in cls.record_types:
                raise exceptions.RecordTypeError(
                    'Bad record: %s' % kwargs['record_type'])
            return func(*args, **kwargs)
        return wrapper


class BaseMember(BaseResource):

    def retrieve(self):
        response = self.request('get')
        if response.status == 200:
            return json.loads(response.content)
        if response.status == 404:
            raise exceptions.NotFoundError
        raise exceptions.UnknownError(response)

    @BaseResource.validate
    def update(self, **kwargs):
        response = self.request('put', kwargs)
        if response.status == 202:
            return
        if response.status == 422:
            raise exceptions.UnprocessableEntityError(
                json.loads(response.content))
        raise exceptions.UnknownError(response)

    def delete(self):
        response = self.request('delete')
        if response.status == 202:
            return
        if response.status == 409:
            raise exceptions.ConflictError
        raise exceptions.UnknownError(response)


class BaseCollection(BaseResource):

    member_class = None

    def __call__(self, id):
        kwargs = self.kwargs.copy()
        kwargs['id'] = id
        return self.member_class(**kwargs)

    def retrieve(self, **kwargs):
        response = self.request('get', query_data=kwargs)
        if response.status == 200:
            return json.loads(response.content)
        raise exceptions.UnknownError(response)

    @BaseResource.validate
    def create(self, **kwargs):
        response = self.request('post', kwargs)
        if response.status == 201:
            return json.loads(response.content)
        if response.status == 422:
            raise exceptions.UnprocessableEntityError(
                json.loads(response.content))
        raise exceptions.UnknownError(response)

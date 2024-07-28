#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
Descriptive HTTP status codes, for code readability.

See RFC 2616 and RFC 6585.

RFC 2616: http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
RFC 6585: http://tools.ietf.org/html/rfc6585
"""
import time
from werkzeug.exceptions import HTTPException

from . import httpstatus


class Error(HTTPException):
    def __init__(self, message, code=None):
        super(Error, self).__init__()
        self.message = message
        if code is not None:
            self.code = code

    def to_dict(self):
        e = dict(error={})
        nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        e["error"] = {"message": self.message,
                      "type": self.__class__.__name__,
                      "timestamp": nowtime}
        return e


class RequestError(Error):
    code = httpstatus.HTTP_400_BAD_REQUEST


class InvalidParam(RequestError):
    def __init__(self, param_name):
        self.message = "Invalid Param: %s" % param_name


class NoParam(RequestError):
    def __init__(self, param_name):
        self.message = "No Param:%s" % param_name


class ResourceExists(RequestError):
    def __init__(self, res, **kv):
        o = {"resource": res}
        o.update(kv)
        self.message = "Resource %s Exists" % res


class NotFound(RequestError):
    def __init__(self, param_name):
        self.message = "Resource not found: %s" % param_name


class ForbidHandle(RequestError):
    code = httpstatus.HTTP_403_FORBIDDEN

    def __init__(self, msg):
        self.message = "%s" % msg


class Unauthorized(RequestError):
    code = httpstatus.HTTP_401_UNAUTHORIZED

    def __init__(self, msg):
        self.message = "%s" % msg


class ServiceError(Error):
    code = httpstatus.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, service, code=None):
        self.message = "Service error.'%s' " % service

#!/usr/bin/env python3
"""
Module defines class auth
"""

from flask import request


class Auth:
    """
        class is the template for all authentication system implementd.
    """

    def __init__(self):
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:

    def authorization_header(self, request=None) -> str:

    def current_user(self, request=None) -> TypeVar('User'):

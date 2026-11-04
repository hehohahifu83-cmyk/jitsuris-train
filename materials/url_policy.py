"""転送先へ接続する前に、呼び出し側のURLポリシーを検査する。"""
from urllib.parse import urlparse
from urllib.request import HTTPRedirectHandler, build_opener

class AllowedRedirect(HTTPRedirectHandler):
    def __init__(self, check):
        self.check = check

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if not self.check(newurl):
            raise ValueError(f"redirected outside the allowed hosts: {urlparse(newurl).hostname}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)

def allowed_open(req, timeout, check):
    if not check(req.full_url):
        raise ValueError(f"URL not allowed: {urlparse(req.full_url).hostname}")
    return build_opener(AllowedRedirect(check)).open(req, timeout=timeout)

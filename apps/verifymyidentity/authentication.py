from social_core.backends.open_id_connect import OpenIdConnectAuth

__author__ = "Alan Viars"


class SocialCoreOpenIdConnect(OpenIdConnectAuth):
    name = 'verifymyidentity-openidconnect'
    # differs from value in discovery document
    # http://openid.net/specs/openid-connect-core-1_0.html#rfc.section.15.6.2
    # ID_TOKEN_ISSUER = 'http://verifymyidentity:8001'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.OIDC_ENDPOINT = self.setting('OIDC_ENDPOINT', '')

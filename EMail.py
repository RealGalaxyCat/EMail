import re
import whois

class EmailProvider:
    def __init__(self, name, tld, registrar, registrant_country, creation_date, expiration_date, last_updated, status, statuses, dnssec, name_servers, registrant, emails):
        self.name = name
        self.tld = tld
        self.registrar = registrar
        self.registrant_country = registrant_country
        self.creation_date = creation_date
        self.expiration_date = expiration_date
        self.last_updated = last_updated
        self.status = status
        self.statuses = statuses
        self.dnssec = dnssec
        self.name_servers = name_servers
        self.registrant = registrant
        self.emails = emails


class EMail:
    def __init__(self, email: str):
        self.email = email

    def has_valid_format(self) -> bool:
        email_regex = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
        if re.search(email_regex, self.email):
            return True
        else:
            return False

    @property
    def email_provider(self):
        url = self.email.split("@")[1]
        data = whois.get(url)
        return EmailProvider(data["name"], data["tld"], data["registrar"], data["registrant_country"], data["creation_date"], data["expiration_date"], data["last_updated"], data["status"], data["statuses"], data["dnssec"], data["name_servers"], data["registrant"], data["emails"])


        
        

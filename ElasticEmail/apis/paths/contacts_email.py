from ElasticEmail.paths.contacts_email.get import ApiForget
from ElasticEmail.paths.contacts_email.put import ApiForput
from ElasticEmail.paths.contacts_email.delete import ApiFordelete


class ContactsEmail(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass

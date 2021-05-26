class ContactList(list):
    def search(self, name):
        """Return all contacts that contain the search value in their name"""

        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contact = ContactList()

    def __init__(self, name, email, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        Contact.all_contact.append(self)


class AddressHolder:
    def __init__(self, street="", city="", state="", code="", **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend(Contact, AddressHolder):
    """Add phone attribute on the contact"""

    def __init__(self, phone, **kwargs):
        super().__init__(**kwargs)
        self.phone = phone


class Supplier(Contact):
    def order(self, order):
        print("Of this were a real system we would send" f"'{order}' order to '{self.name}'")


if __name__ == '__main__':
    c1 = Contact("Jonh A", "jonhA@email.com")
    c2 = Contact("Jonh B", "jonhB@email.com")
    c3 = Contact("Jenna C", "jonhC@email.com")

    [c.name for c in Contact.all_contact.search('Jonh')]

    s = Supplier("Sup Plier", "supplier@email.com")
    f = Friend("123456", street="TQK", email="fuck@mail", name="fuck", city="HN")
    s.order("I need pliers")
    print("Hello")

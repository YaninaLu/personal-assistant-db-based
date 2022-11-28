from db_session import session
from models import Contact
import datetime
from validate_input import verify_name, verify_phone, verify_birthday, verify_email


DATE_FORMAT = "%d.%m.%Y"


def add_contact(name, birthday, email, phone, address):
    try:
        if birthday:
            birthday = verify_birthday(convert_bd(birthday))

        contact = Contact(name=verify_name(name), birthday=birthday, email=verify_email(email),
                          phone=verify_phone(phone), address=address)
        session.add(contact)
        session.commit()

        return "New contact was successfully added!"

    except Exception as err:
        return f"Something went wrong: {err}"


def remove_contact(name):
    contact_query = session.query(Contact).filter(Contact.name == name)
    contact = contact_query.first()
    if contact:
        contact_query.delete()
        session.commit()
        return f"{name} was successfully removed from your contact book."
    else:
        return f"{name} wasn't found in your contact book."


def search_contact(name_seed, phone_seed, email_seed):
    if name_seed:
        result = session.query(Contact).filter(Contact.name.like("%" + name_seed + "%")).all()
    elif phone_seed:
        result = session.query(Contact).filter(Contact.phone.like("%" + phone_seed + "%")).all()
    elif email_seed:
        result = session.query(Contact).filter(Contact.email.like("%" + email_seed + "%")).all()
    else:
        return "Can search contacts only by name, phone, or email."

    if len(result) > 0:
        res = []
        for r in result:
            res.append([r.name, r.phone, r.email, r.birthday, r.address])
        return res
    else:
        return "Search wasn't successful."


def convert_bd(birthday):
    try:
        birthday_date = datetime.datetime.strptime(birthday, DATE_FORMAT).date()
    except ValueError:
        raise ValueError(f"{birthday} does not march format '%d.%m.%Y'")
    return birthday_date


def change_contact(attrs_to_update):
    contact_query = session.query(Contact).filter(Contact.name == attrs_to_update.get("name"))
    contact = contact_query.first()
    if not contact:
        return "No contact with this name found."

    for attr, value in attrs_to_update.items():
        if value:
            if attr == "birthday":
                setattr(contact, attr, verify_birthday(value))
            elif attr == "email":
                setattr(contact, attr, verify_email(value))
            elif attr == "phone":
                setattr(contact, attr, verify_phone(value))
            else:
                setattr(contact, attr, value)

    session.add(contact)
    session.commit()

    return "The contact was changed successfully."

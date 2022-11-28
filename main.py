import argparse

from db_session import session
from repository.repository_notes import add_note, remove_note, search_note, change_note
from repository.repository_contacts import add_contact, remove_contact, search_contact, change_contact


parser = argparse.ArgumentParser(description="Personal Assistant")
parser.add_argument("--action", "-a", help="Commands: add, remove, search, change", required=True)
parser.add_argument("--target", "-t", help="Targets: contact, note", required=True)

group_contacts = parser.add_argument_group("contacts", "arguments to work with contacts")
group_contacts.add_argument("--name")
group_contacts.add_argument("--birthday")
group_contacts.add_argument("--email")
group_contacts.add_argument("--phone")
group_contacts.add_argument("--address")

group_notes = parser.add_argument_group("notes", "arguments to work with notes")
group_notes.add_argument("--title")
group_notes.add_argument("--text")
group_notes.add_argument("--tags")

args = vars(parser.parse_args())
action = args.get("action")

if args["target"] == "contact":
    name = args.get("name")
    birthday = args.get("birthday")
    email = args.get("email")
    phone = args.get("phone")
    address = args.get("address")
elif args["target"] == "note":
    title = args.get("title")
    text = args.get("text")
    tags = args.get("tags")


def work_with_contacts():
    match action:
        case "add":
            return add_contact(name, birthday, email, phone, address)
        case "remove":
            return remove_contact(name)
        case "search":
            return search_contact(name, phone, email)
        case "change":
            attrs_to_update = {
                "name": name,
                "birthday": birthday,
                "email": email,
                "phone": phone,
                "address": address
            }
            return change_contact(attrs_to_update)
        case _:
            print("Unknown command")


def work_with_notes():
    match action:
        case "add":
            return add_note(title, text, tags)
        case "remove":
            return remove_note(title)
        case "search":
            return search_note(title, text, tags)
        case "change":
            return change_note(title, text, tags)
        case _:
            return "Unknown command"


def main():
    if args["target"] == "contact":
        return work_with_contacts()
    elif args["target"] == "note":
        return work_with_notes()
    else:
        return "Unknown target."


if __name__ == '__main__':
    print(main())
    session.close()

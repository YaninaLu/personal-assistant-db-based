from db_session import session
from models import Note, Tag


def add_note(title, text, tags):
    try:
        note = Note(title=title, text=text)
        session.add(note)
        add_tags(note, tags)
        session.commit()
        return "The note was created successfully!"

    except Exception as err:
        return f"Something went wrong: {err}"


def remove_note(title):
    note_query = session.query(Note).filter(Note.title == title)
    note = note_query.first()
    if note:
        note.tags.clear()
        note_query.delete()
        session.commit()
        return f"{title} was successfully removed from your notes."
    else:
        return f"{title} wasn't found in your notes."


def search_note(title_seed, text_seed, tags_seed):
    if title_seed:
        result = session.query(Note).filter(Note.title.like("%" + title_seed + "%")).all()
    elif text_seed:
        result = session.query(Note).filter(Note.text.like("%" + text_seed + "%")).all()
    elif tags_seed:
        result = session.query(Note).filter(Note.tags.any(name=tags_seed)).all()
    else:
        return "Can search contacts only by name, phone, or email."

    if len(result) > 0:
        res = []
        for r in result:
            res.append([r.title, r.text, [tag.name for tag in r.tags]])
        return res
    else:
        return "Search wasn't successful."


def change_note(title, new_text, tags):
    note_query = session.query(Note).filter(Note.title == title)
    note = note_query.first()
    if not note:
        return "No note with this title found."

    setattr(note, "text", new_text)
    session.add(note)
    add_tags(note, tags)
    session.commit()

    return "The note was changed successfully."


def add_tags(note, tags):
    tags = tags.strip().split()
    for tag in tags:
        tag_query = session.query(Tag).filter(Tag.name == tag)
        tag_exists = tag_query.first()

        if not tag_exists:
            tag = Tag(name=tag)
            session.add(tag)
            note.tags.append(tag)
            continue

        note.tags.append(tag_exists)

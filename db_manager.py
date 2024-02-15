import json


def load_data():
    """Loads data from the JSON file."""
    with open("db.json", "r") as f:
        return json.load(f)


def save_data(data):
    """Saves data to the JSON file."""
    with open("db.json", "w") as f:
        json.dump(data, f, indent=4)


def get_contacts():
    """Returns all contacts."""
    data = load_data()
    return data["contacts"]


def get_contact(contact_id):
    """Returns a specific contact by ID."""
    data = load_data()
    for contact in data["contacts"]:
        if contact["id"] == contact_id:
            return contact
    return None


def create_contact(name, phone, email):
    """Creates a new contact."""
    data = load_data()
    new_id = max(contact["id"] for contact in data["contacts"]) + 1
    new_contact = {"id": new_id, "name": name, "phone": phone, "email": email}
    data["contacts"].append(new_contact)
    save_data(data)


def update_contact(contact_id, name, phone, email):
    """Updates a contact."""
    data = load_data()
    for contact in data["contacts"]:
        if contact["id"] == contact_id:
            contact["name"] = name
            contact["phone"] = phone
            contact["email"] = email
            save_data(data)
            return
    raise ValueError("Contact not found")


def delete_contact(contact_id):
    """Deletes a contact."""
    data = load_data()
    for i, contact in enumerate(data["contacts"]):
        if contact["id"] == contact_id:
            del data["contacts"][i]
            save_data(data)
            return
    raise ValueError("Contact not found")


def get_all_commitments():
    """Returns all commitments."""
    data = load_data()
    return data["commitments"]


def get_commitment(commitment_id):
    """Returns a specific commitment by ID."""
    data = load_data()
    for commitment in data["commitments"]:
        if commitment["id"] == commitment_id:
            return commitment
    return None


def create_commitment(description, date, location, time):
    """Creates a new commitment."""
    data = load_data()
    new_id = max(commitment["id"] for commitment in data["commitments"]) + 1
    new_commitment = {
        "id": new_id,
        "description": description,
        "date": date,
        "location": location,
        "time": time,
    }
    data["commitments"].append(new_commitment)
    save_data(data)


def update_commitment(commitment_id, description, date, location):
    """Updates a commitment."""
    data = load_data()
    for commitment in data["commitments"]:
        if commitment["id"] == commitment_id:
            commitment["description"] = description
            commitment["date"] = date
            commitment["location"] = location
            save_data(data)
            return
    raise ValueError("Commitment not found")


def delete_commitment(commitment_id):
    """Deletes a commitment."""
    data = load_data()
    for i, commitment in enumerate(data["commitments"]):
        if commitment["id"] == commitment_id:
            del data["commitments"][i]
            save_data(data)
            return
    raise ValueError("Commitment not found")


def add_contact_to_commitment(commitment_id, contact_id):
    """Adds a contact to a commitment."""
    data = load_data()
    new_commitment_contact = {"commitment_id": commitment_id, "contact_id": contact_id}
    data["commitment_contact"].append(new_commitment_contact)
    save_data(data)


def remove_contact_from_commitment(commitment_id, contact_id):
    """Removes a contact from a commitment."""
    data = load_data()
    for i, commitment_contact in enumerate(data["commitment_contact"]):
        if (
            commitment_contact["commitment_id"] == commitment_id
            and commitment_contact["contact_id"] == contact_id
        ):
            del data["commitment_contact"][i]
            save_data(data)
            return
    raise ValueError("Contact not found in commitment")


def get_commitments_for_contact(contact_id):
    """Returns all commitments associated with a contact."""
    data = load_data()
    commitments = []
    for commitment_contact in data["commitment_contact"]:
        if commitment_contact["contact_id"] == contact_id:
            commitment_id = commitment_contact["commitment_id"]
            for commitment in data["commitments"]:
                if commitment["id"] == commitment_id:
                    commitments.append(commitment)
                    break
    return commitments


def get_contacts_for_commitment(commitment_id):
    """Returns all contacts associated with a commitment."""
    data = load_data()
    contacts = []
    for commitment_contact in data["commitment_contact"]:
        if commitment_contact["commitment_id"] == commitment_id:
            contact_id = commitment_contact["contact_id"]
            for contact in data["contacts"]:
                if contact["id"] == contact_id:
                    contacts.append(contact)
                    break
    return contacts

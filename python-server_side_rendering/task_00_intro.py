import os

def generate_invitations(template, attendees):
    """
    Generates invitation files from a given template and a list of attendees.

    :param template: Invitation template as a string.
    :param attendees: List of dictionaries containing attendee details.
    """
    if not isinstance(template, str):
        print("Error: The template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return

    if not attendees:
        print("Error: No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, start=1):
        filled_template = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )
        output_filename = f"output_{i}.txt"

        with open(output_filename, "w", encoding="utf-8") as output_file:
            output_file.write(filled_template)

        print(f"Invitation generated: {output_filename}")

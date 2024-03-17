from datetime import datetime

class event:
    """A class representing an event."""
    def __init__(self, name, location, start_date, end_date):
        """Initialize an Event object with the specified attributes.
        Args:
            name (str): The name of the event.
            location (str): The location of the event.
            start_date (datetime): The start date and time of the event.
            end_date (datetime): The end date and time of the event."""
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date

    def duration(self):
        """Calculate the duration of the event in days.
        Returns:
            int: The duration of the event in days."""
        durdays = (self.end_date - self.start_date).days
        return durdays

class conference(event):
    """A class representing a conference, inheriting from Event."""
    def __init__(self, name, location, start_date, end_date, attendees):
        """Initialize a Conference object with the specified attributes.
        Args:
            name (str): The name of the conference.
            location (str): The location of the conference.
            start_date (datetime): The start date and time of the conference.
            end_date (datetime): The end date and time of the conference.
            attendees (int): The number of attendees expected at the conference."""
        super().__init__(name, location, start_date, end_date)
        self.attendees = attendees

    def duration(self):
        """Calculate the duration of the conference in hours.
        Returns:
            float: The duration of the conference in hours."""
        durhrs = (self.end_date - self.start_date).total_seconds()/3600
        return durhrs

def main():
    """main function. instanciates event and conference. prints out the event and conference details."""
    event1 = event("Shindig", "CNA PPD Campus", datetime(2024, 3, 11), datetime(2024, 3, 12))
    conference1 = conference("Sales Conference", "SAP Center in San Jose", datetime(2023, 4, 27), datetime(2023, 4, 30), 259)

    print("Event:")
    print("Name:", event1.name)
    print("Location:", event1.location)
    print("Start Date:", event1.start_date)
    print("End Date:", event1.end_date)
    print("Duration (days):", event1.duration())
    print("\n")
    print("Conference:")
    print("Name:", conference1.name)
    print("Location:", conference1.location)
    print("Start Date:", conference1.start_date)
    print("End Date:", conference1.end_date)
    print("Attendees:", conference1.attendees)
    print("Duration (hours):", conference1.duration())

if __name__ == "__main__":
    main()

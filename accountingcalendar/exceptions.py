# 4_4_5_calendar/exceptions.py

class CalendarError(Exception):
    """Base exception for calendar errors."""
    pass

class FiscalCalendarCreationError(CalendarError):
    """Exception raised when invalid data is passed to FiscalCalendar."""
    def __init__(self, message):
        super().__init__(message)
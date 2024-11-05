from datetime import datetime, timedelta
from .exceptions import FiscalCalendarCreationError as _FiscalCalendarCreationError

class FiscalCalendar:
    def __init__(self, start_date, structure='445', is_53_week_year=False, extra_week_month=None):
        try:
            if isinstance(start_date, str):
                self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            elif isinstance(start_date, datetime):
                self.start_date = start_date.date()
            else:
                raise _FiscalCalendarCreationError(
                    "start_date must be a string in 'YYYY-MM-DD' format or a datetime object."
                )
        except ValueError as ve:
            raise _FiscalCalendarCreationError(f"Invalid date format for start_date: {ve}")
        
        try:
            if not is_53_week_year:
                self.extra_week_month = None
            elif is_53_week_year and extra_week_month is None:
                raise _FiscalCalendarCreationError(
                    "if is_53_week_year is set to true, the month containing the extra week must be specified as an integer"
                )
            elif extra_week_month is None:
                self.extra_week_month = extra_week_month
            elif isinstance(extra_week_month, str):
                raise _FiscalCalendarCreationError(
                    "if is_53_week_year is set to true, the month containing the extra week must be specified as an integer"
                )
            elif not 1 <= extra_week_month <= 12:
                raise _FiscalCalendarCreationError(
                    "extra_week_month must be an integer 1-12"
                )
            else:
                self.extra_week_month = extra_week_month
        except ValueError as ve:
            raise _FiscalCalendarCreationError(f"Invalid format for extra_week_month: {ve}")
    
    def _get_calendar_structure(self, structure: str, is_53_week_year, extra_week_month):
        if is_53_week_year:
            default_list = [4, 4, 5, 4, 4, 5, 4, 4, 5, 4, 4, 5]
        else:
            default_list = [4, 4, 5, 4, 4, 5, 4, 4, 5, 4, 4, 5]
        # Check if the input string has at least 3 characters
        if len(structure) < 3:
            print("Error: Input string must be at least 3 characters long.")
            return default_list
        try:
            # Convert each character to an integer
            s_digits = [int(ch) for ch in structure]
        except ValueError:
            print("Error: Input string must contain only digits.")
            return default_list
        # Calculate how many times to repeat the sequence to get at least 12 numbers
        repeat_count = -(-12 // len(s_digits))  # Ceiling division
        # Create the final list and truncate to 12 elements
        result_list = (s_digits * repeat_count)[:12]
        return result_list
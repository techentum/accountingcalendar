import sys
import os

# Get the parent directory and add it to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from accountingcalendar.calendar import FiscalCalendar

# Rest of your test code
calendar = FiscalCalendar("2024-01-01",is_53_week_year=True, extra_week_month=12)
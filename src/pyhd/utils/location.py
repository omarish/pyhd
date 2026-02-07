"""
Location utilities for geocoding and timezone lookup.
"""
from datetime import datetime
from typing import Optional, Tuple
from zoneinfo import ZoneInfo

from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder


def get_location_info(location_name: str) -> Tuple[float, float, str]:
    """
    Get latitude, longitude, and timezone for a given location name.
    
    Args:
        location_name: City/State string (e.g. "New York, NY")
        
    Returns:
        Tuple of (latitude, longitude, timezone_name)
    """
    geolocator = Nominatim(user_agent="pyhd")
    location = geolocator.geocode(location_name)
    
    if not location:
        raise ValueError(f"Could not find location: {location_name}")
        
    tf = TimezoneFinder()
    timezone_str = tf.timezone_at(lng=location.longitude, lat=location.latitude)
    
    if not timezone_str:
        raise ValueError(f"Could not determine timezone for: {location_name}")
        
    return location.latitude, location.longitude, timezone_str


def localize_datetime(dt_str: str, timezone_str: str) -> datetime:
    """
    Parse a datetime string and localize it to the given timezone.
    
    Args:
        dt_str: Date time string (e.g. "1987-04-12 14:00")
        timezone_str: Timezone name (e.g. "America/New_York")
        
    Returns:
        Timezone-aware datetime object
    """
    dt = datetime.fromisoformat(dt_str)
    if dt.tzinfo is not None:
        # If already aware, convert to target timezone
        return dt.astimezone(ZoneInfo(timezone_str))
    
    # If naive, assume it's in the target timezone
    return dt.replace(tzinfo=ZoneInfo(timezone_str))

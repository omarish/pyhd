#!/usr/bin/env python3
"""
Human Design Library: CLI entry point.
"""
import argparse
import sys
from datetime import UTC, datetime

from pyhd import Chart
from pyhd.utils.location import get_location_info, localize_datetime


def parse_datetime_utc(arg: str) -> datetime:
    """Parse the arg string into an aware datetime (defaulting to UTC)."""
    dt = datetime.fromisoformat(arg)
    dt = (dt.astimezone(UTC) if dt.tzinfo  # Aware => convert to UTC.
          else dt.replace(tzinfo=UTC))     # Naive => set as UTC.
    return dt


def parse_args():
    parser = argparse.ArgumentParser(description="PyHD – BodyGraph calculator.")
    parser.add_argument("birth_time", type=str,
        help="Birth date/time. Format: 'YYYY-MM-DD HH:MM[:SS][±HH:MM]'")
    parser.add_argument("-l", "--location", type=str,
        help="City/State for local time (e.g. 'New York, NY')")

    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    if args.location:
        try:
            lat, lon, timezone_str = get_location_info(args.location)
            print(f"Location: {args.location} ({lat:.4f}, {lon:.4f})")
            print(f"Timezone: {timezone_str}")
            
            dt = localize_datetime(args.birth_time, timezone_str)
            # Convert to UTC for the Chart class
            dt_utc = dt.astimezone(UTC)
            print(f"Local Time: {dt}")
            print(f"UTC Time:   {dt_utc}")
            print("-" * 40)
            
            chart = Chart(dt_utc)
        except Exception as e:
            print(f"Error processing location: {e}", file=sys.stderr)
            return 1
    else:
        # Default behavior: assume UTC or explicit offset in string
        dt_utc = parse_datetime_utc(args.birth_time)
        chart = Chart(dt_utc)

    chart.print()
    return 0


if __name__ == "__main__":
    sys.exit(main())

# PyHD

Python library for Human Design – BodyGraph calculations and analysis.

PyHD computes complete Human Design charts from birth date and time. It calculates planetary
activations for both the Personality (birth) and Design (88° solar arc before birth) imprints, and
derives all characteristics.

This library uses (a [Python extension](https://github.com/astrorigin/pyswisseph) to) the
[Swiss Ephemeris](https://www.astro.com/swisseph/) for high-precision planetary position
calculations.


## Installation

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

```bash
uv sync
```

## Usage

You can run the CLI using `uv run`:

```bash
uv run pyhd "1987-04-12 14:00"
```

You can also specify a location to use local time:

```bash
uv run pyhd "1987-04-12 14:00" --location "New York, NY"
```


## License

Distributed under the terms of the [MIT license][LICENSE], PyHD is free and open source software.

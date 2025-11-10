# Property Search Tool

Search UK properties for sale using the Zoopla UK API via RapidAPI.

## Setup

1. Install dependencies:
```bash
pip install requests
```

2. Get your API key:
   - Sign up at [RapidAPI](https://rapidapi.com/)
   - Subscribe to [Zoopla UK API](https://rapidapi.com/vibapidev/api/zoopla-uk)

3. Update `search.py` with your API key

## Usage

```bash
python search.py
```

Customize the search location in `search.py`:
```python
params={"query": "Your Location"}  # e.g., "London", "SW7 2AZ"
```

## Example Output

```
dict_keys(['listing_id', 'title', 'price', 'address', 'bedrooms', ...])
{'display_address': '123 Example Street, South Kensington, London SW7'}
```

## License

Licensed under the terms in the LICENSE file. For educational and personal use only.
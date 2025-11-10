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
dict_keys(['address', 'agent', 'attributes', 'flag', 'highlights', 'imageUris', 'isExpired', 'isFeatured', 'isPremium', 'listingId', 'location', 'pricing', 'shortPriceTitle', 'publicationStatus', 'tags', 'title'])
Onslow Mews West, Kensington SW7
```

## License

Licensed under the terms in the LICENSE file. For educational and personal use only.
import tweepy

# Reemplaza estos valores con tus credenciales
API_KEY = 'QQoMOWLb4DevY9hl9ahbxUjjl'
API_SECRET_KEY = '1lK2MQS2GFWQrdasoX3oeUanqzFUZWHWmbZJbYQHLlXGZNWdxY'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAF4WvgEAAAAAyRtmIlLf2TBkKGpc0kq%2FUwc90v8%3DNb7tRTAM651WIttEZOdqxgkFWMkEto2g3s2G1bqAVPMRQRUVYA'

# Autentica con la API de Twitter
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def get_place_id(place_name):
    """Obtiene el ID de un lugar por nombre."""
    response = client.search_geo(query=place_name)
    if response.data:
        return response.data[0]['id']
    return None

def get_tweets_by_location(query, place_id, max_results=10):
    """Obtiene tweets geolocalizados por ID de lugar."""
    tweets = client.search_recent_tweets(
        query=query,
        place_id=place_id,
        max_results=max_results,
        tweet_fields=['geo']
    )
    return tweets.data if tweets.data else []

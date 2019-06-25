import oauth2 as oauth
#import urllib2 as urllib
import urllib.request as urllib

# See assignment1.html instructions or README for how to get these credentials

api_key = "3Rk6zVTw0GtB12WIOaUNMKZHm"
api_secret = "Rm9tXMXOLUNJu6JV1acmGW4xkuLVO9Oa3ITErDd2W7TfAEuO2m"
access_token_key = "2609984694-1hRmhVf3ih7KWFtuUIgMe1ZdWgXQy1qLnqgHdVy"
access_token_secret = "OCqLw4zULqjh8tX79HE1BehOVClrkgN5DHXpsQQmlCxdy"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

print("This is oauth token",oauth_token)
print("This is oauth comsumer",oauth_consumer)
print('**'*20)
signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response
  
def get_url_data(url_link,uid,upassword):
    """
    Pass Input as a html url link and get html data
    @@ function takes input as url and return content of that file.
    """
    prin_px = "https://" + uid + ":" + upassword + "@pfgproxy.principal.com:80"
    r = requests.get(url_link, proxies={"https":prin_px})
    #content = r.content.lower()
    content = r.content
    return content
  
def fetchsamples():
  url = "https://stream.twitter.com/1/statuses/sample.json"
  prin_px = "https://" + "J554696" + ":" + "Sep@2018" + "@pfgproxy.principal.com:80"
  parameters = {"https":prin_px}
  response = twitterreq(url, "GET", parameters)
  for line in response:
    print (line.strip())

if __name__ == '__main__':
  fetchsamples()
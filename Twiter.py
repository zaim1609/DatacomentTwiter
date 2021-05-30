import tweepy

api_key = "odr6el7syIv3wInsXLnMsz7Mu"
api_secret_key = "zGCAfN5Votc2TAbxx5jhe643t0ILo5gTIPiexLIKCmKhbxkSuq"
acces_token = "1365568208103645185-hKtFucgQrTqzXz7KprWhfriknW2tdr"
acces_token_secret = "SuEy39CTOPqgZIM5gPXHDhZ8b8mq28swRlMedqmBRM2KU"

auth  = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(acces_token, acces_token_secret)
api = tweepy.API(auth)

hasilUser = api.user_timeline(id = "ernestprakasa", count = 10)
hasilSearch = api.search(q = "jakarta", lang = "id", count = 10)

for tweet in hasilUser:
    # print(tweet.text)
    print(tweet.user.screen_name, "Ngetwit: ", tweet.text)
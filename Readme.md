## Comment ça marche

#### 1 Créer un compte Twitter développeur 

Lien vers la doc de twitter : https://developer.twitter.com/en/dashboard

#### 2 Créer une Apps        
Lien vers la section "Apps" : https://developer.twitter.com/en/apps
Créer une API key, et un token de connexion, noter : 

* API key
* API secret key
* Access token
* Access token secret


#### 3 cloner le projet 

```$ git clone git@github.com:Fabinout/TweetDeleter.git```

#### 4 Install tweepy


[Tweepy](https://github.com/tweepy/tweepy) est la librairie python qui wrap l'api Twitter la plus populaire

```pip install tweepy```

#### 5 Saisir ses moyens d'autentification

Dans le fichier ./[delete_old_tweets.py](delete_old_tweets.py), saisir les identifiants (API key,API secret key,Access token, Access token secret)
dans le dictionnaire 'authent_dict'.

#### 6 Démarrer le programme !

```$ python main.py```


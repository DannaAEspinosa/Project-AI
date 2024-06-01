import pickle
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

#This class helps to classify the genre of a song and conects to the Spotify API
class ClassifierGenre():

    #init method that loads the models and the scaler. Also it starts the connection to the Spotify API 
    def __init__(self):
        self.scaler = pickle.load(open('scaler.pkl', 'rb'))
        self.pca = pickle.load(open('pca.pkl', 'rb'))
        self.decision_tree = pickle.load(open('decision_tree.pkl', 'rb'))
        self.logistic_regression = pickle.load(open('logistic_reg.pkl', 'rb'))
        self.sp = self.start_conection()
    
    #Method that starts the connection to the Spotify API
    def start_conection(self):
        client_id="71e4f66d655b4d17a2f44adf768f4d8e"
        client_secret="bc3ac533973740a9ab4aca024a1da9c4"
        auth_manager = SpotifyClientCredentials(client_id, client_secret)
        sp = spotipy.Spotify(auth_manager=auth_manager)   
        return sp

    #Method that tests the connection to the Spotify API
    def test_spotify_connection(self):
        try:
            results = self.sp.search(q='Adele', limit=1, type='artist')
            if results['artists']['items']:
                print("Conexión exitosa a Spotify API!")
                print("Nombre del artista:", results['artists']['items'][0]['name'])
            else:
                print("Conexión establecida, pero no se encontraron resultados.")
        except Exception as e:
            print("Error al conectar con Spotify API:", e)

    #Method that gets the features of a song
    def get_features(self,name_song):
        try:
            results = self.sp.search(q=name_song, limit=1, type='track')
            if results['tracks']['items']:
                track_id =  results['tracks']['items'][0]['id']
                features = self.sp.audio_features(track_id)[0]
                desired_columns = [
                'acousticness', 'danceability', 'energy', 'instrumentalness',
                'liveness', 'speechiness', 'tempo', 'valence']
                features_df = pd.DataFrame([features])[desired_columns]
                #values_feature = features_df.values
                #print(values_array)
                return features_df
            else:
                return None
        except Exception as e:
            print("Error al buscar la canción:", e)

    #Method that processes the data. Aply the scaler and the pca
    def process_data(self,features):
        features = self.scaler.transform(features)
        features = self.pca.transform(features)
        return features
    
    #Method that predicts the genre of a song using the decision tree model
    def tree_predict(self,features):
        prediction = self.decision_tree.predict(features)
        probabilities = self.decision_tree.predict_proba(features)
        return prediction, probabilities
    
    #Method that predicts the genre of a song using the logistic regression model
    def logistic_predict(self,features):
        prediction = self.logistic_regression.predict(features)
        probabilities = self.logistic_regression.predict_proba(features)
        return prediction, probabilities

'''
if __name__ == '__main__':
    print("Hola mundo")
    classifier = ClassifierGenre()
    features = classifier.get_features("Hundred-Year Flood")
    datas = classifier.process_data(features)
    prediction_tree,proba_tree = classifier.tree_predict(datas)
    prediction_logis,proba_reg = classifier.logistic_predict(datas)

    print(prediction_tree + " " + str(proba_tree))
    print(prediction_logis + " " + str(proba_reg))
'''

    
    


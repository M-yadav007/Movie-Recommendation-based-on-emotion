from flask import Flask, render_template, request
import cv2
from deepface import DeepFace
import time
import requests
from bs4 import BeautifulSoup
import regex as re

app = Flask(__name__)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video_duration = 5  # in seconds

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze_emotion', methods=['POST'])
def analyze_emotion():
    emotions = []

    cap = cv2.VideoCapture(0)
    start_time = time.time()

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
            face_img = frame[y:y+h, x:x+w]
            
            _, img_encoded = cv2.imencode('.jpg', face_img)
            img_bytes = img_encoded.tobytes()
            img_path = 'temp.jpg'
            with open(img_path, 'wb') as f:
                f.write(img_bytes)
            
            result = DeepFace.analyze(img_path=img_path, actions=['emotion'], enforce_detection=False)

            dominant_emotion =(result[0]["dominant_emotion"][:])
            emotions.append(dominant_emotion)

            txt = "Emotion: " + dominant_emotion

            cv2.putText(frame, txt, (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        cv2.imshow('frame', frame)

        if time.time() - start_time >= video_duration:
            break

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    most_common_emotion = max(set(emotions), key=emotions.count)

    movie_data = fetch_movies_from_imdb(most_common_emotion)

    return render_template('result.html', emotion=most_common_emotion, movies=movie_data)

def fetch_movies_from_imdb(emotion):
    genre_mapping = {
        'sad': 'drama',
        'disgust': 'musical',
        'angry': 'family',
        'neutral': 'thriller',
        'fear': 'sport',
        'happy': 'thriller',
        'surprised': 'film_noir'
    }

    genre = genre_mapping.get(emotion)

    if genre:
        url = f'http://www.imdb.com/search/title?genres={genre}&title_type=feature&sort=moviemeter, asc'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        movie_titles = soup.find_all('h3', class_='lister-item-header')
        movie_ratings = soup.find_all('div', class_='inline-block ratings-imdb-rating')
        movie_image = soup.find_all("img", {"class": "loadlate"})

        movie_data = []
        # for title, rating,image, in zip(movie_titles, movie_ratings,movie_image):
        #     movie_data.append({'title': title.text.strip(), 'rating': rating.text.strip(),'image':image.text.strip()})

        
    for i in range(0, 10):
        title = movie_titles[i].text
        rating = movie_ratings[i].text
        images = movie_image[i]['loadlate']
        names=movie_image[i]['loadlate']
        movie_data.append({'title': title, 'rating': rating, 'image_url': images})
    return movie_data
        # return movie_data

    return []

if __name__ == '__main__':
    app.run()

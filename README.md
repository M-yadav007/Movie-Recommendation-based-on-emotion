# Movie-Recommendation-based-on-emotion




## Overview
The Movie Recommendation Based on Emotion project aims to develop a personalized movie recommendation system that suggests movies to users based on their emotions. By leveraging web scraping techniques, sentiment analysis, and emotion recognition, the system provides movie recommendations that align with the user's current emotional state or desired emotional experience.

## Features
- Web scraping: Gather movie data from various online sources such as movie databases, review sites, or streaming platforms using web scraping techniques.
- Sentiment Analysis: Utilize IBM Watson APIs or other sentiment analysis techniques to analyze the emotional content of movie data.
- Emotion Recognition: Employ the DeepFace model or other deep learning models to detect emotions from facial expressions in images or videos.
- Recommendation Algorithm: Create a recommendation algorithm that matches user emotions with the emotional content of movies to generate personalized recommendations.
- Flask Web Application: Build a web application using Flask to provide a user-friendly interface for users to interact with the recommendation system.
- HTML and CSS: Design an intuitive and visually appealing webpage to display movie recommendations and other relevant information.

## Installation
1. Clone the repository: `git clone https://github.com/M-yadav007/Move-Recommendation-based-on-emotion.git`
2. Install the required dependencies: `pip install -r requirements.txt`

## Usage
1. Run the Flask web application: `python app.py`
2. Access the web application through your browser at: `http://localhost:5000`

## Experimental Investigations
During the development of this project, we encountered several challenges, including:
- Ensuring the accuracy of the emotion recognition model: Fine-tuning the DeepFace model or exploring other pre-trained models to improve the accuracy of emotion recognition.
- Integrating the emotion recognition model with the Flask application: Linking the emotion recognition model to the Flask application and passing the detected emotions to the recommendation algorithm.
- Displaying the results on the HTML webpage: Designing the webpage layout using HTML and CSS to showcase the recommended movies and their emotional relevance to the user.

## Future Scope
- Enhance emotion recognition: Explore advanced deep learning models and techniques to improve the accuracy and robustness of emotion recognition.
- Incorporate user feedback: Implement a feedback mechanism where users can rate the recommended movies and provide feedback to further personalize the recommendations.
- Collaborative filtering: Integrate collaborative filtering techniques to consider the preferences and emotions of similar users when generating recommendations.
- Mobile application development: Extend the project to develop a mobile application for users to access movie recommendations on their smartphones.

## License
This project is licensed under the [MIT License](https://github.com/M-yadav007/Movie-Recommendation-based-on-emotion/blob/main/LICENSE).



## Acknowledgments
We would like to express our gratitude to our project supervisor for their guidance and support throughout the development process. We also extend our thanks to the developers of the various technologies and frameworks used in this project, as well as the online communities and open-source contributors for their valuable resources and assistance. Lastly, we acknowledge the dataset providers and researchers in the field of emotion recognition for their valuable contributions.

## Contact
For any inquiries or feedback, please contact us at [mayank.yad2004@gmail.com].

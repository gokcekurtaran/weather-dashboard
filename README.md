# 🌦️ Weather Dashboard
A modern weather dashboard developed with **Django** and **OpenWeather API**. 
The application allows users to search for any city and view real-time weather information through a clean and responsive interface.

## 🚀 Feature
- 🌍 Search weather by city name
- 🌡️ Display current temperature
- 💧 Show humidity level
- 🌬️ Display wind speed
- ☁️ Weather condition and description
- 🎨 Clean and responsive user interface
- ⚡ Real-time weather data using OpenWeather API
- ❌ Error handling for invalid city names
- 
## 🛠️ Technologies Used
- Python
- Django
- HTML5
- CSS3
- OpenWeather API
- Requests Library

## 📁 Project Structure
weather_project/
│
├── weather/
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── ...
│
├── weather_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py
└── requirements.txt

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/weather-dashboard.git
```

Navigate into the project:

```bash
cd weather-dashboard
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the development server:

```bash
python manage.py runserver
```

Open your browser:

```
http://127.0.0.1:8000/
```

## 🔑 API
This project uses the **OpenWeather API** to retrieve real-time weather information.

Create an API key from:
https://openweathermap.org/api
Add your API key inside the project configuration before running the application.

## 📌 Future Improvements
- 5-day weather forecast
- Weather icons
- Favorite cities
- Dark mode
- Geolocation support
- Temperature unit conversion (°C / °F)


## 👨‍💻 Author
Developed by **Gökçe Kurtaran** as part of software development and Django practice projects.

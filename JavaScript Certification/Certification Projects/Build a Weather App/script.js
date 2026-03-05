const getWeatherBtn = document.getElementById("get-weather-btn");
const citySelect = document.querySelector("select");
const weatherIcon = document.getElementById("weather-icon");
const mainTemperature = document.getElementById("main-temperature");
const feelsLike = document.getElementById("feels-like");
const humidity = document.getElementById("humidity");
const wind = document.getElementById("wind");
const windGust = document.getElementById("wind-gust");
const weatherMain = document.getElementById("weather-main");
const locationEl = document.getElementById("location");
const weatherInfo = document.getElementById("weather-info");

async function getWeather(city) {
  try {
    const res = await fetch(
      `https://weather-proxy.freecodecamp.rocks/api/city/${city}`,
    );

    if (!res.ok) throw new Error("Request failed");

    const data = await res.json();
    return data;
  } catch (err) {
    console.error(err);
    return null;
  }
}

async function showWeather(city) {
  const data = await getWeather(city);

  if (!data) {
    alert("Something went wrong, please try again later");
    return;
  }

  const weather = data.weather?.[0] || {};
  const main = data.main || {};
  const windData = data.wind || {};

  weatherIcon.src = weather.icon || "";
  weatherIcon.alt = weather.description || "weather icon";

  mainTemperature.textContent =
    main.temp !== undefined ? `${main.temp} °C` : "N/A";

  feelsLike.textContent =
    main.feels_like !== undefined ? `${main.feels_like} °C` : "N/A";

  humidity.textContent =
    main.humidity !== undefined ? `${main.humidity}%` : "N/A";

  wind.textContent =
    windData.speed !== undefined ? `${windData.speed} m/s` : "N/A";

  windGust.textContent =
    windData.gust !== undefined ? `${windData.gust} m/s` : "N/A";

  weatherMain.textContent = weather.main || "N/A";

  locationEl.textContent = data.name || "N/A";

  weatherInfo.style.display = "flex";
}

getWeatherBtn.addEventListener("click", () => {
  const city = citySelect.value;

  if (!city) return;

  showWeather(city);
});

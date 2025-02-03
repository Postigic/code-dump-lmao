let timeFormat = "12-hour";
let showSeconds = true;
let dateFormat = "long";
let dayFormat = "long";

function updateClock() {
    const clockElement = document.getElementById("clock");
    const timeElement = document.getElementById("date");

    const now = new Date();

    let hours = now.getHours().toString().padStart(2, "0");
    const minutes = now.getMinutes().toString().padStart(2, "0");
    const seconds = now.getSeconds().toString().padStart(2, "0");

    let meridiem = "";

    if (timeFormat === "12-hour") {
        meridiem = hours >= 12 ? "PM" : "AM";
        hours = hours % 12 || 12;
    }

    const weekdayOption =
        dayFormat === "none"
            ? undefined
            : dayFormat === "long"
            ? "long"
            : "short";

    const timeString = `${hours}:${minutes}${
        showSeconds ? `:${seconds}` : ""
    } ${meridiem}`;
    let dateString = now.toLocaleDateString("en-SG", {
        weekday: weekdayOption,
        day: dateFormat === "long" ? "numeric" : "2-digit",
        month: dateFormat === "long" ? "long" : "2-digit",
        year: "numeric",
    });

    clockElement.textContent = timeString;
    timeElement.textContent = dateString;
}

updateClock();
setInterval(updateClock, 100);

const settingsButton = document.getElementById("settings-btn");
const settingsMenu = document.getElementById("settings-menu");
const closeSettingsButton = document.getElementById("close-settings");
const timeFormatSelect = document.getElementById("time-format");
const showSecondsSelect = document.getElementById("show-seconds");
const dateFormatSelect = document.getElementById("date-format");
const dayFormatSelect = document.getElementById("day-format");

settingsButton.addEventListener("click", () => {
    settingsButton.style.opacity = "0";
    settingsMenu.style.bottom = "0";
});

closeSettingsButton.addEventListener("click", () => {
    settingsButton.style.opacity = "1";
    settingsMenu.style.bottom = "-100%";
});

timeFormatSelect.addEventListener("change", () => {
    timeFormat = timeFormatSelect.value;
    updateClock();
});

showSecondsSelect.addEventListener("change", () => {
    showSeconds = showSecondsSelect.value === "true";
    updateClock();
});

dateFormatSelect.addEventListener("change", () => {
    dateFormat = dateFormatSelect.value;
    updateClock();
});

dayFormatSelect.addEventListener("change", () => {
    dayFormat = dayFormatSelect.value;
    updateClock();
});

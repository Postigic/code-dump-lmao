const lengthSlider = document.querySelector(".password-length input");
const options = document.querySelectorAll(".option input");
const copyIcon = document.querySelector(".input-box span");
const passwordInput = document.querySelector(".input-box input");
const passwordIndicator = document.querySelector(".password-indicator");
const generateBtn = document.querySelector(".generate-btn");

const characters = {
    lowercase: "abcdefghijklmnopqrstuvwxyz",
    uppercase: "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    numbers: "0123456789",
    symbols: "!@#$%^&*()[]{}|:;.,+-<>~",
};

const generatePassword = () => {
    let staticPassword = "",
        randomPassword = "",
        excludeDuplicate = false,
        passwordLength = lengthSlider.value;

    options.forEach((option) => {
        if (option.checked) {
            if (option.id !== "exc-duplicate" && option.id !== "spaces") {
                staticPassword += characters[option.id];
            } else if (option.id === "spaces") {
                staticPassword += `  ${staticPassword}  `;
            } else {
                excludeDuplicate = true;
            }
        }
    });

    if (excludeDuplicate && passwordLength > staticPassword.length) {
        lengthSlider.value = 15;
        updateSlider();
        return;
    }

    for (let i = 0; i < passwordLength; i++) {
        let randomChar =
            staticPassword[Math.floor(Math.random() * staticPassword.length)];
        if (excludeDuplicate) {
            !randomPassword.includes(randomChar) || randomChar == " "
                ? (randomPassword += randomChar)
                : i--;
        } else {
            randomPassword += randomChar;
        }
    }
    passwordInput.value = randomPassword;
};

const updatePasswordIndicator = () => {
    passwordIndicator.id =
        lengthSlider.value <= 8
            ? "weak"
            : lengthSlider.value <= 16
            ? "medium"
            : "strong";
};

const updateSlider = () => {
    document.querySelector(".password-length span").innerText =
        lengthSlider.value;
    generatePassword();
    updatePasswordIndicator();
};
updateSlider();

const copyPassword = () => {
    navigator.clipboard.writeText(passwordInput.value);
    copyIcon.innerText = "check";
    copyIcon.style.color = "#4285F4";
    setTimeout(() => {
        copyIcon.innerText = "copy_all";
        copyIcon.style.color = "#707070";
    }, 1500);
};

copyIcon.addEventListener("click", copyPassword);
lengthSlider.addEventListener("input", updateSlider);
generateBtn.addEventListener("click", generatePassword);

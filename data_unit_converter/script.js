const dataInput = document.getElementById("data-size");
const initialInput = document.getElementById("initial-unit");
const conversionInput = document.getElementById("conversion-unit");
const convertBtn = document.querySelector(".convert-btn");
const result = document.querySelector("#result input");
const bitResult = document.querySelector("#bits-result input");
const resultCopyIcon = document.querySelector("#result span");
const bitResultCopyIcon = document.querySelector("#bits-result span");

const units = {
    B: 1,
    KB: 1000,
    KIB: 1024,
    MB: 1000 ** 2,
    MIB: 1024 ** 2,
    GB: 1000 ** 3,
    GIB: 1024 ** 3,
    TB: 1000 ** 4,
    TIB: 1024 ** 4,
    PB: 1000 ** 5,
    PIB: 1024 ** 5,
};

const convertUnit = () => {
    const dataSize = Number(dataInput.value);
    const initialUnit = initialInput.value.trim().toUpperCase();
    const conversionUnit = conversionInput.value.trim().toUpperCase();

    if (dataSize < 0 || isNaN(dataSize)) {
        dataSize = 0;
        dataInput.value = 0;
    }
    if (!units.hasOwnProperty(initialUnit)) {
        initialInput.value = "Invalid initial unit!";
    }
    if (!units.hasOwnProperty(conversionUnit)) {
        conversionInput.value = "Invalid conversion unit!";
        return;
    }

    const conversionResult =
        (dataSize * units[initialUnit]) / units[conversionUnit];
    const bitsResult = ((dataSize * units[initialUnit]) / units["B"]) * 8;

    result.value = conversionResult;
    bitResult.value = bitsResult;
};

const copyResult = (result, icon) => {
    navigator.clipboard.writeText(result.value);
    icon.innerText = "check";
    icon.style.color = "#4285F4";
    setTimeout(() => {
        icon.innerText = "copy_all";
        icon.style.color = "#707070";
    }, 1500);
};

convertBtn.addEventListener("click", convertUnit);
resultCopyIcon.addEventListener("click", () =>
    copyResult(result, resultCopyIcon)
);
bitResultCopyIcon.addEventListener("click", () =>
    copyResult(bitResult, bitResultCopyIcon)
);

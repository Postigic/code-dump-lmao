function calculate() {
    const principalInput = document.getElementById("principal");
    const rateInput = document.getElementById("rate");
    const yearsInput = document.getElementById("years");
    const totalAmount = document.getElementById("total-amount");

    let principal = Number(principalInput.value);
    let rate = Number(rateInput.value / 100);
    let years = Number(yearsInput.value);

    // Error handling
    if (principal < 0 || isNaN(principal)) {
        principal = 0;
        principalInput.value = 0;
    }
    if (rate < 0 || isNaN(rate)) {
        rate = 0;
        rateInput.value = 0;
    }
    if (years < 0 || isNaN(years)) {
        years = 0;
        yearsInput.value = 0;
    }

    // Calculate interest
    const result = principal * Math.pow(1 + rate / 1, 1 * years);

    // Update total
    totalAmount.textContent = result.toLocaleString(undefined, {
        style: "currency",
        currency: "USD",
    });
}

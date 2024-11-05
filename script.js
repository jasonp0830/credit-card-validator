function validateCard() {
    const cardNumber = document.getElementById('cardNumber').value;
    const networkInfo = document.getElementById('networkInfo');
    const validationResult = document.getElementById('validationResult');

    // Reset output
    networkInfo.innerHTML = ""; // Use innerHTML to insert HTML content
    validationResult.textContent = "";

    if (!/^\d{13,16}$/.test(cardNumber)) {
        validationResult.textContent = "Please enter a valid credit card with 13, 15, or 16 digits.";
        return;
    }

    const network = detectNetwork(cardNumber);
    const networkIcon = getNetworkIcon(network);

    if (networkIcon) {
        networkInfo.innerHTML = `Type of Payment Network: ${network} <img src="${networkIcon}" alt="${network} logo" style="width: 30px; height: 20px; vertical-align: middle; margin-left: 5px;">`;
    } else {
        networkInfo.textContent = `Type of Payment Network: ${network}`;
    }

    if (luhnCheck(cardNumber)) {
        validationResult.textContent = "This card is Valid! It passed the Luhn test.";
    } else {
        validationResult.textContent = "This card is not Valid.";
        networkInfo.textContent = "Type of Payment Network: Invalid";
    }
}

function detectNetwork(cardNumber) {
    if (cardNumber.startsWith("4")) return "Visa";
    if (cardNumber.startsWith("5")) return "MasterCard";
    if (cardNumber.startsWith("34") || cardNumber.startsWith("37")) return "American Express";
    if (cardNumber.startsWith("6011")) return "Discover";
    return "Other";
}

function getNetworkIcon(network) {
    switch (network) {
        case "Visa":
            return "visa.png";
        case "MasterCard":
            return "mastercard.png";
        case "American Express":
            return "amex.png";
        case "Discover":
            return "discover.png";
        default:
            return null; // No icon for "Other"
    }
}

function luhnCheck(cardNumber) {
    let sum = 0;
    let shouldDouble = false;

    for (let i = cardNumber.length - 1; i >= 0; i--) {
        let digit = parseInt(cardNumber[i]);

        if (shouldDouble) {
            digit *= 2;
            if (digit > 9) digit -= 9;
        }

        sum += digit;
        shouldDouble = !shouldDouble;
    }

    return sum % 10 === 0;
}
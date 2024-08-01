(function () {
    var preTag = document.getElementById("donut");

    // Angles
    var angleA = 1;
    var angleB = 1;
    // Settings
    const rotationIncrementA = 0.07;
    const rotationIncrementB = 0.03;
    const frameInterval = 50;

    // Function to render ASCII frame
    function renderASCIIFrame() {
        var asciiChars = []; // Array to store ASCII chars
        var depthValues = []; // Array to store depth values

        var width = 280; // Width of frame
        var height = 160; // Height of frame

        angleA += rotationIncrementA; // Increment angle A
        angleB += rotationIncrementB; // Increment angle B
        // Sine and Cosine of angles
        var cosAngleA = Math.cos(angleA),
            sinAngleA = Math.sin(angleA),
            cosAngleB = Math.cos(angleB),
            sinAngleB = Math.sin(angleB);

        // Initialise arrays with default angles
        for (var index = 0; index < width * height; index++) {
            // Set default ASCII character
            asciiChars[index] = index % width == width - 1 ? "\n" : " ";
            // Set default depth
            depthValues[index] = 0;
        }

        // Generate the ASCII frame
        for (var j = 0; j < 6.28; j += 0.07) {
            var cosTheta = Math.cos(j); // Cosine of j
            var sinTheta = Math.sin(j); // Sine of j

            for (var i = 0; i < 6.28; i += 0.02) {
                var sinPhi = Math.sin(i); // Sine of i
                (cosPhi = Math.cos(i)), // Cosine of i
                    (h = cosTheta + 2), // Height calculation
                    // Distance calculation
                    (D =
                        1 /
                        (sinPhi * h * sinAngleA + sinTheta * cosAngleA + 5)),
                    // Temporary variable
                    (t = sinPhi * h * cosAngleA - sinTheta * sinAngleA);

                // Calculate coordinates of ASCII characters
                var x = Math.floor(
                    width / 2 +
                        (width / 4) *
                            D *
                            (cosPhi * h * cosAngleB - t * sinAngleB)
                );
                var y = Math.floor(
                    height / 2 +
                        (height / 4) *
                            D *
                            (cosPhi * h * sinAngleB + t * cosAngleB)
                );

                // Calculate the index in the array
                var o = x + width * y;
                // Calculate the ASCII character index
                var N = Math.floor(
                    8 *
                        ((sinTheta * sinAngleA -
                            sinPhi * cosTheta * cosAngleA) *
                            cosAngleB -
                            sinPhi * cosTheta * sinAngleA -
                            sinTheta * cosAngleA -
                            cosPhi * cosTheta * sinAngleB)
                );

                // Update ASCII characters and depth if conditions are met
                if (
                    y < height &&
                    y >= 0 &&
                    x >= 0 &&
                    x < width &&
                    D > depthValues[o]
                ) {
                    depthValues[o] = D;
                    // Update ASCII characters based on the index
                    asciiChars[o] = ".,-~:;=!*#$@"[N > 0 ? N : 0];
                }
            }
        }

        // Update HTML element with the ASCII frame
        preTag.innerHTML = asciiChars.join("");
    }

    // Function to start the animation
    function startASCIIAnimation() {
        // Start it by calling renderASCIIFrame every 50ms
        window.asciiIntervalID = setInterval(renderASCIIFrame, frameInterval);
    }

    renderASCIIFrame(); // Render the initial ASCII frame
    // Add event listener to start animation when page is loaded
    if (document.all) {
        // For older versions of Internet Explorer
        window.attachEvent("onload", startASCIIAnimation);
    } else {
        // For modern browsers
        window.addEventListener("load", startASCIIAnimation, false);
    }

    // Add event listener to update ASCII frame when window resizes
    window.addEventListener("resize", renderASCIIFrame);
})();

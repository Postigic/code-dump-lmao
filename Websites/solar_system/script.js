for (let i = 0; i < 200; i++) {
    const star = document.createElement("div");
    star.style.cssText = `
        position: absolute;
        z-index: -1;
        width: ${Math.random() * 3}px;
        height: ${Math.random() * 3}px;
        background: rgba(255, 255, 255, ${Math.random()});
        left: ${Math.random() * 100}%;
        top: ${Math.random() * 100}%;
        border-radius: 50%;
    `;
    document.body.appendChild(star);
}

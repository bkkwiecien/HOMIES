const eye1 = document.getElementById('eye1')
const rekt1 = eye1.getBoundingClientRect();
const eye1X = rekt1.left + rekt1.width / 2;
const eye1Y = rekt1.top + rekt1.height / 2;

const eye2 = document.getElementById('eye2')
const rekt2 = eye2.getBoundingClientRect();
const eye2X = rekt2.left + rekt2.width / 2;
const eye2Y = rekt2.top + rekt2.height / 2;

document.addEventListener('mousemove', (e) => {

    const mouseX = e.clientX;
    const mouseY = e.clientY;

    const angleDeg1 = angle(mouseX, mouseY, eye1X, eye1Y);
    const angleDeg2 = angle(mouseX, mouseY, eye2X, eye2Y);

    const eye1Loc = document.getElementById('eye1')
    const eye2Loc = document.getElementById('eye2')

    eye1Loc.style.transform = `rotate(${224 + angleDeg1}deg)`;
    eye2Loc.style.transform = `rotate(${224 + angleDeg2}deg)`;

})

function angle(cx, cy, ex, ey) {
    const dy = ey - cy;
    const dx = ex - cx;
    const rad = Math.atan2(dy, dx);
    const deg = rad * 180 / Math.PI;
    return deg;
}
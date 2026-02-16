function openNav() {
    if (document.getElementById('navegation').style.display == 'none') {
        document.getElementById('navegation').style.display = 'flex';
    } else {
        document.getElementById('navegation').style.display = 'none'
    };
}

function openOverlay(id) {
    document.getElementById(id).style.display = "flex";
}

function closeOverlay(id) {
    document.getElementById(id).style.display = "none";
}

function openOverlayClass(cl) {
    document.querySelector(`.${cl}`).style.display = "flex";
}

document.addEventListener("DOMContentLoaded", () => {
    const inputs = document.querySelectorAll(".current-date-input");
    const today = new Date().toISOString().split("T")[0];

    inputs.forEach(input => {
        input.value = today
    });
})
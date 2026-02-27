const weeklyCheckbox = document.getElementById("weekly-checkbox")
const weeklyOptions = document.getElementById("tasks-checkboxes-repeat-options")
weeklyCheckbox.addEventListener("change", function() {
    if (weeklyCheckbox.checked) {
        weeklyOptions.style.display = "flex"
    }
    else {
        weeklyOptions.style.display = "none"
    }
    
})
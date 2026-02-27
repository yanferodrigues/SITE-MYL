const allowTimeCheckbox = document.getElementById("allow-time-checkbox")
const setTime = document.querySelector(".task-overlay-content-time")

const repeatCheckbox = document.getElementById("repeat-checkbox")
const repeatOptions = document.querySelector(".tasks-checkboxes-repeat")

const weeklyCheckbox = document.getElementById("weekly-checkbox")
const weeklyOptions = document.querySelector(".tasks-checkboxes-repeat-options")

const monthlyCheckbox = document.getElementById("monthly-checkbox")

const yearlyCheckbox = document.getElementById("yearly-checkbox")


weeklyCheckbox.addEventListener("change", function() {
    if (weeklyCheckbox.checked) {
        weeklyOptions.style.display = "flex"
        monthlyCheckbox.checked = false
        yearlyCheckbox.checked = false
    }
    else {
        weeklyOptions.style.display = "none"
    }
    
})
monthlyCheckbox.addEventListener("change", function() {
    if (monthlyCheckbox.checked) {
        weeklyCheckbox.checked = false
        yearlyCheckbox.checked = false
        weeklyOptions.style.display = "none"
    }
})
yearlyCheckbox.addEventListener("change", function() {
    if (yearlyCheckbox.checked) {
        weeklyCheckbox.checked = false
        monthlyCheckbox.checked = false
        weeklyOptions.style.display = "none"
    }
})

repeatCheckbox.addEventListener("change", function() {
    if (repeatCheckbox.checked) {
        repeatOptions.style.display = "flex"
    }
    else {
        repeatOptions.style.display = "none"
    }
    
})

allowTimeCheckbox.addEventListener("change", function() {
    if (allowTimeCheckbox.checked) {
        setTime.style.display = "flex"
    }
    else {
        setTime.style.display = "none"
    }
    
})
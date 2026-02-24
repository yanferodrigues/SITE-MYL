function addGymRowByButton(button) {
    const row = button.closest(".overlay-container-content-gym-exercises");
    const form = row.closest(".overlay-container-content-gym-form");
    const container = form.querySelector(".gymExercisesContainer");

    const newRow = row.cloneNode(true);

    newRow.querySelectorAll("input").forEach(input => {
        input.value = "";
    });

    container.insertBefore(newRow, row.nextSibling);
}

function removeGymRowByButton(button) {
    const row = button.closest(".overlay-container-content-gym-exercises");
    const form = row.closest(".overlay-container-content-gym-form");
    const container = form.querySelector(".gymExercisesContainer");

    if (container.children.length > 1) {
        row.remove();
    }
    else {
        row.querySelectorAll("input").forEach(input => {
            input.value = "";
        })
    }
}

function addNewForm() {
    const container = document.getElementById("overlay-gym-general-forms");
    const form = container.querySelector(".overlay-container-content-gym-form");
    const newForm = form.cloneNode(true);
    const exercisesRows = newForm.querySelector(".gymExercisesContainer")

    while (exercisesRows.children.length > 1) {
        exercisesRows.lastElementChild.remove()
    }

    newForm.querySelectorAll("input").forEach(input => {
        input.value = "";
    });

    container.appendChild(newForm)
}

function removeForm(button) {
    const container = document.getElementById("overlay-gym-general-forms");
    const form = button.closest(".overlay-container-content-gym-form");
    if (container.children.length > 1) {
        form.remove();
    }
    else {
        form.querySelectorAll("input").forEach(input => {
            input.value = "";
        })
    }
    
    
}

document.addEventListener("input", function (e) {

    if (
        e.target.classList.contains("gym-sets") ||
        e.target.classList.contains("gym-reps") ||
        e.target.classList.contains("gym-exercise")
    ) {

        const groupForm = e.target.closest(".overlay-container-content-gym-form")

        if (!groupForm) return

        const saveButton = groupForm.querySelector(".save-gym-group")

        if (saveButton) {
            saveButton.classList.remove("hidden")
        }
    }
})


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

function addNewForm(button) {

    const overlayContent = button.closest(".overlay-container-content");
    const container = overlayContent.querySelector(".overlay-gym-general-forms");

    const form = container.querySelector(".overlay-container-content-gym-form");
    const newForm = form.cloneNode(true);

    const exercisesRows = newForm.querySelector(".gymExercisesContainer");

    while (exercisesRows.children.length > 1) {
        exercisesRows.lastElementChild.remove();
    }

    newForm.querySelectorAll("input").forEach(input => {
        if (
            input.name !== "workout_day" &&
            input.name !== "csrfmiddlewaretoken"
        ) {
            input.value = "";
        }
    });

    newForm.querySelectorAll("select").forEach(select => {
        select.value = "";

    });

    container.appendChild(newForm);
}

function removeForm(button) {

    const form = button.closest(".overlay-container-content-gym-form");
    const container = form.closest(".overlay-gym-general-forms");

    if (container.children.length > 1) {
        form.remove();
    } else {
        form.querySelectorAll("input").forEach(input => {
            if (
                input.name !== "workout_day" &&
                input.name !== "csrfmiddlewaretoken"
            ) {
                input.value = "";
            }
        });
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


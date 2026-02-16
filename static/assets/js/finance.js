let activeReportId = 'finance-main';
function tabSelector(id,tab) {
    activeReportId = id;
    document.querySelectorAll(".finance-page").forEach(page => {page.classList.remove('active')});
    document.getElementById(id).classList.add('active')

    document.querySelectorAll(".finance-tab").forEach(page => {page.classList.remove('active')});
    tab.classList.add('active')
}

function cardSelector(id,idcard) {
    activeReportId = id;
    document.querySelectorAll(".credit-cards-accounts").forEach(card => {card.classList.remove('active')});
    document.getElementById(id).classList.add('active')

    document.querySelectorAll('.self-card').forEach(card => card.classList.remove('active'))
    idcard.classList.add('active')
}

let activeButton = null;

function addSelfCard(button) {
    const allCards = document.getElementById("credit-cards");

    const form = document.createElement("form");
    form.className = "self-card-form";
    //form.method = "POST";
    //form.action = "/salvar/"; // ou a URL correta

    // BLOQUEIA O RELOAD
    form.addEventListener("submit", (e) => {
        e.preventDefault();
        console.log("Form enviado, mas sem reload 😎");
    });

    //const csrf = document.querySelector('[name=csrfmiddlewaretoken]');
    //if (csrf) {
    //  form.appendChild(csrf.cloneNode(true));
    //}

    const input = document.createElement("input");
    input.type = "text";
    input.name = "card_name";
    input.className = "new-self-card";
    input.placeholder = "Card Name";

    button.classList.remove("btn-add");
    button.classList.add("btn-save");
    button.removeAttribute("onclick");
    button.type = "submit";
    button.textContent = "Save"
    
    


    form.appendChild(input);
    form.appendChild(button);
    allCards.appendChild(form);
}

function setState(btn) {
    btn.classList.toggle("payed");
    if (btn.lastElementChild.textContent === "Payed") {
        btn.lastElementChild.textContent = "Pendent"
    }
    else {
        btn.lastElementChild.textContent = "Payed"
    }
}

function addNewDuty(btn) {
    const motherDiv = document.getElementById("finance-duties-all-content");
    const sonDiv = motherDiv.lastElementChild;
    const newSonDiv = sonDiv.cloneNode(true);

    if (btn.textContent == "Add") {
        const dutyInput = document.createElement("input");
        dutyInput.type = "text";
        dutyInput.placeholder = "Add new duty"
        dutyInput.classList.add("default-input")

        newSonDiv.querySelector("p").replaceWith(dutyInput)

        btn.textContent = "Confirm";
        btn.classList.remove("btn-add");
        btn.classList.add("btn-save");

        motherDiv.appendChild(newSonDiv);
    }
    else if (btn.textContent == "Confirm") {
        btn.type = "submit"
        btn.textContent = "Add";
        btn.classList.remove("btn-save");
        btn.classList.add("btn-add");
    }
}

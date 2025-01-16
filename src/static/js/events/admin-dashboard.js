document.addEventListener("DOMContentLoaded", () => {
    crudEmployee()
})

function crudEmployee() {
    const crudEmployeeBtn = document.getElementById("crudEmployeeBtn")
    const crudEmployeeCard = document.getElementById("crudEmployeeCard")
    crudEmployeeBtn.addEventListener("click", () => {
        crudEmployeeCard.style.display = "flex"
    })
}
document.addEventListener("DOMContentLoaded", () => {
    login()    
})

function login() {
    const loginBtn = document.getElementById("loginBtn")
    const form = document.getElementById("userLoginForm")
    loginBtn.addEventListener("click", async () => {
        const formData = Object.fromEntries(new FormData(form).entries())

        if (!formData["username"] || !formData["password"]) {
            loginInputError(formData["username"], formData["password"])
            textBoxValidation(formData["username"], formData["password"])
            return
        }

        const url = "http://127.0.0.1:5000/login"
        const interface = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Cache-Control": "no-store"
            },
            body: JSON.stringify({
                "username": formData["username"],
                "password": formData["password"]
            })
        }
        try {
            const response = await fetch(
                url, interface
            )

            if (!response.ok) {
                console.log(`A network error has occurred: ${response.status}`)
                return
            }

            const responseData = await response.json() //success, first_time, role

            if (responseData["success"] && !responseData["first_time"]) {
                switch (responseData["role"]) {

                    case "admin":
                        window.location.href = "http://127.0.0.1:5000/admin-homepage"
                        break

                    case "doctor":
                        window.location.href = "http://127.0.0.1:5000/doctor-homepage"
                        break

                    case "pharmacist":
                        window.location.href = "http://127.0.0.1:5000/pharmacist-homepage"
                        break

                    case "help desk":
                        window.location.href = "http://127.0.0.1:5000/helpdesk-homepage"
                        break

                    default:
                        console.log("Role does not exist")
                        break
                }
            } else if (responseData["success"] && responseData["first_time"]) {
                // CHANGE THE INPUT CREDENTIALS
            } else {
                loginInputError()
            }
        } catch {
            console.error("Error")
        }
    })
}

function loginInputError(usernameInput = null, passwordInput = null) {
    const username = document.getElementById("username")
    const password = document.getElementById("password")
    const styleSheet = document.styleSheets[0]

    styleSheet.insertRule(`
        @keyframes horizontal-shake {
            0% { transform: translateX(0); }
            25% { transform: translateX(1px); }
            50% { transform: translateX(-1px); }
            75% { transform: translateX(1px); }
            100% { transform: translateX(0); }
        }
    `)

    if (!usernameInput && !passwordInput) {
        username.style.border = "1px solid red"
        password.style.border = "1px solid red"
        triggerAnimaton(username)
        triggerAnimaton(password)
    } else if (!usernameInput) {
        username.style.border = "1px solid red"
        triggerAnimaton(username)
        password.style.border = null
    } else if (!passwordInput) {
        password.style.border = "1px solid red"
        triggerAnimaton(password)
        username.style.border = null
    }
    // ease-in-out
    // cubic-bezier( 0, 0, 0, 1 )
}

function triggerAnimaton(textBox) {
    textBox.style.animation = "none"
    textBox.offsetHeight
    textBox.style.animation = "horizontal-shake 0.5s cubic-bezier( 0, 0, 0, 1 )"
}

function textBoxValidation(username, password) {
    const inputErrorText = document.getElementById("inputErrorText")

    if (!username && !password) {
        inputErrorText.innerText = "both fields are empty"
        inputErrorText.hidden = false
    } else if (!username) {
        inputErrorText.innerText = "username field is empty"
        inputErrorText.hidden = false
    } else if (!password) {
        inputErrorText.innerText = "password field is empty"
        inputErrorText.hidden = false
    } else {
        inputErrorText.hidden = true
    }
}

function credential() {
    const finishBtn = document.getElementById("finishBtn")
    const form = document.getElementById("credentialInputForm")

    finishBtn.addEventListener("click", () => {
        const formData = Object.fromEntries(new FormData(form).entries())
        const url = "http://127.0.0.1:5000/credential-registration"
        const interface = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Cache-Control": "no-store"
            },
            body: JSON.stringify({
                "name": {
                    "first_name": formData["first_name"],
                    "middle_initial": formData["middle_initial"],
                    "last_name": formData["last_name"],
                    "suffix": formData["suffix"]
                },  
                "demograph": {
                    "age": formData["age"],
                    "birthdate": formData["birth"],
                    "sex": formData["sex"],
                    "marital_status": formData["marital_status"],
                    "nationality": formData["nationality"],
                    "religion": formData["religion"]
                },
                "address": {
                    "house_number": formData["house_number"],
                    "street": formData["street"],
                    "division": formData["division"],
                    "division_type": formData["division_type"],
                    "city": formData["city"],
                    "zip_code": formData["zip_code"]
                },
                "contact": {
                    "mobile_number": formData["mobile_number"],
                    "email": formData["email"]
                }
            })
        }
    })
}

function divisionOrder(divisionName, divisionType) {
    if (divisionType == "Barangay") {
        return `${divisionType} ${divisionName}`
    } else {
        return `${divisionName} ${divisionType}`
    }
}
document.addEventListener("DOMContentLoaded", () => {
    loginInputError()
    login()    
})

function login() {
    const loginBtn = document.getElementById("loginBtn")
    const form = document.getElementById("userLoginForm")
    loginBtn.addEventListener("click", async () => {
        const formData = Object.fromEntries(new FormData(form).entries())

        if (!formData["username"] || !formData["password"]) {
            loginInputError(formData["username"], formData["password"])
            // Create the functionality for if a certain ui is empty
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

function loginInputError(username = null, password = null) {
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

    if (username === null) {
        username.style.border = "1px solid red"
        username.style.animation = "horizontal-shake 0.5s cubic-bezier( 0, 0, 0, 1 )"
    } else if (password === null) {
        password.style.border = "1px solid red"
        password.style.animation = "horizontal-shake 0.5s cubic-bezier( 0, 0, 0, 1 )"
    } else {
        username.style.border = "1px solid red"
        password.style.border = "1px solid red"
        username.style.animation = "horizontal-shake 0.5s cubic-bezier( 0, 0, 0, 1 )"
        password.style.animation = "horizontal-shake 0.5s cubic-bezier( 0, 0, 0, 1 )"
    }
    // ease-in-out
    // cubic-bezier( 0, 0, 0, 1 )
}

function emptyField() {

}
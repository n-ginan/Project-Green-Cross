document.addEventListener("DOMContentLoaded", () => {
    const username = document.getElementById("username")    
    const password = document.getElementById("password")
    login(username, password)    
})

function login(username, password) {
    const loginBtn = document.getElementById("loginBtn")
    const form = document.getElementById("userLoginForm")
    loginBtn.addEventListener("click", async () => {
        const formData = Object.fromEntries(new FormData(form).entries())
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

            const responseData = await response.json()

            if (responseData["success"] && !responseData["first_time"]) {
                // REDIRECTION TO HOMEPAGE
            } else if (responseData["success"] && responseData["first_time"]) {
                // REDIRECTION TO CREDENTIAL CREATION
            } else {
                // INPUT ERROR HTML/STYLES MANIPULATION
            }
        } catch {
            console.error("Error")
        }
    })
}


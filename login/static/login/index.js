// função de interação para "was-validated" no formulario de registro:
document.addEventListener("DOMContentLoaded", function() {
    const formulario = document.querySelector(".formulario-register");
    const formulario_inputs = formulario.querySelectorAll(".formulario-input");

    formulario_inputs.forEach( function (input) {
        input.addEventListener("click", function() {
            formulario.classList.add("was-validated");
        });
    });
});

// inplementação da função de mostrar e ocultar senha:

function togglePasswordVisibility() {

    var passWordinput = document.getElementById("id_password");
    var toggleIcon = document.querySelector(".toggle-password");

    if (passWordinput.type === "password") {
        passWordinput.type = "text";
        toggleIcon.classList.remove("fa-eye-slash");
        toggleIcon.classList.add("fa-eye")
    }
    else {
        passWordinput.type = "password";
        toggleIcon.classList.remove("fa-eye");
        toggleIcon.classList.add("fa-eye-slash");
    }
}
document.querySelector(".toggle-password").addEventListener("click", togglePasswordVisibility);

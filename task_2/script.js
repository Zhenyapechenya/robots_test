function validateForm() {
    var fullName = document.getElementById("fullName").value;
    var phone = document.getElementById("phone").value;
    var email = document.getElementById("email").value;

    if (fullName === "") {
        alert("Пожалуйста, заполните поле ФИО.");
        return false;
    }

    if (!/^\d{10}$/.test(phone)) {
        alert("Пожалуйста, введите корректный мобильный телефон (10 цифр).");
        return false;
    }

    if (email !== "" && !/^\S+@\S+\.\S+$/.test(email)) {
        alert("Пожалуйста, введите корректный email.");
        return false;
    }

    return true;
}
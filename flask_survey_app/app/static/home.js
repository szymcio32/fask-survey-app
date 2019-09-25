// Validate name and email in survey form

btn = document.querySelector("#survey-btn");
if (btn !== null){
    btn.addEventListener('click', validateSurvey);
}


function validateSurvey(e){
    const name_value = document.querySelector('form input[name="name"]').value;
    const email_value = document.querySelector('form input[name="email"]').value;

    const name_validation = document.querySelector('#name_validation');
    const email_validation = document.querySelector('#email_validation');

    if (name_value === ""){
        name_validation.style.display = 'block';
    } else {
        name_validation.style.display = 'none';
    }
    if (email_value === ""){
        email_validation.style.display = 'block';
    } else {
        email_validation.style.display = 'none';
    }
}


// validate password during adding admin user

add_admin_password = document.querySelector("#add-admin-password");
add_admin_confirm_password = document.querySelector("#add-admin-confirm-password");
if (add_admin_password !== null){
    add_admin_password.addEventListener('keyup', checkPassword);
    add_admin_confirm_password.addEventListener('keyup', checkPassword);
}


function checkPassword(e){
    admin_password_text = document.querySelector("#add-admin-password").value
    admin_confirm_password_text = document.querySelector("#add-admin-confirm-password").value
    if (admin_password_text !== admin_confirm_password_text){
        document.querySelector('#confirm-password-validation-invalid').style.display = 'block';
        document.querySelector('#confirm-password-validation-valid').style.display = 'none';
    }
    else {
        document.querySelector('#confirm-password-validation-invalid').style.display = 'none';
        document.querySelector('#confirm-password-validation-valid').style.display = 'block';
    }
}


// Count characters in textarea fields

like_text = document.querySelector('#like-textarea');
dislike_text = document.querySelector('#dislike-textarea');
if (like_text !== null){
    like_text.addEventListener('keyup', countWords);
    dislike_text.addEventListener('keyup', countWords);
}


function countWords(e){
    let text = `Characters left: ${300 - e.target.value.length}`;

    if (e.target.id === "like-textarea"){
        document.querySelector('#like-length').innerHTML = text;
    }
    else{
        document.querySelector('#dislike-length').innerHTML = text;
    }
}
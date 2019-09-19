function validateSurvey(){
    var name_value = document.forms["survey_form"]["name"].value
    var email_value = document.forms["survey_form"]["email"].value

    if (name_value == ""){
        document.getElementById('name_validation').style.display = 'block';
    } else {
        document.getElementById('name_validation').style.display = 'none';
    }
    if (email_value == ""){
        document.getElementById('email_validation').style.display = 'block';
    } else {
        document.getElementById('email_validation').style.display = 'none';
    }
}

function checkPassword(){
    if (document.forms["add-admin-form"]["add-admin-password"].value !== document.forms["add-admin-form"]["add-admin-confirm-password"].value){
        document.getElementById('confirm-password-validation-invalid').style.display = 'block';
        document.getElementById('confirm-password-validation-valid').style.display = 'none';
    }
    else {
        document.getElementById('confirm-password-validation-invalid').style.display = 'none';
        document.getElementById('confirm-password-validation-valid').style.display = 'block';
    }
}

document.getElementById('like-textarea').onkeyup = function(){
    document.getElementById('like-length').innerHTML = "Characters left:".concat(' ', 300 - this.value.length);
}
document.getElementById('dislike-textarea').onkeyup = function(){
    document.getElementById('dislike-length').innerHTML = "Characters left:".concat(' ', 300 - this.value.length);
}
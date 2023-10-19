
// -------- Objeto que armazena os valores booleanos que validam o envio do formulário --------

let checkInput = {
    email : false, 
    phone : true, 
    password : false, 
    name : true
}

const NAME_ERROR = document.querySelector('li.hidden:nth-child(2)')
const EMAIL_ERROR = document.querySelector('li.hidden:nth-child(3)')
const PHONE_ERROR = document.querySelector('li.hidden:nth-child(4)')
const PASSWORD_ERROR = document.querySelector('li.hidden:nth-child(5)')


// -------- Formatação da entrada de Numerais --------

const NUMBER_ID = document.getElementById('id_number');
NUMBER_ID.addEventListener('input', () => {formatNumeral(NUMBER_ID)})

function formatNumeral(field) {
    let value = field.value.replace(/\D/g, '') //Remove todos os caracteres não numéricos
    field.value = value
}

// -------- Formatação e Validação na entrada de Telefone/Celular (Brasileiros) --------

const BORDER_PHONE = document.querySelector('div.input_field > input')
const PHONE_INPUT = document.getElementById('phone');
PHONE_INPUT.addEventListener('input', () => {formatNumeral(PHONE_INPUT), cleanPhone(),validatePhone(), changeToDefault()});

function cleanPhone(){
    let phone = PHONE_INPUT.value
    if (phone.length === 11) {
        cleanedPhone = phone.replace(/(\d{2})(\d{5})(\d{4})/, '($1)$2-$3'); //Formatação para Celular
    } else if (phone.length === 10) {
        cleanedPhone = phone.replace(/(\d{2})(\d{4})(\d{4})/, '($1)$2-$3'); //Formatação para Telefone
    } else {
        cleanedPhone = phone;
        
    }

    PHONE_INPUT.value = cleanedPhone
}

function validatePhone() {
    let phone = PHONE_INPUT.value
    let regex = /^\(?(?:[14689][1-9]|2[12478]|3[1234578]|5[1345]|7[134579])\)? ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$/;
    let validation = regex.test(phone)
    if (validation){
        changeGreen(PHONE_INPUT)
        PHONE_ERROR.classList.add('hidden')
        return checkInput.phone = true // telefone formatado, válido

    } else if (phone === "") {
        return checkInput.phone = true // Campo em branco, telefone válido
    
    } else {
        changeRed(PHONE_INPUT)
        PHONE_ERROR.classList.remove('hidden')
        return checkInput.phone = false // fora de formatação, telefone inválido
    }
}

// -------- Validação de email --------

const EMAIL_FIELD = document.getElementById('email')
EMAIL_FIELD.addEventListener('input', () => validateEmail())

function validateEmail() {
    let email = EMAIL_FIELD.value
    let regex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
    let validation = regex.test(email)
    if(validation){
        EMAIL_ERROR.classList.add("hidden")
        changeGreen(EMAIL_FIELD)
        return checkInput.email = true // Email válido
    } 
    else {
        changeRed(EMAIL_FIELD)
        EMAIL_ERROR.classList.remove("hidden")
        return checkInput.email = false // Email inválido
    }
}

// -------- Alterações causadas pelo tipo do usuário --------

const TYPE_OF_USER = document.getElementById('user_type')
TYPE_OF_USER.addEventListener('input', () => verifyTypeOfUser())

function verifyTypeOfUser() {
    let userType = TYPE_OF_USER.value
    let nameField = document.querySelector('input#fullname')
    let numberID = document.querySelector('input#id_number')
    let birthDate = document.querySelector('div.input_field>legend')

    if (userType === "responsavel") {
        nameField.classList.remove('hidden')
        numberID.placeholder = 'Matrícula do seu dependente*'
        birthDate.textContent = 'Data de nascimento do seu dependente*'
        return checkInput.name = false // nome  inválido até o preenchimento do nome na formatação correta ser feito.
    } 
    else {
        nameField.classList.add('hidden')
        NAME_ERROR.classList.add('hidden')
        numberID.placeholder = 'Matrícula*'
        birthDate.textContent = 'Data de Nascimento*'
        return checkInput.name = true  // alunos e professores válidação automatica no campo do nome.
    }
}

// -------- Validação no Campo de senhas --------

const PASSWORD_FIELD = document.getElementById('password1')
const PASSWORD_CONFIRM = document.getElementById('password2')

PASSWORD_FIELD.addEventListener('input', () => validatePassword())
PASSWORD_CONFIRM.addEventListener('input', () => validatePassword())

function validatePassword(){
    let userPassword = PASSWORD_FIELD.value
    let userPasswordConfirm = PASSWORD_CONFIRM.value
    let regex = /^(?=.*[A-Z])(?=.*[!#@$%&*])(?=.*[0-9])(?=.*[a-z]).{8,64}$/;
    let validation = regex.test(userPassword)
    
    if (validation) {
        changeGreen(PASSWORD_FIELD)
        if (userPasswordConfirm !== userPassword) {
            changeRed(PASSWORD_CONFIRM)
            PASSWORD_ERROR.classList.remove('hidden')
            return checkInput.password = false
        } else {
            changeGreen(PASSWORD_CONFIRM)
            PASSWORD_ERROR.classList.add('hidden')
            return checkInput.password = true
        }
    } 
    else {
        changeRed(PASSWORD_FIELD)
        return checkInput.password = false
    }
}

// -------- Alterações visuais --------

function changeGreen(query) {
    query.style.borderColor = 'green'
}

function changeRed(query) {
    query.style.borderColor = 'red'
}

function changeToDefault() {
    let phone = PHONE_INPUT.value
    let computedStyle = getComputedStyle(BORDER_PHONE);
    let defaultColor = computedStyle.borderColor;
    if (phone === "") {
        PHONE_ERROR.classList.add('hidden')
        PHONE_INPUT.style.borderColor = defaultColor;
    }
}


// -------- Formatação e validação de nome --------

const NAME_INPUT = document.getElementById('fullname')
NAME_INPUT.addEventListener('input', () => {cleanName(), validateName()})

function cleanName() {
    //---- Remove todos os numerais e especiais, menos acentuados e espaço. ----
    let value = NAME_INPUT.value.replace(/[^a-zA-Z\u00C0-\u017F\s]+/gu, '')
    NAME_INPUT.value = value
}

function validateName() {
    let name = NAME_INPUT.value
    let regex = /^[a-zA-Z\u00C0-\u017F]{2,}(?: [a-zA-Z\u00C0-\u017F]{1,})+$/u
    let validation = regex.test(name)
    if (validation === true) {
        changeGreen(NAME_INPUT)
        NAME_ERROR.classList.add('hidden')
        return checkInput.name = true  // Nome válido
    } else {
        changeRed(NAME_INPUT)
        NAME_ERROR.classList.remove('hidden')
        return checkInput.name = false // Nome inválido
    }
}

// -------- Validar envio --------

const REGISTER_FORM = document.getElementById("register_form");
REGISTER_FORM.addEventListener("submit", validateSubmit);

function verifyObject(objeto) {
    let fields = Object.values(objeto)
    return fields.every(checkInput => checkInput === true);
}

function validateSubmit(event) {
    // Verifica se todos os itens do objeto são true 
    if (!verifyObject(checkInput)) {
      alert("Por favor, preencha todos os campos corretamente.");
      event.preventDefault(); //Nesse contexto, o metódo impede o envio do formulário. 
    }
    else {
        return true
    }
}

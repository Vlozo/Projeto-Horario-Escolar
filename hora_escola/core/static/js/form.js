
// -------- Elemento que armazena os valores booleanos que validam o envio do formulário --------

let valor = {
    email : false, 
    telefone : true, 
    senha : false, 
    nome : true
}

const nome_error = document.querySelector('li.hidden:nth-child(2)')
const email_error = document.querySelector('li.hidden:nth-child(3)')
const phone_error = document.querySelector('li.hidden:nth-child(4)')
const senha_error = document.querySelector('li.hidden:nth-child(5)')


// -------- Formatação da entrada de Numerais --------

const matricula_id = document.getElementById('matricula')
matricula_id.addEventListener('input', () => {formatNumeral(matricula_id), validarDados()})

function formatNumeral(field) {
    let value = field.value.replace(/\D/g, '') //Remove todos os caracteres não numéricos
    field.value = value
}

// -------- Formatação e Validação na entrada de Telefone/Celular (Brasileiros) --------

const borderTel = document.querySelector('div.input_field > input')
const phoneInput = document.getElementById('telefone');
phoneInput.addEventListener('input', () => {formatNumeral(phoneInput), formatarTelefone(),validarTelefone(), changeToDefault()});

function formatarTelefone(){
    let telefone = phoneInput.value
    if (telefone.length === 11) {
        telefoneFormatado = telefone.replace(/(\d{2})(\d{5})(\d{4})/, '($1)$2-$3'); //Formatação para Celular
    } else if (telefone.length === 10) {
        telefoneFormatado = telefone.replace(/(\d{2})(\d{4})(\d{4})/, '($1)$2-$3'); //Formatação para Telefone
    } else {
        telefoneFormatado = telefone;
        
    }

    phoneInput.value = telefoneFormatado
}

function validarTelefone() {
    let telefone = phoneInput.value
    let regex = /^\(?(?:[14689][1-9]|2[12478]|3[1234578]|5[1345]|7[134579])\)? ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$/;
    let validation = regex.test(telefone)
    if (validation){
        changeGreen(phoneInput)
        phone_error.classList.add('hidden')
        return valor.telefone = true // telefone formatado, válido

    } else if (telefone === "") {
        return valor.telefone = true // Campo em branco, telefone válido
    
    } else {
        changeRed(phoneInput)
        phone_error.classList.remove('hidden')
        return valor.telefone = false // fora de formatação, telefone inválido
    }
}

// -------- Validação de email --------

const email_field = document.getElementById('email')
email_field.addEventListener('input', () => validarEmail())

function validarEmail() {
    let email = email_field.value
    let regex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
    let validation = regex.test(email)
    if(validation){
        email_error.classList.add("hidden")
        changeGreen(email_field)
        return valor.email = true // Email válido
    } 
    else {
        changeRed(email_field)
        email_error.classList.remove("hidden")
        return valor.email = false // Email inválido
    }
}

// -------- Alterações causadas pelo tipo do usuário --------

const userType = document.getElementById('select_id')
userType.addEventListener('input', () => kindOfUser())

function kindOfUser() {
    let tipo = userType.value
    let etiqueta = document.querySelector('input#nome')
    let matricula = document.querySelector('input#matricula')
    let nascimento = document.querySelector('div.input_field>legend')

    if (tipo === "responsavel") {
        etiqueta.classList.remove('hidden')
        matricula.placeholder = 'Matrícula do seu dependente*'
        nascimento.textContent = 'Data de nascimento do seu dependente*'
        return valor.nome = false // nome  inválido até o preenchimento do nome na formatação correta ser feito.
    } 
    else {
        etiqueta.classList.add('hidden')
        nome_error.classList.add('hidden')
        matricula.placeholder = 'Matrícula*'
        nascimento.textContent = 'Data de Nascimento*'
        return valor.nome = true  // alunos e professores válidação automatica no campo do nome.
    }
}

// -------- Validação no Campo de senhas --------

const senha = document.getElementById('senha')
const confirmar_senha = document.getElementById('confirmar_senha')

senha.addEventListener('input', () => validarSenha())
confirmar_senha.addEventListener('input', () => validarSenha())

function validarSenha(){
    let userSenha = senha.value
    let userConfirmar = confirmar_senha.value
    let regex = /^(?=.*[A-Z])(?=.*[!#@$%&*])(?=.*[0-9])(?=.*[a-z]).{8,64}$/;
    let validation = regex.test(userSenha)
    
    if (validation) {
        changeGreen(senha)
        if (userConfirmar !== userSenha) {
            changeRed(confirmar_senha)
            senha_error.classList.remove('hidden')
            return valor.senha = false
        } else {
            changeGreen(confirmar_senha)
            senha_error.classList.add('hidden')
            return valor.senha = true
        }
    } 
    else {
        changeRed(senha)
        return valor.senha = false
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
    let telefone = phoneInput.value
    let minhadiv = document.querySelector('div.input_field > input')
    let computedStyle = getComputedStyle(borderTel);
    let defaultColor = computedStyle.borderColor;
    if (telefone === "") {
        phone_error.classList.add('hidden')
        phoneInput.style.borderColor = defaultColor;
    }
}


// -------- Formatação e validação de nome --------

const name_input = document.getElementById('nome')
name_input.addEventListener('input', () => {formatarNome(), validarNome()})

function formatarNome() {
    //---- Remove todos os numerais e especiais, menos acentuados e espaço. ----
    let value = name_input.value.replace(/[^a-zA-Z\u00C0-\u017F\s]+/gu, '')
    name_input.value = value
}

function validarNome() {
    let nome = name_input.value
    let regex = /^[a-zA-Z\u00C0-\u017F]{2,}(?: [a-zA-Z\u00C0-\u017F]{1,})+$/u
    let validation = regex.test(nome)
    if (validation === true) {
        console.log('Nome válido!')
        changeGreen(name_input)
        nome_error.classList.add('hidden')
        return valor.nome = true  // Nome válido
    } else {
        console.log('Nome inválido!')
        changeRed(name_input)
        nome_error.classList.remove('hidden')
        return valor.nome = false // Nome inválido
    }
}

// -------- Validar envio --------

const cadastro = document.getElementById("cadastro");
cadastro.addEventListener("submit", validarEnvio);

function validarDados(){
    let codigo = matricula_id.value
    if (codigo === "26638250") {
        console.log(valor)
    }
}

function verificar(objeto) {
    let valores = Object.values(objeto)
    return valores.every(valor => valor === true);
}

function validarEnvio(event) {
    // Verifica se todos os itens do objeto são true usando o operador ternário
    if (!verificar(valor)) {
      alert("Por favor, preencha todos os campos corretamente.");
      event.preventDefault();
    }
    else {
        return true
    }
}

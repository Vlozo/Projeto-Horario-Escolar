
// Dark/Light Theme

const inputContainer = document.querySelector('input#theme')
const rootElement = document.documentElement

const lightTheme = {
    '--background-color': '#eff1f3',
    '--text-color': '#000000',
    '--button-text': '#ffffff',
    '--destaque': '#3482db',
    '--login-bg': '#ffffff',
    '--input-bg': '#ffffff',
    '--input-txt': '#000000',
    '--input-border': '#cacaca',
    '--input-placeholder': '#949494',
    '--button-entrar': '#3482db',
    '--button-novaconta': '#289c55',
    '--switch-color': '#212529',
}

const darkTheme = {
    '--background-color': '#212529',
    '--text-color': '#d4d4d4',
    '--button-text': '#e9e9e9',
    '--destaque': '#3a8ff1',
    '--login-bg': '#343a41',
    '--input-bg': '#4d5157',
    '--input-txt': '#d1d6db',
    '--input-border': '#71757c',
    '--input-placeholder': '#949494',
    '--button-entrar': '#3482db',
    '--button-novaconta': '#228849',
    '--switch-color': '#eff1f3',
}


inputContainer.addEventListener('change', function() {
    const isChecked = inputContainer.checked
    isChecked ? changeTheme(darkTheme) : changeTheme(lightTheme)
})

function changeTheme(theme) {
    for (let prop in theme) {
        changeProperty(prop, theme[prop])
    }
}

function changeProperty(property, value) {
    rootElement.style.setProperty(property, value)
}

// Mostrar/Esconder Senha

let container = document.querySelector('div.input_field')
let input = document.querySelector('input#senha_id')
let icon = document.querySelector('img#eye-icon')

icon.addEventListener('click', function() {
    container.classList.toggle('visible');
    if(container.classList.contains('visible')) {
        icon.src = 'static/assets/eye-off.svg';
        input.type = 'text';
    } else {
        icon.src = 'static/assets/eye.svg';
        input.type = 'password';
    }
})

// Mostrar Erros

document.body.addEventListener('htmx:beforeSwap', function(evt) {    
    // indica que erros deverão ser renderizados 
    evt.detail.shouldSwap = true;
    // suprime mensagens de erro do console  
    evt.detail.isError = false;
});

from django.core.validators import RegexValidator


validate_password = RegexValidator(
    regex = r"^(?=.*[A-Z])(?=.*[!#@$%&*])(?=.*[0-9])(?=.*[a-z]).{8,64}$",
    message = "Sua senha precisa ter no mínimo 8 digitos e deve conter um caractere maiúsculo, um caractere minúsculo, um número e um caractere especial (#!$*&@?)",
    code = "invalid_password"
)
# Limite máximo é de 64 caracteres

validate_fullname = RegexValidator(
    regex = r"^[a-zA-Z\u00C0-\u017F]{2,}(?: [a-zA-Z\u00C0-\u017F]{1,})+$",
    message = "O nome inserido é inválido, certifique-se de fornecer seu nome e sobrenome.",
    code = "invalid_name"
)
# Verifica se o nome é apenas composto por maiúsculas, minúsculas e acentuadas. 
# Deve conter dois ou mais caracteres.
# Sobrenome é um grupo de não-captura que corresponde a um ou mais grupos de caracteres separados por um espaço


validate_phone = RegexValidator(
    regex= r"^\(?(?:[14689][1-9]|2[12478]|3[1234578]|5[1345]|7[134579])\)? ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$",
    message = "O número de telefone é inválido, verifique se digitou o número certo ou se o DDD é válido no Brasil.",
    code = "invalid_phone"
)
# Valida números de telefone apenas no formato brasileiro; Tem entre oito e nove dígitos
# Opcionalmente pode ter um hífen e um parêntese de abertura.
# DDD obrigatório, todos os números de celular (9 dígitos) devem começar com 9


only_numbers_validate = RegexValidator(
    regex = r"^\d+$",
    message = "O campo deve conter apenas números.",
    code = "invalid_caracter"
)

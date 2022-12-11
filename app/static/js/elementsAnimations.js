var buttonForm = document.querySelector('#form-delete-save input[type=submit]')
var formDelete = document.querySelector('#form-delete-save')

buttonForm.addEventListener('mouseenter', function(event){
    document.querySelector('#form-delete-save input[type=password]').classList.add('move-input')
    document.querySelector('#form-delete-save input[type=password]').style.display = 'inline-block'
    
})

formDelete.addEventListener('mouseleave', function(event){
    document.querySelector('#form-delete-save input[type=password]').classList.remove('move-input')
    document.querySelector('#form-delete-save input[type=password]').style.display = 'none'
})

setTimeout(function(){
    document.querySelector('form .mensagem-form').innerText = ''
}, 8000)

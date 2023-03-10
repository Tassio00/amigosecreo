
let participante_name = document.getElementById('participante_name');
let email_participante = document.getElementById('email_participante');
let btnaddparticipante = document.getElementById('btnaddparticipante');
let listaParticipantes = document.getElementById('listaParticipantes');

participante_name.addEventListener('keypress', (e) => {

    if(e.keycode === 13 ){
        let participante= {
            nome:participante_name.value,
            email: email_participante.value,
            
        }
        adicioarParticipanteNaLista(participante);
    }


});

btnaddparticipante.addEventListener('click', (e) =>{
    let participante = {
        nome:participante_name.value,
        email: email_participante.value,
        
    }
    adicioarParticipanteNaLista(participante);
});



function adicioarParticipanteNaLista(participante){
    listaParticipantes.appendChild(adicioarLi(participante));
    participante_name.value;
}



function adicioarLi(participante){
    let li = document.createElement('li');

    let spanName = document.createElement('span');
    spanName.classList.add('n_participante');       
    spanName.innerHTML = participante.nome;  

    let spanEmail = document.createElement('span');
    spanEmail.classList.add('e_participante');
    spanEmail.innerHTML = participante.email;

    let div = document.createElement('div');

    let spanIconEdit = document.createElement('span');
    spanIconEdit.classList.add('material-symbols-outlined');
    spanIconEdit.innerHTML = 'edit';

    let spanIconDell = document.createElement('span');
    spanIconDell.classList.add('material-symbols-outlined');
    spanIconDell.innerHTML = 'delete';


    div.appendChild(spanIconEdit);
    div.appendChild(spanIconDell);

    li.appendChild(spanName);
    li.appendChild(spanEmail);
    li.appendChild(div);

    return li;

}
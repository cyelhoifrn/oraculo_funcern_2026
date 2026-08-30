// =====================================
// ORÁCULO FUNCERN
// Dashboard + Questões
// v1.1
// =====================================


// -----------------------------
// Relógio
// -----------------------------

function atualizarRelogio(){

    const agora = new Date();

    document.getElementById("hora").innerHTML =
        agora.toLocaleTimeString("pt-BR");

}

setInterval(atualizarRelogio,1000);

atualizarRelogio();


// -----------------------------
// Saudação
// -----------------------------

(function(){

    const hora = new Date().getHours();

    let texto="Olá";

    if(hora<12)
        texto="Bom dia";

    else if(hora<18)
        texto="Boa tarde";

    else
        texto="Boa noite";

    document.getElementById("saudacao").innerHTML =
        texto + ", Cyelho 👋";

})();


// -----------------------------
// Menu
// -----------------------------

const menus=document.querySelectorAll(".menu");

menus.forEach(menu=>{

    menu.addEventListener("click",function(e){

        e.preventDefault();

        menus.forEach(x=>x.classList.remove("ativo"));

        this.classList.add("ativo");

        const pagina=this.dataset.pagina;

        if(pagina==="questoes"){

            document.getElementById("dashboard").style.display="none";

            document.getElementById("paginaQuestoes").style.display="block";

            carregarQuestoes();

        }

        if(pagina==="dashboard"){

            document.getElementById("dashboard").style.display="block";

            document.getElementById("paginaQuestoes").style.display="none";

        }

    });

});


// -----------------------------
// API
// -----------------------------

async function carregarStatus(){

    const resposta=await fetch("/api/status");

    const dados=await resposta.json();

    console.log(dados);

}

carregarStatus();


// -----------------------------
// Questões
// -----------------------------

async function carregarQuestoes(){

    const resposta=await fetch("/api/questoes");

    const dados=await resposta.json();

    document.getElementById("totalQuestoes").innerHTML=dados.length;

    let html="";

    if(dados.length===0){

        html=`
        <tr>

            <td colspan="4">

                Nenhuma questão cadastrada.

            </td>

        </tr>
        `;

    }

    else{

        dados.forEach(q=>{

            html+=`

            <tr>

                <td>${q.id}</td>

                <td>${q.disciplina}</td>

                <td>${q.assunto}</td>

                <td>${q.resposta}</td>

            </tr>

            `;

        });

    }

    document.getElementById("tabelaQuestoes").innerHTML=html;

}


// -----------------------------
// Pesquisa
// -----------------------------

const pesquisa=document.getElementById("pesquisa");

pesquisa.addEventListener("keyup",function(){

    const termo=this.value.toLowerCase();

    const linhas=document.querySelectorAll("#tabelaQuestoes tr");

    linhas.forEach(linha=>{

        if(linha.innerText.toLowerCase().includes(termo))

            linha.style.display="";

        else

            linha.style.display="none";

    });

});
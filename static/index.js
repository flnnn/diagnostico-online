function formatarEntradaCep(event) {
    let cep = event.target.value.replace(/\D/g, '');
    if (cep.length <= 5) {
        cep = cep.replace(/(\d{2})(\d{0,3})/, '$1$2');
    } else {
        cep = cep.replace(/(\d{2})(\d{3})(\d{0,3})/, '$1$2-$3');
    }
    event.target.value = cep;
}

let entradaCep = document.getElementById("cep");
let seletorRaio = document.getElementById("raio");
let infoRaio = document.getElementById("raio-info");

entradaCep.addEventListener("input", formatarEntradaCep);

seletorRaio.addEventListener("input", () => {
    metros = seletorRaio.value;
    infoRaio.textContent = `Raio: ${metros} metros.`;
});

// TESTE
let botaoDiagnosticar = document.querySelector("#gerarDiagnostico");

function mostrarAlerta() {
    const sintoma1 = document.getElementById('sintoma1').value;
    const sintoma2 = document.getElementById('sintoma2').value;
    const sintoma3 = document.getElementById('sintoma3').value;

    const sintomasSelecionados = [sintoma1, sintoma2, sintoma3].filter(sintoma => sintoma);

    if (sintomasSelecionados.length > 0) {
        alert('Sintomas selecionados: ' + sintomasSelecionados.join(', '));
    } else {
        alert('Nenhum sintoma selecionado.');
    }
}

// botaoDiagnosticar.addEventListener("click", mostrarAlerta);

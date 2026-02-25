//const API="http://127.0.0.1:5000"
const API = ""

async function cargarMedicos() {
    const res = await fetch(`${API}/medicos`)
    const data = await res.json()
    const lista = document.getElementById("listaMedicos")
    lista.innerHTML = ""
    data.forEach(element => {
        lista.innerHTML += `<li>${element.id} - ${element.nombre}</li>`
    });
    
}

async function cargarTurnos() {
    const medicoId = document.getElementById("medicoId").value
    const res = await fetch(`${API}/turnos/${medicoId}`)

    const data = await res.json()

    const lista = document.getElementById("listaTurnos")
    lista.innerHTML = ""
    data.forEach(element => {
        lista.innerHTML += `<li>${element.fecha_hora} - ${element.nombre_paciente}</li>`
    });
}

async function crearTurno() {
    const respuesta = document.getElementById("respuesta");



    const medico_id = document.getElementById("medico_id").value
    const fecha_hora = document.getElementById("fecha_hora").value
    const paciente = document.getElementById("paciente").value

    const res = await fetch(`${API}/turnos`, {

        // Método HTTP
        method: "POST",

        // Cabecera obligatoria cuando enviamos JSON
        headers: {
            "Content-Type": "application/json"
        },

        // body → datos que enviamos al backend
        // JSON.stringify convierte el objeto JS a JSON válido
        body: JSON.stringify({
            medico_id,
            fecha_hora,
            paciente
        })
    })

    const data = await res.json()
    document.getElementById("respuesta").innerText = JSON.stringify(data, null, 2)

    
    respuesta.style.display = "block";
    respuesta.textContent = JSON.stringify(data, null, 2)


}
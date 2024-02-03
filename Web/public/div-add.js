console.log("file div-add.js loaded")




function addDiv() {
    // Récupère la valeur de l'input
    var inputValue = document.getElementById("inputLetter").value;

    // Crée un élément div
    var newDiv = document.createElement("div");

    // Ajoute la classe pour le style (facultatif)
    newDiv.className = "letterDiv";

    // Ajoute le texte de l'input à la div
    newDiv.appendChild(document.createTextNode(inputValue));

    // Récupère l'élément de sortie
    var outputDiv = document.getElementById("outputDiv");

    // Vide le contenu précédent de la div de sortie
    outputDiv.innerHTML = "";

    // Ajoute la nouvelle div à la div de sortie
    outputDiv.appendChild(newDiv);
}



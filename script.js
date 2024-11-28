// Fonction pour afficher un message lors du clic sur le bouton "Cliquer"
function showMessage(movieTitle) {
    const message = `Voulez-vous continuer à regarder ${movieTitle} ?`;
    const isConfirmed = confirm(message);  // Affiche une boîte de dialogue pour la confirmation

    if (isConfirmed) {
        alert('Vous avez choisi de continuer à regarder le film!');
    } else {
        alert('Vous avez choisi de ne pas continuer.');
    }
}




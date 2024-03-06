function showPopup(message) {
  document.getElementById('popup-message').textContent = message;
  document.getElementById('popup-container').style.display = 'block';
}

function closePopup() {
  document.getElementById('popup-container').style.display = 'none';
}
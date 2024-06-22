document.addEventListener('DOMContentLoaded', function() {
    const editorElement = document.querySelector('.editor');
    const editorUrl = editorElement.dataset.editorUrl; // Obtiene la URL desde el atributo data-editor-url

    const userStaffElement = document.querySelector('.userStaff');
    const isStaff = userStaffElement.textContent.trim() === 'True';

    if (isStaff) {
        editorElement.innerHTML = `
            <a href="${editorUrl}">Editor</a>
        `;
    }
});

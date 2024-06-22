document.addEventListener('DOMContentLoaded', function() {
    const editorElement = document.querySelector('.editor');
    if (editorElement) {
        const editorUrl = editorElement.dataset.editorUrl;

        const userStaffElement = document.querySelector('.userStaff');
        if (userStaffElement) {
            const isStaff = userStaffElement.textContent.trim() === 'True';

            if (isStaff) {
                editorElement.innerHTML = `
                    <a href="${editorUrl}">Editor</a>
                `;
            }
        } else {
            console.error('No se encontró el elemento .userStaff en el DOM.');
        }
    } else {
        console.warn('Se verifico que el usuario no es Admin.');
    }
});

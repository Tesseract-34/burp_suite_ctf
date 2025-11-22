document.addEventListener('DOMContentLoaded', () => {
    const loginBtn = document.getElementById('loginBtn');
    const outputEl = document.getElementById('output');

    loginBtn.addEventListener('click', loginAsUser);
});

async function loginAsUser() {
    const outputEl = document.getElementById('output');
    outputEl.textContent = '⏳ Sending request...';

    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: 'guest',
                password: 'guest',
                role: 'ywiv'
            })
        });

        const data = await response.json();
        outputEl.textContent = JSON.stringify(data, null, 2);
    } catch (err) {
        outputEl.textContent = `❌ Error: ${err.message}`;
    }
}

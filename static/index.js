window.addEventListener('scroll', () => {
    localStorage.setItem('scrollY',window.scrollY);
}, false);

window.addEventListener('load', () => {
    const y = localStorage.getItem('scrollY');
    if (y) {
        document.documentElement.scrollTop = y;
    };
}, false);

// Open specific model when user clicks on button
const openForm = () => {
    document.getElementById(`add-container`).style.display = 'flex';
}

// Close modal
const closeForm = () => {
    document.getElementById(`add-container`).style.display = 'none';
}

// Hide username field if user wishes to be anonymous
const hideUsername = () => {
    document.getElementById('user').style.display = 'none';
}

// Show username input field
const showUsername = () => {
    document.getElementById('user').style.display = 'block';
}

const addShow = async () => {
    // Get body values
    const username = document.getElementById('show-username').value;
    const title = document.getElementById('show-title').value;
    const link = document.getElementById('show-link').value;
    
    // Send request
    const body = { username, title, link }; 
    try {
        const res = await fetch('/api/shows', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', },
            body: JSON.stringify(body),
        });
        // TODO: Add it in as a new item
    } catch (err) {
        console.log(err);
    } finally {
        closeForm('shows');
    }
}